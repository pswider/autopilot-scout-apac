# Fact check

Every factual claim in the deck, checked against first-party sources where they exist. Checked on **30 September 2026**. Preview features, names and billing change often, so treat anything marked *preview* as a snapshot.

**Status key**

| Mark | Meaning |
| --- | --- |
| ✅ Verified | A first-party source says this directly |
| 🟡 Nuance | Accurate, with context worth adding when you repeat it |
| 🔄 Update | Was accurate when written, a source now says something newer |

## Sources

| ID | Source | Publisher |
| --- | --- | --- |
| **S1** | [Introducing the new Copilot with Home, Code and Autopilot](https://blogs.microsoft.com/blog/2026/09/25/introducing-the-new-copilot-with-home-code-and-autopilot/) (25 Sep 2026) | Official Microsoft Blog |
| **S2** | [New Microsoft Copilot brings Home, Code, and Autopilot together](https://news.microsoft.com/source/emea/2026/09/new-microsoft-copilot-brings-home-code-and-autopilot-together/) (25 Sep 2026) | Microsoft Source EMEA |
| **S3** | [Introducing Microsoft Scout, your always-on personal agent](https://www.microsoft.com/en-us/copilot/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/) (2 Jun 2026, updated 25 Sep 2026) | Microsoft AI at Work Blog |
| **S4** | [Evolution of the Copilot pricing model](https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/evolution-of-the-copilot-pricing-model/4559416) (25 Sep 2026) | Microsoft Tech Community |
| **S5** | [microsoft/waza](https://github.com/microsoft/waza) README and [docs](https://microsoft.github.io/waza/) | Microsoft |
| **S6** | [realactivity/tula](https://github.com/realactivity/tula) README | RealActivity |
| **S7** | [Patient Agent Eval Standard v0.1](https://github.com/realactivity/tula/blob/main/evals/README.md) and [TAXONOMY.yaml](https://github.com/realactivity/tula/blob/main/evals/TAXONOMY.yaml) | RealActivity |
| **S8** | [openclaw/openclaw](https://github.com/openclaw/openclaw) README and [docs](https://docs.openclaw.ai) | OpenClaw Foundation |
| **S9** | [What is Microsoft Entra Agent ID?](https://learn.microsoft.com/en-us/entra/agent-id/what-is-microsoft-entra-agent-id) | Microsoft Learn |
| **S10** | [prep-my-visit SKILL.md](https://github.com/realactivity/tula/blob/main/skills/prep-my-visit/SKILL.md) | RealActivity |

## Slide 1. Title

| Claim | Status | Source and note |
| --- | --- | --- |
| Microsoft's new Autopilot keeps working after you log off | ✅ Verified | S1 describes a persistent, proactive agent that keeps working even when you are not, hosted in the tenant. See slide 4 for the one caveat about the earlier desktop preview. |

## Slide 3. Copilot Home, Code and Autopilot

| Claim | Status | Source and note |
| --- | --- | --- |
| Announced 25 September 2026 | ✅ Verified | S1, S2 |
| Home brings Chat and Cowork together | ✅ Verified | S1, S2. Home is the new starting point in the Copilot app. |
| Chat is for asking, drafting and analyzing. Cowork delegates a task across apps | ✅ Verified | S2 describes Chat for day to day work and Cowork for delegating entire tasks. |
| Code creates apps and workflows with GitHub Copilot technology | ✅ Verified | S1 says Code is powered by the same underlying technology as GitHub Copilot. Code runs sandboxed and can be hosted in the tenant, alongside Copilot Managed Runtime in preview. |
| Autopilot is a persistent agent with its own identity, memory and workspace | ✅ Verified | S1, as quoted in coverage of the announcement, describes Autopilot living in your tenant with its own identity, memory, execution environment and workspace. Identity is also stated directly in S3. |
| Home and Code roll out through Frontier. Autopilot expands to private preview | ✅ Verified | S1 says Home and Code roll out in Frontier in the coming weeks and Autopilot expands to private preview at the end of the month. |
| Copilot seat plus usage charges for Cowork, Code and Autopilot | ✅ Verified | S4. Everyday use stays in the per user license. Premium work runs on usage based billing in Copilot Credits, and for enterprises it stays off until an admin creates a spending policy in the Microsoft 365 admin center. |

## Slide 4. Autopilot keeps working after you log off

| Claim | Status | Source and note |
| --- | --- | --- |
| Autopilot was formerly Microsoft Scout | ✅ Verified | S3 now carries the banner "Microsoft Scout is now Autopilot." |
| Morning brief example from email, calendar and Teams | ✅ Verified | S3 lists Teams, Outlook, OneDrive and SharePoint plus chats, email, calendar and contacts as its grounding. The brief itself is an illustrative prompt. |
| Runs in the cloud and continues while your device is off | ✅ Verified | S1 positions Autopilot as hosted in the Microsoft 365 tenant and working even when you are not. Worth one line on stage. The June Scout preview was a desktop app plus cloud services (S3), so if your demo tenant still runs that preview, call it the earlier Scout experience. |
| Acts within set boundaries, with its own identity and workspace | ✅ Verified | S3. Autopilots carry out tasks within the permissions and policies you and your organization set. |
| Private preview expands at the end of September | ✅ Verified | S1 |

## Slide 5. Autopilot governance

| Claim | Status | Source and note |
| --- | --- | --- |
| Own governed identity, actions attributed to the agent | ✅ Verified | S3. Every agent runs under its own governed Entra identity, not a shared service account. See also S9 for the Entra Agent ID platform. |
| Access stays within granted permissions | ✅ Verified | S3. Agents reach only resources and destinations you have approved. Credentials are scoped to the task and redacted from logs. |
| Sensitive actions can require human approval | ✅ Verified | S3 |
| Microsoft described Scout as powered by OpenClaw | ✅ Verified | S3 says it is powered by OpenClaw open source technology. S3 also says Microsoft is contributing policy conformance upstream to OpenClaw. |

## Slide 7. OpenClaw agent architecture

| Claim | Status | Source and note |
| --- | --- | --- |
| Gateway, tools, memory and skills make up the runtime | ✅ Verified | S8. The Gateway is the local control plane for sessions, tools, events and channel connections. Tools, skills and plugins extend it. |
| Channels include Teams and Telegram | ✅ Verified | S8 lists Teams, Telegram and more than twenty others. |
| Email as a channel | 🟡 Nuance | Deployment specific. Tula uses email ingestion locked to an Exchange sender allowlist (S6). The slide already says channels depend on the deployment. |
| FHIR in the workspace | ✅ Verified | S6. Tula pulls records with SMART on FHIR into a private workspace. |

## Slide 8. Tula

| Claim | Status | Source and note |
| --- | --- | --- |
| A health focused skill layer on OpenClaw | ✅ Verified | S6 |
| Private, single user, self hosted workspace | ✅ Verified | S6. The reference deployment runs on a single self hosted VM. |
| Records, PDFs, visit prep, portal drafts | ✅ Verified | S6 lists `health-records`, `med-pdf`, `prep-my-visit` and `epic-note` as live. |
| Synthetic fixtures and behavior evals | ✅ Verified | S7. All public fixtures use a fictional persona. |

## Slide 9. Live demo 2, Tula and Waza

| Claim | Status | Source and note |
| --- | --- | --- |
| USE FOR upcoming visit prep. DO NOT USE FOR diagnosis or treatment. Keep PHI in the workspace | ✅ Verified | S10. The published contract matches the slide. |
| `waza check skills/prep-my-visit` | ✅ Verified | S5 documents `waza check [skill-path]`. |
| `waza run evals/prep-my-visit/eval.yaml -v` | ✅ Verified | S5 documents `waza run <eval.yaml>` with `-v`. |

## Slide 10. Behavior evaluation

| Claim | Status | Source and note |
| --- | --- | --- |
| 78 defined behavior tasks | ✅ Verified | S7 suite table sums to 78 (8 + 8 + 6 + 6 + 7 + 16 + 12 + 9 + 6). |
| 8 skills plus composition | ✅ Verified | S7 |
| Positive, handoff, PHI, adversarial, golden | ✅ Verified | S7 tags `routing-positive`, `routing-negative`, `phi-boundary`, `adversarial`, `golden`. |
| Live pass rates are not published in the public status page | 🔄 Update | The Tula README now shows one local snapshot, `request-amendment` passing 8 of 10 tasks with an aggregate score of 0.97 (S6). Full live pass rates across all suites are still not published. |

## Slide 11. Release gates

| Claim | Status | Source and note |
| --- | --- | --- |
| Structural checks on every PR, live evaluation against a model | ✅ Verified | S7 two lane model. `eval.mock.yaml` with the mock executor on every PR, `eval.yaml` with `copilot-sdk` for certification. |
| Release blockers are PHI boundary, adversarial, triage override and golden | ✅ Verified | S7 `release_blockers` |
| Thresholds 0.85, and 1.0 for strict suites | ✅ Verified | S7 `live_lane_default: 0.85`, `live_lane_strict: 1.0`, with `prep-my-visit` named as strict. |

## Slide 12 to 16

The governance gap, Trust Bridge and reusable pattern slides are the speaker's argument rather than factual claims. The Microsoft controls they lean on are verified above (identity, approved resources, sign-off, Purview enforcement). The closing links resolve to [realactivity/tula](https://github.com/realactivity/tula) and [microsoft/waza](https://github.com/microsoft/waza).

## Worth adding next time

- Microsoft is contributing **policy conformance** upstream to OpenClaw so any OpenClaw deployment can check whether it is configured within its security and compliance requirements (S3). It strengthens slide 12.
- **Microsoft Entra Agent ID** works with agents built on non-Microsoft platforms through the Entra SDK sidecar or workload identity federation (S9). That is the path from "self-hosted" toward "governed" for a Tula style agent.
- Waza now ships **built-in adversarial packs** (`prompt-injection`, `scope-bypass`) through `waza adversarial` (S5). A natural companion to the Tula adversarial tasks.
