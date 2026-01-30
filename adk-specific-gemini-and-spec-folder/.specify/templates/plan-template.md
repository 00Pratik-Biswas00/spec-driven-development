# ADK Agent Implementation Plan: [AGENT/FEATURE NAME]

**Branch**: `[###-feature-name]` | **Date**: [DATE] | **Spec**: [link]
**Input**: Agent specification from `/specs/[###-feature-name]/spec.md`

**Note**: This template is filled in by the `/speckit.plan` command for ADK agent development.

## Summary

[Extract from agent spec: primary agent purpose + architecture approach from research]

## ADK Technical Context

<!--
  ACTION REQUIRED: Replace with ADK-specific technical details.
  This section defines the ADK agent architecture and implementation approach.
-->

**ADK Version**: [e.g., google-adk 1.0.0 or NEEDS CLARIFICATION]  
**Python Version**: [e.g., Python 3.10+ (ADK requirement) or NEEDS CLARIFICATION]  
**Primary Model**: [e.g., gemini-2.5-flash, gemini-2.5-pro or NEEDS CLARIFICATION]  
**Agent Architecture**: [LlmAgent | SequentialAgent | ParallelAgent | LoopAgent | Multi-Agent System or NEEDS CLARIFICATION]  
**Deployment Target**: [e.g., Local (adk run), Vertex AI Agent Engine, Cloud Run or NEEDS CLARIFICATION]  
**Session Management**: [e.g., In-memory, Vertex AI Session Service or NEEDS CLARIFICATION]  
**Memory Services**: [e.g., None, Vertex AI RAG Memory, Custom memory or NEEDS CLARIFICATION]  
**Testing Framework**: [e.g., pytest with ADK AgentEvaluator or NEEDS CLARIFICATION]  
**Observability**: [e.g., OpenTelemetry, BigQuery Analytics, AgentOps or NEEDS CLARIFICATION]

### Agent Type Selection Rationale

**Chosen Architecture**: [Selected agent type]

**Why this architecture**:
- [Reason 1: e.g., "SequentialAgent chosen because tasks must execute in order"]
- [Reason 2: e.g., "ParallelAgent chosen for independent data collection"]
- [Reason 3: e.g., "Multi-agent system chosen for specialized sub-tasks"]

**Alternative Architectures Considered**:
- [Alternative 1]: [Why not chosen]
- [Alternative 2]: [Why not chosen]

### Tool Ecosystem

**Required Tools**:
1. **[Tool Name]**: [Purpose]
   - Type: [FunctionTool | LongRunningFunctionTool | AgentTool | Built-in | Toolset]
   - Implementation: [Brief description]
   - Confirmation Required: [Yes/No]

2. **[Tool Name]**: [Purpose]
   - Type: [Tool type]
   - Implementation: [Brief description]
   - Confirmation Required: [Yes/No]

**Google Cloud Integration** (if applicable):
- [ ] Vertex AI Search
- [ ] BigQuery
- [ ] Pub/Sub
- [ ] Cloud Storage
- [ ] Other: [Specify]

### State Management Strategy

**State Keys**:
- `[key_name]`: [Purpose, e.g., "user_preferences - stores user settings"]
- `[key_name]`: [Purpose, e.g., "analysis_results - stores intermediate analysis"]
- `[key_name]`: [Purpose, e.g., "conversation_context - tracks conversation state"]

**State Flow**:
```
[Agent/Phase 1] → state["key1"] → [Agent/Phase 2] → state["key2"] → [Agent/Phase 3]
```

**Session Strategy**:
- Session Duration: [e.g., "Per conversation", "24 hours", "Persistent"]
- Session Storage: [e.g., "In-memory", "Vertex AI Session Service"]
- State Persistence: [e.g., "None", "Save to Cloud Storage after each conversation"]

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

[Gates determined based on constitution file - ADK-specific principles]

**ADK Best Practices Check**:
- [ ] Single Responsibility: Each agent has one clear purpose
- [ ] Tool Documentation: All tools have clear docstrings
- [ ] State Keys: Unique, descriptive state keys
- [ ] Error Handling: Graceful error handling in tools and agents
- [ ] Testing: Plan includes agent evaluation strategy
- [ ] Observability: Tracing and logging configured

## Project Structure

### Documentation (this feature)

```text
specs/[###-feature]/
├── spec.md              # Agent specification
├── plan.md              # This file (implementation plan)
├── research.md          # Phase 0 output (tool/model research)
├── agent-architecture.md # Phase 1 output (detailed agent design)
├── tool-specifications.md # Phase 1 output (tool implementations)
├── prompts/             # Phase 1 output (agent instructions)
│   ├── root_agent.txt
│   ├── sub_agent_1.txt
│   └── sub_agent_2.txt
└── tasks.md             # Phase 2 output (/speckit.tasks command)
```

**Note on prompts**:
- `specs/.../prompts/*.txt` are planning artifacts for this feature.
- Runtime agent instructions MUST live in code as `prompt.py` modules (see below).

### ADK Agent Code Structure

<!--
  ACTION REQUIRED: Define the ADK agent project structure.
  Follow ADK conventions for agent organization.
-->

```text
# Canonical ADK agent layout (mirrors google/adk-samples travel-concierge)
#
# IMPORTANT:
# - The Python package lives at the REPO ROOT (not under agents/).
# - Use snake_case for agent package names (e.g., travel_concierge).
#
[agent_package_name]/
├── __init__.py
├── agent.py                     # Root agent entrypoint (defines root_agent)
├── prompt.py                    # Root agent instruction strings/constants
├── tracing.py                   # Optional observability helpers
├── shared_libraries/            # Optional shared helpers (if needed)
├── tools/                       # Custom tools (FunctionTool implementations)
│   ├── __init__.py
│   └── [tool_name].py
└── sub_agents/                  # Sub-agents (multi-agent systems)
    ├── __init__.py
    └── [sub_agent_name]/
        ├── __init__.py
        ├── agent.py             # Sub-agent definition (exports <name>_agent)
        ├── prompt.py            # Sub-agent instruction strings/constants
        └── tools/               # Optional sub-agent specific tools
            ├── __init__.py
            └── [tool_name].py

# Repo-level folders (optional but common, as in travel-concierge)
tests/
eval/
deployment/
```

**Structure Decision**: [Document the selected structure and any deviations from standard]

## Agent Architecture Design

### For LlmAgent (Single Agent)

```python
# High-level structure
root_agent = LlmAgent(
    name="[agent_name]",
    model="[model_name]",
    description="[agent_description]",
    instruction="[agent_instruction]",
    tools=[tool1, tool2, ...],
    output_key="[output_key]",  # If saving to state
    # Optional: callbacks, code_executor, planner, etc.
)
```

**Instruction Strategy**: [How will agent instructions be structured? Static vs dynamic?]
**Tool Selection**: [How does agent decide which tools to use?]

### For SequentialAgent (Pipeline)

```python
# High-level structure
root_agent = SequentialAgent(
    name="[pipeline_name]",
    sub_agents=[
        agent_1,  # Phase 1
        agent_2,  # Phase 2
        agent_3,  # Phase 3
    ]
)
```

**Pipeline Flow**: [Describe the sequential flow and state passing]
**Checkpoints**: [Where can pipeline be paused/resumed?]

### For ParallelAgent (Concurrent Execution)

```python
# High-level structure
root_agent = ParallelAgent(
    name="[parallel_name]",
    sub_agents=[
        agent_a,  # Independent task A
        agent_b,  # Independent task B
        agent_c,  # Independent task C
    ]
)
```

**Parallelization Strategy**: [Why are these tasks independent?]
**Result Aggregation**: [How are parallel results combined?]

### For Multi-Agent System (Complex Orchestration)

```
Root Orchestrator ([Type])
    ├── Sub-Agent 1 ([Type]) - [Responsibility]
    │   ├── Tool A
    │   └── Tool B
    ├── Sub-Agent 2 ([Type]) - [Responsibility]
    │   └── Tool C
    └── Sub-Agent 3 ([Type]) - [Responsibility]
        ├── Tool D
        └── Tool E
```

**Orchestration Pattern**: [Hub-and-spoke | Hierarchical | Map-reduce | Custom]
**Communication**: [How do agents communicate? State? AgentTool?]
**Error Propagation**: [How are errors handled across agents?]

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., 5+ sub-agents] | [current need] | [why fewer agents insufficient] |
| [e.g., Custom orchestration] | [specific problem] | [why standard patterns insufficient] |

## Phase 0: Research & Discovery

**Goal**: Resolve all NEEDS CLARIFICATION items and research ADK implementation approaches

### Research Tasks

1. **Model Selection Research**
   - Compare Gemini models (flash vs pro) for this use case
   - Evaluate cost vs performance trade-offs
   - Test model capabilities with sample prompts

2. **Tool Implementation Research**
   - Research existing ADK tools that could be reused
   - Evaluate OpenAPI tool generation for external APIs
   - Research MCP tool integration if needed

3. **Architecture Pattern Research**
   - Research similar ADK agent implementations
   - Evaluate orchestration patterns for this use case
   - Research state management best practices

4. **Deployment Strategy Research**
   - Evaluate deployment targets (local, Agent Engine, Cloud Run)
   - Research session management options
   - Evaluate observability tools

**Output**: `research.md` with all decisions documented

## Phase 1: Agent Design & Implementation

**Prerequisites**: `research.md` complete, all NEEDS CLARIFICATION resolved

### 1. Agent Architecture Document

Create `agent-architecture.md` with:
- Detailed agent hierarchy (if multi-agent)
- State flow diagrams
- Tool call sequences
- Error handling strategies
- Session management approach

### 2. Tool Specifications

Create `tool-specifications.md` with:
- Each tool's function signature
- Input/output schemas
- Error handling approach
- Confirmation requirements
- Test scenarios

### 3. Prompt Engineering

Create prompts in `prompts/` directory:
- `root_agent.txt`: Main agent instruction
- `[sub_agent].txt`: Sub-agent instructions (if applicable)
- Include:
  - Agent persona and role
  - Task description
  - Tool usage guidelines
  - Output format requirements
  - Error handling instructions

### 4. Agent Context Update

Run `.specify/scripts/bash/update-agent-context.sh gemini` to update:
- Agent-specific context file
- Add ADK version and dependencies
- Add agent architecture patterns
- Preserve manual additions between markers

**Output**: `agent-architecture.md`, `tool-specifications.md`, `prompts/`, updated agent context

## Phase 2: Task Breakdown

**Prerequisites**: Phase 1 complete

**Command**: `/speckit.tasks` will generate `tasks.md` with:
- Setup tasks (project initialization)
- Foundational tasks (shared infrastructure)
- Scenario-based implementation tasks (one phase per scenario from spec.md)
- Testing tasks (agent evaluation)
- Deployment tasks

**Output**: `tasks.md` ready for implementation

## Key Implementation Principles

### ADK Best Practices

1. **Single Responsibility**: Each agent does one thing well
2. **Clear Instructions**: Agent instructions are specific and actionable
3. **Tool Documentation**: Every tool has a clear docstring for the LLM
4. **State Management**: Use unique, descriptive state keys
5. **Error Handling**: Handle tool failures gracefully
6. **Testing**: Test agents independently before integration
7. **Observability**: Enable tracing for debugging

### Anti-Patterns to Avoid

- ❌ Mega-agents that try to do everything
- ❌ Vague or ambiguous instructions
- ❌ Reusing state keys across agents
- ❌ Tools without documentation
- ❌ Ignoring tool failures
- ❌ Sequential execution for independent tasks
- ❌ Skipping agent evaluation

### Performance Optimization

- Use ParallelAgent for independent tasks
- Cache static instructions with `static_instruction`
- Minimize state - only store what's needed
- Use `output_schema` for structured output
- Batch tool calls when possible
- Reuse Runner across requests

## Dependencies & Prerequisites

### External Dependencies

- Python 3.10+
- google-adk package
- Model access (Gemini via Vertex AI or API)
- Google Cloud Project (if using Vertex AI)
- Additional packages: [List any other required packages]

### Environment Setup

Required environment variables:
```bash
GOOGLE_API_KEY=<your-api-key>  # If using API
# OR
GOOGLE_GENAI_USE_VERTEXAI=true  # If using Vertex AI
GOOGLE_CLOUD_PROJECT=<project-id>
GOOGLE_CLOUD_LOCATION=<location>
```

### Development Tools

- `adk` CLI for local testing
- `pytest` for testing
- `uv` or `pip` for dependency management
- Optional: Docker for containerization

## Success Criteria

This implementation plan is complete when:

- [ ] All NEEDS CLARIFICATION items resolved
- [ ] Agent architecture fully documented
- [ ] All tools specified with clear interfaces
- [ ] Prompts written and tested
- [ ] Tasks.md generated and ready for implementation
- [ ] Constitution check passes
- [ ] Team understands the agent design and can begin implementation
