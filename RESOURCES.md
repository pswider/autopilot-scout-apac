# Resources

Curated links from the talk, first-party wherever possible. Mostly Microsoft, plus the OpenClaw project, the open standards underneath, and RealActivity's open source work. Checked on 30 September 2026.

## Microsoft announcements

| Resource | Why it matters |
| --- | --- |
| [Introducing the new Copilot with Home, Code and Autopilot](https://blogs.microsoft.com/blog/2026/09/25/introducing-the-new-copilot-with-home-code-and-autopilot/) | The 25 September 2026 announcement behind slides 1, 3 and 4 |
| [New Microsoft Copilot brings Home, Code, and Autopilot together](https://news.microsoft.com/source/emea/2026/09/new-microsoft-copilot-brings-home-code-and-autopilot-together/) | Microsoft Source summary with rollout details |
| [Evolution of the Copilot pricing model](https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/evolution-of-the-copilot-pricing-model/4559416) | Seat plus usage based billing in Copilot Credits |
| [Introducing Microsoft Scout, your always-on personal agent](https://www.microsoft.com/en-us/copilot/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/) | The Autopilot category, the OpenClaw foundation and the enterprise controls on slide 5 |
| [Microsoft Scout documentation](https://learn.microsoft.com/microsoft-scout) | Setup requirements for the preview |
| [Frontier program](https://www.microsoft.com/en-us/copilot/resources/frontier-program) | Early access path for Home, Code and Autopilot |
| [Work IQ](https://www.microsoft.com/en-us/copilot/features/work-iq) | The work context Autopilot builds on |

## Identity for agents

| Resource | Why it matters |
| --- | --- |
| [What is Microsoft Entra Agent ID?](https://learn.microsoft.com/en-us/entra/agent-id/what-is-microsoft-entra-agent-id) | First class identities for agents, including agents built outside Microsoft |
| [Agent identities in Microsoft Entra](https://learn.microsoft.com/en-us/entra/agent-id/agent-identities) | How an agent identity differs from a user or service principal |
| [Authorization in Microsoft Entra Agent ID](https://learn.microsoft.com/en-us/entra/agent-id/authorization-agent-id) | Roles, permission limits and high privilege blocks for agents |
| [Governing agent identities](https://learn.microsoft.com/en-us/entra/id-governance/agent-id-governance-overview) | Lifecycle, owners and sponsors |
| [Microsoft Entra Agent ID documentation hub](https://learn.microsoft.com/en-us/entra/agent-id/) | Everything else, including SDKs and OAuth flows |

## Data protection and control plane

| Resource | Why it matters |
| --- | --- |
| [Use Microsoft Purview to manage data security and compliance for AI agents](https://learn.microsoft.com/en-us/purview/ai-agents) | Labels, DLP and auditing for agent interactions |
| [How Microsoft Purview supports Agent 365](https://learn.microsoft.com/en-us/microsoft-agent-365/guidance/purview-agent-365) | One compliance model for people and agents |
| [Microsoft Agent 365 overview](https://learn.microsoft.com/en-us/microsoft-agent-365/overview) | Registry, access control and observability for the agent fleet |
| [Why does an enterprise need Agent 365?](https://learn.microsoft.com/en-us/microsoft-agent-365/guidance/why-agent-365-for-enterprise) | The agent sprawl argument |
| [Secure AI agents at scale using Microsoft Agent 365](https://learn.microsoft.com/en-us/security/security-for-ai/agent-365-security) | How Defender, Entra and Purview divide the work |
| [Agents hub on Microsoft Learn](https://learn.microsoft.com/en-us/agents/) | Starting point across Copilot Studio, Foundry and Agent 365 |

## Evaluation with Waza

| Resource | Why it matters |
| --- | --- |
| [microsoft/waza](https://github.com/microsoft/waza) | The CLI used on slides 9 to 11 |
| [Waza documentation site](https://microsoft.github.io/waza/) | Guides and reference |
| [Getting started](https://github.com/microsoft/waza/blob/main/docs/GETTING-STARTED.md) | init, new, run, check in five minutes |
| [Grader reference](https://microsoft.github.io/waza/guides/graders/) | text, code, behavior, action sequence, prompt and more |
| [Skills CI integration](https://github.com/microsoft/waza/blob/main/docs/SKILLS_CI_INTEGRATION.md) | GitHub Actions patterns |
| [Adversarial harness guide](https://microsoft.github.io/waza/guides/adversarial/) | Built-in prompt injection and scope bypass packs |
| [Azure/PyRIT](https://github.com/Azure/PyRIT) | Microsoft's open source red teaming toolkit for generative AI, for going deeper on adversarial testing |

## OpenClaw

| Resource | Why it matters |
| --- | --- |
| [openclaw/openclaw](https://github.com/openclaw/openclaw) | The runtime under Scout and Tula |
| [OpenClaw documentation](https://docs.openclaw.ai) | Install, channels, tools and gateway |
| [Architecture](https://docs.openclaw.ai/concepts/architecture) | Gateway, sessions and nodes |
| [Skills](https://docs.openclaw.ai/tools/skills) | How skills load and route |
| [Security guide](https://docs.openclaw.ai/gateway/security) | Read before exposing a gateway |
| [Sandboxing guide](https://docs.openclaw.ai/gateway/sandboxing) | Tools run on the host unless you configure this |
| [ClawHub](https://clawhub.ai) | Community registry for skills and plugins |
| [OpenClaw Foundation](https://openclaw.org) | Independent steward of the project |

## Tula and the Patient Agent Eval Standard

| Resource | Why it matters |
| --- | --- |
| [realactivity/tula](https://github.com/realactivity/tula) | Open source patient agent on OpenClaw |
| [Patient Agent Eval Standard v0.1](https://github.com/realactivity/tula/blob/main/evals/README.md) | The 78 task, five dimension eval standard from slide 10 |
| [TAXONOMY.yaml](https://github.com/realactivity/tula/blob/main/evals/TAXONOMY.yaml) | Release blockers and thresholds from slide 11 |
| [prep-my-visit SKILL.md](https://github.com/realactivity/tula/blob/main/skills/prep-my-visit/SKILL.md) | The contract shown in demo 2 |
| [Safety and disclaimer](https://github.com/realactivity/tula/blob/main/docs/safety-and-disclaimer.md) | What Tula is not |
| [Tula live demo video](https://youtu.be/FcLl6fASpgw) | About sixteen minutes, end to end |

## Open standards

| Resource | Why it matters |
| --- | --- |
| [Agent Skills specification](https://agentskills.io) | The `SKILL.md` format Waza validates against |
| [Model Context Protocol](https://modelcontextprotocol.io) | How agents connect to tools and data |
| [HL7 FHIR](https://hl7.org/fhir/) | The health data format in Tula's workspace |
| [SMART App Launch](https://hl7.org/fhir/smart-app-launch/) | How Tula connects to patient portals |
| [Azure Health Data Services FHIR service](https://learn.microsoft.com/en-us/azure/healthcare-apis/fhir/overview) | Microsoft's managed FHIR server |
| [OpenTelemetry semantic conventions for generative AI](https://opentelemetry.io/docs/specs/semconv/gen-ai/) | A shared shape for agent traces |

## Responsible AI

| Resource | Why it matters |
| --- | --- |
| [Microsoft Responsible AI](https://www.microsoft.com/en-us/ai/responsible-ai) | Principles, standard and transparency reports |
| [Enterprise data protection in Microsoft 365 Copilot](https://learn.microsoft.com/en-us/copilot/microsoft-365/enterprise-data-protection) | What Copilot does and does not do with your data |
