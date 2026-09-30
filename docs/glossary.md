# Glossary

| Term | Meaning in this talk |
| --- | --- |
| **Agent 365** | Microsoft's control plane to observe, govern and secure AI agents across an organization, built on Entra, Purview and Defender. [Docs](https://learn.microsoft.com/en-us/microsoft-agent-365/overview) |
| **Agent Plugins 1.0** | An open, vendor-neutral package format for skills and MCP server configurations. Lantern provides a source example. [Specification](https://github.com/agentplugins/agent-plugins-spec/blob/main/spec/1.0.0.md) |
| **Autopilot** | In this repo, the cloud-hosted Copilot capability announced 25 September 2026, previously called Microsoft Scout. It has its own identity, memory, computer and workspace. [Announcement](https://blogs.microsoft.com/blog/2026/09/25/introducing-the-new-copilot-with-home-code-and-autopilot/) |
| **Behavior eval** | A test that checks what an agent does, not just whether it runs. Graded against expected outputs, refusals or tool use |
| **Copilot Credits** | The usage based billing unit for premium Copilot work such as Cowork, Code and Autopilot, on top of the per user license |
| **Cowork** | Copilot's mode for delegating a whole task across apps, now inside Home |
| **Entra Agent ID** | Microsoft Entra's identity platform for AI agents, with Conditional Access, governance and audit logs. [Docs](https://learn.microsoft.com/en-us/entra/agent-id/what-is-microsoft-entra-agent-id) |
| **FHIR** | HL7 Fast Healthcare Interoperability Resources, the standard format for exchanging health records. [HL7 FHIR](https://hl7.org/fhir/) |
| **Frontier program** | Microsoft's early access program for new Copilot and agent capabilities. [Program page](https://www.microsoft.com/en-us/copilot/resources/frontier-program) |
| **Golden task** | An eval task with complete fixture input and a fixed contract output, used as a release blocker |
| **Handoff** | Routing a request that belongs to another skill, person or system instead of attempting it |
| **Lantern** | RealActivity's desktop Scout bridge, combining a skill and local MCP server using a OneDrive App Folder mailbox. RealActivity confirms the bridge was deployed and tested; work paused before the mobile app was built. [Repo](https://github.com/realactivity/scout-remote) |
| **MCP** | Model Context Protocol, an open standard for connecting agents to tools and data. [Spec](https://modelcontextprotocol.io) |
| **MCP Apps** | An MCP extension for interactive interfaces rendered inside supporting AI hosts. Separate from Agent Plugins packaging and from standalone mobile applications. [Docs](https://modelcontextprotocol.io/extensions/apps/overview) |
| **OpenClaw** | An open source personal agent runtime stewarded by the independent OpenClaw Foundation. Microsoft Scout and Tula both build on it. [Repo](https://github.com/openclaw/openclaw) |
| **PHI** | Protected health information |
| **Policy conformance** | The capability Microsoft is contributing upstream to OpenClaw so a deployment can verify it runs within its security and compliance requirements |
| **Purview** | Microsoft's data security and compliance suite. Labels, DLP and auditing apply to agent interactions. [AI agents docs](https://learn.microsoft.com/en-us/purview/ai-agents) |
| **Release blocker** | An eval tag that must pass for a release to ship, regardless of the aggregate score |
| **SKILL.md** | The file that defines a skill. Frontmatter for routing, body for workflow and rules. See the [Agent Skills specification](https://agentskills.io) |
| **SMART on FHIR** | The OAuth based standard apps use to connect to EHRs and read FHIR data. [SMART App Launch](https://hl7.org/fhir/smart-app-launch/) |
| **Structural lane** | Eval run with a mock executor on every PR. Proves wiring, not behavior |
| **Tula** | RealActivity's open source patient agent skill layer on OpenClaw. [Repo](https://github.com/realactivity/tula) |
| **Waza** | Microsoft's CLI and framework to create, test, measure and improve agent skills. [Repo](https://github.com/microsoft/waza) |
| **Work IQ** | The work context layer that grounds Copilot and Autopilot in a person's mail, meetings, chats and files. [Overview](https://www.microsoft.com/en-us/copilot/features/work-iq) |
