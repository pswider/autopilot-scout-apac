#!/usr/bin/env python3
"""Rebuild the synthetic, hash-chained audit log used by the Trust Bridge demo.

Every entry stores the SHA-256 of the previous entry, so changing any past
record breaks the chain from that point on. That is what lets explain.py answer
"can we prove it?" instead of only "what happened?".

SYNTHETIC DEMO DATA ONLY.
"""

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "data" / "audit-log.jsonl"
GENESIS = "0" * 64

# (event id, time, actor, bridge, action, data classes, decision, policy, reason)
EVENTS = [
    ("evt-0001", "2026-09-22T08:02:11Z", "agent:tula-demo", "BR-01", "share", ["scheduling"],
     "allowed", "POL-SCOPE-03", "Scheduling data only, bridge consent active"),
    ("evt-0002", "2026-09-22T08:02:40Z", "agent:autopilot-scheduling-demo", "BR-01", "schedule", ["scheduling"],
     "allowed", "POL-SCOPE-03", "Appointment moved to 2026-10-14 09:30 within granted scope"),
    ("evt-0003", "2026-09-23T13:15:05Z", "agent:tula-demo", "BR-01", "share", ["scheduling", "lab-results"],
     "blocked", "POL-SCOPE-03", "Lab values requested by a workforce agent, scope covers scheduling only"),
    ("evt-0004", "2026-09-24T09:40:18Z", "agent:tula-demo", "BR-03", "draft", ["visit-brief"],
     "allowed", "POL-PHI-01", "Visit brief drafted inside workspace, nothing sent"),
    ("evt-0005", "2026-09-24T09:41:02Z", "agent:tula-demo", "BR-03", "send", ["visit-brief"],
     "held", "POL-SEND-02", "Awaiting patient approval before delivery"),
    ("evt-0006", "2026-09-24T10:05:57Z", "patient:sam-rivera-demo", "BR-03", "approve", ["visit-brief"],
     "allowed", "POL-SEND-02", "Patient approved delivery of visit brief"),
    ("evt-0007", "2026-09-25T07:30:00Z", "agent:employer-wellness-demo", "BR-02", "request", ["lab-results", "wellness-summary"],
     "blocked", "POL-PHI-01", "Consent for BR-02 revoked on 2026-09-10, no data may cross"),
    ("evt-0008", "2026-09-26T16:12:44Z", "agent:tula-demo", "BR-03", "send", ["visit-brief", "medications"],
     "blocked", "POL-PHI-01", "Medications outside consented scope visit-brief"),
    ("evt-0009", "2026-09-27T11:00:09Z", "agent:tula-demo", "BR-01", "send", ["scheduling"],
     "blocked", "POL-SEND-02", "Forced send without patient approval refused"),
    ("evt-0010", "2026-09-28T08:00:00Z", "agent:autopilot-scheduling-demo", "BR-01", "schedule", ["scheduling"],
     "allowed", "POL-SCOPE-03", "Reminder scheduled for 2026-10-13 within granted scope"),
]


def entry_hash(entry: dict) -> str:
    body = {k: v for k, v in entry.items() if k != "hash"}
    return hashlib.sha256(json.dumps(body, sort_keys=True).encode()).hexdigest()


def main() -> None:
    prev = GENESIS
    lines = []
    for seq, (eid, ts, actor, bridge, action, data, decision, policy, reason) in enumerate(EVENTS, start=1):
        entry = {
            "seq": seq,
            "event_id": eid,
            "time": ts,
            "actor": actor,
            "bridge": bridge,
            "action": action,
            "data_classes": data,
            "decision": decision,
            "policy": policy,
            "reason": reason,
            "prev_hash": prev,
        }
        entry["hash"] = entry_hash(entry)
        prev = entry["hash"]
        lines.append(json.dumps(entry, sort_keys=True))
    OUT.write_text("\n".join(lines) + "\n")
    print(f"wrote {len(lines)} entries to {OUT.relative_to(HERE)}")


if __name__ == "__main__":
    main()
