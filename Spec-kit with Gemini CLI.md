
# Spec‑Kit + Gemini CLI (Simple Quickstart)

Spec-Driven Development flips the script on traditional software development. For decades, code has been king — specifications were just scaffolding we built and discarded once the "real work" of coding began. Spec-Driven Development changes this: specifications become executable, directly generating working implementations rather than just guiding them.

---

## Prerequisites

- **Python 3.11+**
- **Git**
- **uv** for package management (https://docs.astral.sh/uv/)
- **Gemini CLI** installed and runnable from your terminal
- A Gemini API key available as an environment variable

> Note: The Gemini CLI can be configured to query the ADK documentation using the ADK Docs Extension.

Install it with:

```bash
gemini extensions install https://github.com/derailed-dash/adk-docs-ext
```

---

##  Get Started
## 1) Install the Specify CLI

Recommended (install once):

```bash
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
```

Verify:

```bash
specify --help
```

One-time usage (no install):

```bash
uvx --from git+https://github.com/github/spec-kit.git specify --help
```

---


## 2) Initialize a Spec‑Kit project

Create a new project directory:

```bash
specify init <PROJECT_NAME>
```
After initializing, Select the appropriate AI interface.(eg: gemini, claude)

Initialize inside an existing repo/folder:

```bash
specify init --here --ai gemini
```

After init, you should see a Spec‑Kit structure created for specs/plans/tasks.

---

## 3) Start Gemini CLI in the project folder

In a terminal, `cd` into the initialized project and launch Gemini CLI.


Once Gemini CLI is running in the project directory, you can use:

- `/speckit.constitution`
- `/speckit.specify`
- `/speckit.plan`
- `/speckit.tasks`
- `/speckit.implement`
- `/speckit.clarify`
- `/speckit.checklist`
- `/speckit.analyze`
---
## 4) Run the Spec‑Driven workflow

### Step A — Constitution (project rules)

Define the rules that all future work must follow:

```
/speckit.constitution Create a constitution file for governing principles and development guidelines for an ADK-based Terraform Workflow Orchestrator using a hierarchical team-of-agents pattern.
```

Include things like:

- Code quality standards (formatting, linting)
- Testing expectations (unit/integration, coverage targets)
- UX consistency rules
- Performance and reliability constraints

> Note: You can manually generate/modify the `.specify\memory\constitution.md` file based on the requirements.

### Step B — Specification (what & why)

Describe the feature in user-focused terms (no tech stack):

```
/speckit.specify Build a tool that turns an infrastructure request into Terraform code through a clear workflow: propose a design, get approval, then generate and validate.
It must produce a complete repo-style output plus validation results, and ask clarifying questions when requirements are missing or risky.
```

Good inputs:

- user behaviors and scenarios
- constraints and acceptance criteria
- edge cases

Avoid:

- libraries/frameworks
- architecture decisions

### Step C — Clarify (optional)

If anything is ambiguous, force the questions early:

```
/speckit.clarify
```

### Step D — Plan (how)

Now choose the tech stack and architecture:

```
/speckit.plan Create a plan for the Terraform Workflow Orchestrator. I am building with ADK Python, using gemini-2.5-flash for specialist agents and gemini-2.5-pro for orchestration decisions. The system uses a hierarchical team-of-agents pattern with 9 specialist agents. Deploy to Cloud Run with Vertex AI Session Service for state persistence. Include OpenTelemetry tracing and BigQuery Analytics for observability.
```

Keep it concrete:

- components/modules
- data model
- APIs
- storage
- key tradeoffs

### Step E — Tasks (doable work items)

Generate an execution-ready task list:

```
/speckit.tasks Break the orchestrator plan into implementation tasks. Organize by multi-agent pattern demonstration: first setup, then foundational orchestrator, then each specialist agent as an independent scenario, then integration and polish.
```

### Step F — Analyze (optional but valuable)

Consistency and coverage check across artifacts:

```
/speckit.analyze Run a project analysis for ADK agent consistency across spec, plan, and tasks
```



### Step G — Implement

Execute tasks according to your constitution and plan:

```
/speckit.implement Start the ADK multi-agent implementation in phases. Begin with project setup, then foundational orchestrator, then each specialist agent independently, then integration.
```
### Step H — Checklist (optional)
Generate a quality checklist ("unit tests for English"):

```
/speckit.checklist
```
---
## Practical tips

- Treat the **constitution** as “non-negotiable constraints.” Update it when standards change.
- Keep the **spec** focused on outcomes and acceptance criteria; put “how” into the **plan**.
- Run **/speckit.clarify** as soon as you feel uncertainty—rewriting code is costlier than clarifying intent.
- Run **/speckit.analyze** before implementation to catch drift (spec vs plan vs tasks).

## Troubleshooting

- **`/speckit.*` commands don’t show up**: ensure you ran `specify init` in that folder, then start Gemini CLI from the initialized project directory.
- **Auth errors**: confirm `GEMINI_API_KEY` is set in the same shell where you launch Gemini CLI.

---
## Resources
- https://github.com/github/spec-kit?tab=readme-ov-file
- https://github.com/google-gemini/gemini-cli
- https://google.github.io/adk-docs/
---