---

description: "Task list template for ADK agent implementation"
---

# ADK Agent Tasks: [AGENT/FEATURE NAME]

**Input**: Design documents from `/specs/[###-feature-name]/`
**Prerequisites**: plan.md (required), spec.md (required for scenarios), agent-architecture.md, tool-specifications.md, prompts/

**Tests**: Agent evaluation tasks are OPTIONAL - only include them if explicitly requested in the specification.

**Organization**: Tasks are grouped by interaction scenario to enable independent implementation and testing of each capability.

## Format: `[ID] [P?] [Scenario] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Scenario]**: Which interaction scenario this task belongs to (e.g., S1, S2, S3)
- Include exact file paths in descriptions
- Follow ADK project structure conventions

## ADK Project Structure

```text
[agent_package_name]/
├── agent.py                     # Main agent definition
├── prompt.py                    # Agent instructions (code module)
├── tools/                       # Custom tools
│   └── [tool_name].py
├── sub_agents/                  # Sub-agents (if multi-agent)
│   └── [sub_agent_name]/
├── callbacks/                   # Callbacks (optional)
├── deployment/                  # Deployment scripts
├── tests/                       # Tests
└── eval/                        # Evaluation (optional)
```

<!-- 
  ============================================================================
  IMPORTANT: The tasks below are SAMPLE TASKS for illustration purposes only.
  
  The /speckit.tasks command MUST replace these with actual tasks based on:
  - Interaction scenarios from spec.md (with their priorities P1, P2, P3...)
  - Agent architecture from plan.md
  - Tool specifications from tool-specifications.md
  - Prompts from prompts/ directory
  
  Tasks MUST be organized by scenario so each capability can be:
  - Implemented independently
  - Tested independently (with mock tools/sub-agents if needed)
  - Delivered as an MVP increment
  
  DO NOT keep these sample tasks in the generated tasks.md file.
  ============================================================================
-->

## Phase 1: Project Setup & Infrastructure

**Purpose**: Initialize ADK agent project and basic structure

- [ ] T001 Create ADK agent project structure per implementation plan
- [ ] T002 Initialize Python project with ADK dependencies (requirements.txt or pyproject.toml)
- [ ] T003 [P] Create .env.example with required environment variables
- [ ] T004 [P] Setup linting and formatting tools (black, flake8, mypy)
- [ ] T005 [P] Create README.md with agent description and setup instructions

---

## Phase 2: Foundational Components (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY scenario can be implemented

**⚠️ CRITICAL**: No scenario work can begin until this phase is complete

### Configuration & Setup

- [ ] T006 Create config.py with model configuration and environment setup
- [ ] T007 [P] Setup logging and observability (OpenTelemetry, BigQuery Analytics, or AgentOps)
- [ ] T008 [P] Create prompt.py with base prompt templates

### State Management

- [ ] T009 Define state keys and state management strategy in agent.py
- [ ] T010 [P] Setup session management (if needed)
- [ ] T011 [P] Configure memory services (if needed - Vertex AI RAG, etc.)

### Tool Infrastructure (if tools needed)

- [ ] T012 Create tools/__init__.py
- [ ] T013 [P] Implement base tool utilities (error handling, logging)
- [ ] T014 [P] Setup tool confirmation mechanism (if required)

### Testing Infrastructure

- [ ] T015 Create tests/__init__.py and test fixtures
- [ ] T016 [P] Setup pytest configuration
- [ ] T017 [P] Create test utilities and mock tools

**Checkpoint**: Foundation ready - scenario implementation can now begin in parallel

---

## Phase 3: Scenario 1 - [Title] (Priority: P1) 🎯 MVP

**Goal**: [Brief description of what this scenario delivers]

**Independent Test**: [How to verify this scenario works on its own]

### Agent Evaluation for Scenario 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these evaluation tests FIRST, ensure they FAIL before implementation**

- [ ] T018 [P] [S1] Create evaluation test for scenario 1 in eval/test_scenario_1.py
- [ ] T019 [P] [S1] Define expected responses and behavior criteria
- [ ] T020 [P] [S1] Create test fixtures for scenario 1 inputs

### Tools for Scenario 1

- [ ] T021 [P] [S1] Implement [Tool1] in tools/[tool1].py with docstring
- [ ] T022 [P] [S1] Implement [Tool2] in tools/[tool2].py with docstring
- [ ] T023 [P] [S1] Add tool tests in tests/test_tools.py
- [ ] T024 [S1] Register tools in tools/__init__.py

### Agent Implementation for Scenario 1

**For LlmAgent (Single Agent)**:
- [ ] T025 [S1] Write agent instruction in prompt.py for scenario 1
- [ ] T026 [S1] Create root_agent in agent.py with model, instruction, and tools
- [ ] T027 [S1] Configure output_key for state management (if needed)
- [ ] T028 [S1] Add callbacks for logging/monitoring (if needed)

**For Multi-Agent System**:
- [ ] T025 [S1] Create sub-agent directory structure for scenario 1
- [ ] T026 [P] [S1] Implement sub-agent 1 in sub_agents/[name]/agent.py
- [ ] T027 [P] [S1] Implement sub-agent 2 in sub_agents/[name]/agent.py
- [ ] T028 [S1] Write orchestrator agent in agent.py
- [ ] T029 [S1] Configure AgentTool wrappers for sub-agents
- [ ] T030 [S1] Setup state flow between agents

### Testing & Validation for Scenario 1

- [ ] T031 [S1] Create integration test in tests/test_agent.py
- [ ] T032 [S1] Test scenario 1 conversation flow with adk run
- [ ] T033 [S1] Verify tool calls and responses
- [ ] T034 [S1] Test error handling and edge cases
- [ ] T035 [S1] Validate state management

**Checkpoint**: At this point, Scenario 1 should be fully functional and testable independently

---

## Phase 4: Scenario 2 - [Title] (Priority: P2)

**Goal**: [Brief description of what this scenario delivers]

**Independent Test**: [How to verify this scenario works on its own]

### Agent Evaluation for Scenario 2 (OPTIONAL - only if tests requested) ⚠️

- [ ] T036 [P] [S2] Create evaluation test for scenario 2 in eval/test_scenario_2.py
- [ ] T037 [P] [S2] Define expected responses and behavior criteria

### Tools for Scenario 2

- [ ] T038 [P] [S2] Implement [Tool] in tools/[tool].py with docstring
- [ ] T039 [S2] Add tool tests in tests/test_tools.py

### Agent Implementation for Scenario 2

- [ ] T040 [S2] Write agent instruction for scenario 2 in prompt.py
- [ ] T041 [S2] Update agent.py to handle scenario 2 (add tools, update instruction)
- [ ] T042 [S2] Configure state management for scenario 2
- [ ] T043 [S2] Integrate with Scenario 1 components (if needed)

### Testing & Validation for Scenario 2

- [ ] T044 [S2] Create integration test for scenario 2
- [ ] T045 [S2] Test scenario 2 conversation flow
- [ ] T046 [S2] Verify independent functionality

**Checkpoint**: At this point, Scenarios 1 AND 2 should both work independently

---

## Phase 5: Scenario 3 - [Title] (Priority: P3)

**Goal**: [Brief description of what this scenario delivers]

**Independent Test**: [How to verify this scenario works on its own]

### Agent Evaluation for Scenario 3 (OPTIONAL - only if tests requested) ⚠️

- [ ] T047 [P] [S3] Create evaluation test for scenario 3 in eval/test_scenario_3.py

### Tools for Scenario 3

- [ ] T048 [P] [S3] Implement [Tool] in tools/[tool].py with docstring

### Agent Implementation for Scenario 3

- [ ] T049 [S3] Write agent instruction for scenario 3 in prompt.py
- [ ] T050 [S3] Update agent.py to handle scenario 3
- [ ] T051 [S3] Configure state management for scenario 3

### Testing & Validation for Scenario 3

- [ ] T052 [S3] Create integration test for scenario 3
- [ ] T053 [S3] Test scenario 3 conversation flow

**Checkpoint**: All scenarios should now be independently functional

---

[Add more scenario phases as needed, following the same pattern]

---

## Phase N: Polish, Optimization & Deployment

**Purpose**: Improvements that affect multiple scenarios and deployment readiness

### Code Quality & Documentation

- [ ] TXXX [P] Update README.md with usage examples for all scenarios
- [ ] TXXX [P] Add docstrings to all functions and classes
- [ ] TXXX Code cleanup and refactoring
- [ ] TXXX [P] Update prompt.py with refined instructions

### Performance & Optimization

- [ ] TXXX Optimize agent instructions for token efficiency
- [ ] TXXX Review and optimize tool calls
- [ ] TXXX Add context caching for static instructions (if applicable)
- [ ] TXXX Performance testing across all scenarios

### Observability & Monitoring

- [ ] TXXX [P] Configure OpenTelemetry tracing
- [ ] TXXX [P] Setup BigQuery Analytics (if using)
- [ ] TXXX [P] Configure AgentOps integration (if using)
- [ ] TXXX Add logging for all tool calls and agent decisions

### Deployment Preparation

- [ ] TXXX Create deployment/deploy.py for Vertex AI Agent Engine
- [ ] TXXX Create deployment/test_deployment.py for deployment testing
- [ ] TXXX [P] Create Dockerfile (if deploying to Cloud Run)
- [ ] TXXX [P] Setup CI/CD pipeline (if needed)
- [ ] TXXX Test deployment to target environment

### Security & Guardrails

- [ ] TXXX [P] Implement authentication for tools (if needed)
- [ ] TXXX [P] Add rate limiting (if needed)
- [ ] TXXX [P] Setup tool confirmation for sensitive operations
- [ ] TXXX [P] Add content safety filters (if needed)

### Additional Testing

- [ ] TXXX [P] Run AgentEvaluator across all scenarios
- [ ] TXXX [P] Load testing (if applicable)
- [ ] TXXX [P] Security testing
- [ ] TXXX End-to-end testing with real users

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all scenarios
- **Scenarios (Phase 3+)**: All depend on Foundational phase completion
  - Scenarios can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired scenarios being complete

### Scenario Dependencies

- **Scenario 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other scenarios
- **Scenario 2 (P2)**: Can start after Foundational (Phase 2) - May reuse tools from S1 but should be independently testable
- **Scenario 3 (P3)**: Can start after Foundational (Phase 2) - May reuse tools from S1/S2 but should be independently testable

### Within Each Scenario

- Evaluation tests (if included) MUST be written and FAIL before implementation
- Tools before agent implementation
- Agent instruction before agent creation
- Core implementation before integration
- Scenario complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all scenarios can start in parallel (if team capacity allows)
- All evaluation tests for a scenario marked [P] can run in parallel
- Tools within a scenario marked [P] can run in parallel
- Different scenarios can be worked on in parallel by different team members

---

## Parallel Example: Scenario 1

```bash
# Launch all evaluation tests for Scenario 1 together (if tests requested):
Task: "Create evaluation test for scenario 1 in eval/test_scenario_1.py"
Task: "Define expected responses and behavior criteria"

# Launch all tools for Scenario 1 together:
Task: "Implement [Tool1] in tools/[tool1].py with docstring"
Task: "Implement [Tool2] in tools/[tool2].py with docstring"
Task: "Add tool tests in tests/test_tools.py"
```

---

## Implementation Strategy

### MVP First (Scenario 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all scenarios)
3. Complete Phase 3: Scenario 1
4. **STOP and VALIDATE**: Test Scenario 1 independently with `adk run`
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add Scenario 1 → Test independently → Deploy/Demo (MVP!)
3. Add Scenario 2 → Test independently → Deploy/Demo
4. Add Scenario 3 → Test independently → Deploy/Demo
5. Each scenario adds capability without breaking previous scenarios

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: Scenario 1 (tools + agent)
   - Developer B: Scenario 2 (tools + agent)
   - Developer C: Scenario 3 (tools + agent)
3. Scenarios complete and integrate independently

---

## ADK-Specific Testing Approach

### Local Testing with ADK CLI

```bash
# Test agent interactively
adk run [agent_name]

# Test with web interface
adk web

# Run pytest tests
pytest tests/

# Run evaluation
pytest eval/
```

### Agent Evaluation Strategy

Use ADK's `AgentEvaluator` for systematic testing:

```python
from google.adk.evaluation import AgentEvaluator

evaluator = AgentEvaluator(agent=root_agent)
results = evaluator.evaluate(test_cases)
```

### Testing Checklist

- [ ] Unit tests for all tools
- [ ] Integration tests for agent behavior
- [ ] Evaluation tests for conversation quality
- [ ] Edge case testing
- [ ] Error handling testing
- [ ] State management testing
- [ ] Multi-turn conversation testing

---

## Deployment Checklist

### Pre-Deployment

- [ ] All scenarios tested and working
- [ ] Environment variables documented in .env.example
- [ ] README.md updated with setup and usage instructions
- [ ] Dependencies locked in requirements.txt or pyproject.toml
- [ ] Observability configured

### Deployment Options

**Option 1: Local Development**
```bash
adk run [agent_name]
adk web
```

**Option 2: Vertex AI Agent Engine**
```bash
python deployment/deploy.py --create
python deployment/test_deployment.py --resource_id=<id>
```

**Option 3: Cloud Run**
```bash
docker build -t [agent_name] .
gcloud run deploy [agent_name] --image [agent_name]
```

### Post-Deployment

- [ ] Verify agent responds correctly
- [ ] Monitor logs and traces
- [ ] Test all scenarios in production
- [ ] Setup alerts for errors
- [ ] Document deployment process

---

## Notes

- [P] tasks = different files, no dependencies
- [Scenario] label maps task to specific interaction scenario for traceability
- Each scenario should be independently completable and testable
- Verify evaluation tests fail before implementing
- Test with `adk run` after each scenario
- Commit after each task or logical group
- Stop at any checkpoint to validate scenario independently
- Follow ADK best practices: single responsibility, clear instructions, tool documentation
- Avoid: mega-agents, vague instructions, undocumented tools, reusing state keys
