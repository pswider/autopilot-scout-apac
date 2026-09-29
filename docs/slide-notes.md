# Slide by slide notes

The deck in sixteen steps. Each entry has the slide's point, what to take away, and where to go deeper. Claim by claim sourcing lives in the [fact check](fact-check.md).

---

### 01. From Vibes to Verifiable

**If it acts, it needs evidence.** The framing for the whole session is four layers, each answering one question.

| Runtime | Skills | Boundary | Tests |
| --- | --- | --- | --- |
| What actually executes | When it should act | What data can move | What proves behavior |

Go deeper. [Architecture](architecture.md), [governance](governance.md), [release gates](release-gates.md).

---

### 02. The human behind the agents

Paul Swider. Founder, CEO and Chief AI Officer of RealActivity. Microsoft MCT and MVP alumni, Tula creator, Wheelhouse AI CoE co-founder, Cloud Wars healthcare AI analyst, BOSHUG founder. Thirty years in healthcare tech.

---

### 03. Copilot Home, Code and Autopilot

Microsoft's 25 September 2026 announcement reorganized Copilot around three capabilities. **Home** brings Chat and Cowork together. **Code** builds apps and workflows with the same technology as GitHub Copilot. **Autopilot** keeps work moving as a persistent agent with its own identity.

Takeaway. The unit of work is shifting from a single prompt to a delegated, long running job, and billing is following it into usage based Copilot Credits.

Go deeper.
- [Introducing the new Copilot with Home, Code and Autopilot](https://blogs.microsoft.com/blog/2026/09/25/introducing-the-new-copilot-with-home-code-and-autopilot/)
- [Evolution of the Copilot pricing model](https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/evolution-of-the-copilot-pricing-model/4559416)
- [Frontier program](https://www.microsoft.com/en-us/copilot/resources/frontier-program)

---

### 04. Autopilot keeps working after you log off

Example prompt. *Every morning, prepare a brief from my email, calendar and Teams.* Three properties matter. It continues without you, it acts within boundaries under its own identity, and permissions and audit stay central.

Go deeper.
- [Introducing Microsoft Scout](https://www.microsoft.com/en-us/copilot/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/)
- [Microsoft Scout setup documentation](https://learn.microsoft.com/microsoft-scout)
- [Work IQ](https://www.microsoft.com/en-us/copilot/features/work-iq)

---

### 05. Governed actions need explicit boundaries

Four controls Microsoft put around the OpenClaw core.

| Control | What it gives you |
| --- | --- |
| Own governed identity | Every action is attributable to the agent, not a shared service account |
| Approved resources | Access stays within the permissions you granted |
| Human sign-off | Sensitive actions can wait for approval |
| OpenClaw foundation | Open runtime underneath, with policy conformance contributed upstream |

Go deeper.
- [Microsoft Entra Agent ID](https://learn.microsoft.com/en-us/entra/agent-id/what-is-microsoft-entra-agent-id)
- [Use Microsoft Purview for AI agents](https://learn.microsoft.com/en-us/purview/ai-agents)
- [Microsoft Agent 365 overview](https://learn.microsoft.com/en-us/microsoft-agent-365/overview)

---

### 06. Live demo 1. Autopilot and Scout preview

Follow the action and the controls. Watch for **context** (what information it uses), **boundary** (what it cannot reach without permission) and **approval** (where a human stays in the loop). Demo tenant only, no personal data.

Re-run it. [Demo guide](demos.md#demo-1-autopilot-and-scout-preview).

---

### 07. OpenClaw agent architecture

Channels feed the OpenClaw gateway. Skills decide use and non-use, workflow and privacy. The workspace holds files, FHIR data and agent memory. Actions are drafts, schedules and escalations. **Channels depend on the deployment. Skills and tools define the boundary.**

Go deeper. [Architecture](architecture.md), [OpenClaw architecture docs](https://docs.openclaw.ai/concepts/architecture), [OpenClaw skills](https://docs.openclaw.ai/tools/skills).

---

### 08. Tula tests the pattern with health data

A health focused skill layer on OpenClaw. **Private** (single user, self hosted), **specific** (records, PDFs, visit prep, portal drafts), **testable** (synthetic fixtures and behavior evals).

Go deeper. [realactivity/tula](https://github.com/realactivity/tula), [Tula safety positioning](https://github.com/realactivity/tula/blob/main/docs/safety-and-disclaimer.md).

---

### 09. Live demo 2. Inspect the contract, then test it

```text
USE FOR:        upcoming visit prep
DO NOT USE FOR: diagnosis or treatment
PRIVACY:        keep PHI in the workspace
```

```bash
waza check skills/prep-my-visit
waza run evals/prep-my-visit/eval.yaml -v
```

Re-run it. [Demo guide](demos.md#demo-2-tula-and-waza), or use the [hands-on lab](../README.md#hands-on-lab) in this repo.

---

### 10. Failure modes belong in the spec

78 defined behavior tasks across 8 skills plus a composition suite, in five dimensions.

| Dimension | Question |
| --- | --- |
| Positive | Does it do the right thing? |
| Handoff | Does it route work elsewhere? |
| PHI | Does it refuse data exfiltration? |
| Adversarial | Does it resist coercion and forced send? |
| Golden | Does complete input produce the contract output? |

Go deeper. [Patient Agent Eval Standard v0.1](https://github.com/realactivity/tula/blob/main/evals/README.md), [Waza grader reference](https://microsoft.github.io/waza/guides/graders/).

---

### 11. A passing demo is not a release gate

Two lanes. **Structural** on every PR (spec, links, task wiring, fixtures). **Live evaluation** against a real model (behavior, graders, pass rates). Tula release blockers are PHI boundary, adversarial, triage override and golden, at 0.85 by default and 1.0 for strict suites.

Go deeper. [Release gates](release-gates.md).

---

### 12. Self-hosted is not the same as governed

Self-hosted tells you **where it runs**. Governed tells you **who is acting, what data can move, which action needs approval, and what remains auditable**. Governance answers questions that hosting cannot.

Go deeper. [Governance checklist](governance.md).

---

### 13. Trust Bridge makes governance visible

Three views over patient to Microsoft 365 agent interactions. **Consent** (should this bridge exist?), **attention** (what needs intervention?), **audit** (can we explain the decision?). Synthetic demo data.

---

### 14. Live demo 3. Trace one interaction across the bridge

Filter to consent-blocked interactions, select one, follow the reason into policy and audit. **What prevented the action, and can we prove it?**

Re-run it offline. [tools/trust-bridge](../tools/trust-bridge/README.md).

---

### 15. The pattern holds across agent domains

One governance spine of identity, policy, approval, audit and evals. **Workforce** runs on Autopilot with work context, Entra identity and Microsoft 365 policy. **Patient** runs on Tula with health context, a patient boundary and safety constraints. Both sit on OpenClaw, where deployment and controls vary.

---

### 16. Build agents you can interrogate

After they act, the evidence must still be there. **Inspect. Test. Constrain. Audit.**

- [github.com/realactivity/tula](https://github.com/realactivity/tula)
- [github.com/microsoft/waza](https://github.com/microsoft/waza)
- [Microsoft Copilot announcement, 25 September 2026](https://blogs.microsoft.com/blog/2026/09/25/introducing-the-new-copilot-with-home-code-and-autopilot/)
