#!/usr/bin/env python3
"""Trust Bridge explainer. Answers one question from the talk:

    What prevented the action, and can we prove it?

Reads synthetic consents, policies and a hash-chained audit log, then:
  --blocked          list every consent- or policy-blocked interaction (Filter)
  --event EVT-ID     trace one interaction into bridge, consent and policy (Select + Explain)
  --verify           check the whole audit chain is intact (Prove)
  --tamper EVT-ID    simulate someone quietly editing a past decision, then verify

Standard library only. SYNTHETIC DEMO DATA ONLY.
"""

import argparse
import copy
import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
GENESIS = "0" * 64

BOLD, DIM, RED, GREEN, AMBER, RESET = "\033[1m", "\033[2m", "\033[31m", "\033[32m", "\033[33m", "\033[0m"
if not sys.stdout.isatty():
    BOLD = DIM = RED = GREEN = AMBER = RESET = ""

MARK = {"allowed": f"{GREEN}ALLOWED{RESET}", "blocked": f"{RED}BLOCKED{RESET}", "held": f"{AMBER}HELD{RESET}"}


def load():
    policies = {p["id"]: p for p in json.loads((DATA / "policies.json").read_text())["policies"]}
    consents = json.loads((DATA / "consents.json").read_text())
    bridges = {b["id"]: b for b in consents["bridges"]}
    log = [json.loads(line) for line in (DATA / "audit-log.jsonl").read_text().splitlines() if line.strip()]
    return policies, bridges, log


def entry_hash(entry: dict) -> str:
    body = {k: v for k, v in entry.items() if k != "hash"}
    return hashlib.sha256(json.dumps(body, sort_keys=True).encode()).hexdigest()


def verify_chain(log):
    """Return (ok, first_bad_seq, message)."""
    prev = GENESIS
    for e in log:
        if e["prev_hash"] != prev:
            return False, e["seq"], f"entry {e['seq']} does not link to entry {e['seq'] - 1}"
        if entry_hash(e) != e["hash"]:
            return False, e["seq"], f"entry {e['seq']} ({e['event_id']}) was modified after it was written"
        prev = e["hash"]
    return True, None, f"{len(log)} entries, every hash links to the one before it"


def cmd_blocked(policies, bridges, log):
    rows = [e for e in log if e["decision"] == "blocked"]
    print(f"\n{BOLD}Filter. Blocked interactions across the bridge{RESET}  ({len(rows)} of {len(log)})\n")
    print(f"  {'EVENT':<10}{'TIME (UTC)':<22}{'BRIDGE':<8}{'ACTION':<10}{'POLICY':<14}REASON")
    for e in rows:
        print(f"  {e['event_id']:<10}{e['time'][:16].replace('T', ' '):<22}{e['bridge']:<8}"
              f"{e['action']:<10}{e['policy']:<14}{e['reason']}")
    print(f"\n{DIM}Next. python3 tools/trust-bridge/explain.py --event {rows[0]['event_id'] if rows else 'evt-0007'}{RESET}\n")


def cmd_event(policies, bridges, log, event_id):
    match = [e for e in log if e["event_id"].lower() == event_id.lower()]
    if not match:
        sys.exit(f"No event {event_id}. Try --blocked to list them.")
    e = match[0]
    b = bridges[e["bridge"]]
    p = policies[e["policy"]]
    c = b["consent"]
    ok, bad, msg = verify_chain(log)

    print(f"\n{BOLD}Select. {e['event_id']}{RESET}  {MARK[e['decision']]}\n")
    print(f"  {BOLD}What was attempted{RESET}")
    print(f"    {e['actor']} tried to {e['action']} {', '.join(e['data_classes'])}")
    print(f"    at {e['time']} across {b['id']}, {b['from']} to {b['to']}")
    print(f"    bridge purpose. {b['purpose']}\n")

    print(f"  {BOLD}Consent. Should this bridge exist?{RESET}")
    extra = f", revoked {c['revoked']}" if c.get("revoked") else f", expires {c.get('expires', 'n/a')}"
    print(f"    status {c['status']}, scope {', '.join(c['scope'])}, granted {c['granted']}{extra}")
    outside = [d for d in e["data_classes"] if d not in c["scope"]]
    if c["status"] != "active":
        print(f"    {RED}no active consent, nothing may cross{RESET}")
    elif outside:
        print(f"    {RED}outside consented scope. {', '.join(outside)}{RESET}")
    else:
        print(f"    {GREEN}within consented scope{RESET}")
    print()

    print(f"  {BOLD}Policy. What prevented or allowed it?{RESET}")
    print(f"    {p['id']}  {p['title']}")
    print(f"    {p['rule']}")
    print(f"    {DIM}Microsoft 365 analogue. {p['maps_to']}{RESET}")
    print(f"    recorded reason. {e['reason']}\n")

    print(f"  {BOLD}Audit. Can we prove it?{RESET}")
    print(f"    entry #{e['seq']}  hash {e['hash'][:16]}...  prev {e['prev_hash'][:16]}...")
    if ok:
        print(f"    {GREEN}chain verified{RESET}. {msg}\n")
    else:
        print(f"    {RED}chain broken{RESET}. {msg}\n")


def cmd_verify(log, label="Prove. Audit chain"):
    ok, bad, msg = verify_chain(log)
    state = f"{GREEN}INTACT{RESET}" if ok else f"{RED}BROKEN{RESET}"
    print(f"\n{BOLD}{label}{RESET}  {state}\n  {msg}\n")
    return ok


def cmd_tamper(log, event_id):
    forged = copy.deepcopy(log)
    target = [e for e in forged if e["event_id"].lower() == event_id.lower()]
    if not target:
        sys.exit(f"No event {event_id}.")
    t = target[0]
    before = t["decision"]
    t["decision"] = "allowed"
    t["reason"] = "Approved"
    print(f"\n{BOLD}Tamper simulation{RESET}. Quietly changing {t['event_id']} from {before} to allowed, in memory only.")
    cmd_verify(forged, label="Prove. Audit chain after tampering")


def main():
    ap = argparse.ArgumentParser(description="What prevented the action, and can we prove it? (synthetic demo)")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--blocked", action="store_true", help="list blocked interactions")
    g.add_argument("--event", metavar="EVT-ID", help="trace one interaction")
    g.add_argument("--verify", action="store_true", help="verify the audit hash chain")
    g.add_argument("--tamper", metavar="EVT-ID", help="simulate editing a past decision, then verify")
    args = ap.parse_args()

    policies, bridges, log = load()
    if args.blocked:
        cmd_blocked(policies, bridges, log)
    elif args.event:
        cmd_event(policies, bridges, log, args.event)
    elif args.verify:
        sys.exit(0 if cmd_verify(log) else 1)
    elif args.tamper:
        cmd_tamper(log, args.tamper)


if __name__ == "__main__":
    main()
