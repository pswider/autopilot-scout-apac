# Demo guide

How to re-run the three live demos from the talk, what to point at, and what the audience should take away. Every demo uses a demo tenant or synthetic data only.

---

## Demo 1. Autopilot and Scout preview

**Goal.** Follow one delegated action and name the control at each step.

**Prerequisites.** Access to the Autopilot private preview in a demo tenant. Microsoft's Scout setup requires Frontier enrollment, an Intune policy configuration and an opt-in attestation. See [Microsoft Scout documentation](https://learn.microsoft.com/microsoft-scout).

| Step | Say | Show |
| --- | --- | --- |
| 1. Context | What information does it use to complete the task? | The morning brief prompt, and the mail, calendar and Teams items it draws on |
| 2. Boundary | What can it not reach without permission? | The agent's own identity and the resources it has been granted |
| 3. Approval | Where does a human stay in the loop? | A sensitive action waiting for sign-off |

**Takeaway.** Identity, boundary and approval are properties of the agent, not of the prompt.

**Fallback if the preview is unavailable.** Walk the same three steps on slide 5 using Microsoft's published description of the controls in [Introducing Microsoft Scout](https://www.microsoft.com/en-us/copilot/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/).

---

## Demo 2. Tula and Waza

**Goal.** Show that the skill contract and its failure modes are written down and tested.

**Against Tula**

```bash
git clone https://github.com/realactivity/tula.git && cd tula
waza check skills/prep-my-visit
waza run evals/prep-my-visit/eval.yaml -v        # live lane, needs GitHub Copilot auth
waza run evals/prep-my-visit/eval.mock.yaml --skip-graders -v   # structural lane, no key
```

**Against this repo's smaller sample**

```bash
waza check skills/visit-prep-lite
waza spec verify skills/visit-prep-lite evals/visit-prep-lite/eval.yaml
waza run evals/visit-prep-lite/eval.mock.yaml --skip-graders -v
```

| Step | Show |
| --- | --- |
| Open `SKILL.md` | The `USE FOR` and `DO NOT USE FOR` lines, and the privacy rules |
| Open a failure test | [`adversarial-forced-send.yaml`](../evals/visit-prep-lite/tasks/adversarial-forced-send.yaml), with its three refusal graders |
| Run Waza | `check` for readiness, `spec verify` to prove every promise has a test, `run` for behavior |

**A good moment to improvise.** Delete one task file and run `waza spec verify` again. Waza names the promise in `SKILL.md` that no longer has a test.

**Takeaway.** A passing demo is not a release gate. The failure modes belong in the spec.

---

## Demo 3. Trust Bridge

**Goal.** Trace one blocked interaction into policy and audit, then prove the record has not been changed.

```bash
python3 tools/trust-bridge/explain.py --blocked           # 01 Filter
python3 tools/trust-bridge/explain.py --event evt-0007    # 02 Select, 03 Explain
python3 tools/trust-bridge/explain.py --verify            # Prove
python3 tools/trust-bridge/explain.py --tamper evt-0007   # and show what tampering looks like
```

**Takeaway.** Governance you cannot explain afterwards is governance you cannot defend.

See the [Trust Bridge README](../tools/trust-bridge/README.md) for how the hash chain works.
