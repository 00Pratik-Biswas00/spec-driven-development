# ADK Agent Development Constitution

## Core Principles

### I. Single Responsibility Principle

**Every agent must have one clear, well-defined purpose.**

- Each agent (LlmAgent, SequentialAgent, ParallelAgent, LoopAgent) must focus on a single responsibility
- Agents must be independently testable and deployable
- Clear purpose required - no organizational-only agents
- Sub-agents in multi-agent systems must have distinct, non-overlapping responsibilities

**Rationale**: Single-responsibility agents are easier to understand, test, debug, and maintain. They enable better composition and reusability.

### II. Tool Documentation Mandate

**Every tool must have a clear, descriptive docstring that the LLM can understand.**

- Tool docstrings are the primary way LLMs understand tool capabilities
- Docstrings must describe: purpose, parameters, return values, and when to use the tool
- Tools without documentation will not be called correctly
- Include examples in docstrings for complex tools

**Rationale**: LLMs rely on tool docstrings to decide when and how to call tools. Poor documentation leads to incorrect tool usage and agent failures.

### III. State Management Discipline

**State keys must be unique, descriptive, and well-documented.**

- Use descriptive state keys (e.g., `user_preferences`, `analysis_results` not `data`, `result`)
- Never reuse state keys across different agents or purposes
- Document what each state key contains in the agent specification
- Use `output_key` to explicitly save agent results to state
- Access state in instructions using `{key_name}` syntax

**Rationale**: Clear state management prevents bugs, makes agent behavior predictable, and enables effective debugging.

### IV. Test-First Development (Recommended)

**Write evaluation tests before implementing agent behavior.**

- Define expected agent responses and behavior criteria first
- Use ADK's AgentEvaluator for systematic testing
- Test each scenario independently before integration
- Include edge cases and error handling in tests

**Rationale**: Test-first development ensures agents meet requirements and behave predictably. It catches issues early and documents expected behavior.

### V. Observability & Debugging

**All agents must be observable and debuggable.**

- Enable OpenTelemetry tracing for development
- Log all tool calls and their results
- Use structured logging for important decisions
- Configure appropriate observability for deployment (BigQuery Analytics, AgentOps)
- Include error context in logs

**Rationale**: Observability is critical for debugging agent behavior, understanding tool usage, and monitoring production performance.

### VI. Performance & Efficiency

**Optimize for cost and latency without sacrificing quality.**

- Use ParallelAgent for independent tasks (not SequentialAgent)
- Cache static instructions with `static_instruction` parameter
- Minimize state - only store what's needed
- Use `output_schema` for structured output when appropriate
- Choose appropriate model (flash vs pro) based on task complexity
- Batch tool calls when possible

**Rationale**: Agent costs scale with tokens and API calls. Efficient design reduces costs and improves user experience.

### VII. Error Handling & Graceful Degradation

**Agents must handle errors gracefully and provide helpful responses.**

- Tools must catch exceptions and return error messages (not raise exceptions)
- Agents must handle tool failures without crashing
- Provide helpful error messages to users
- Include fallback strategies for critical operations
- Test error scenarios explicitly

**Rationale**: Production agents will encounter errors. Graceful handling ensures good user experience and system reliability.

## Agent Architecture Guidelines

### Agent Type Selection

**Choose the right agent type for the task:**

- **LlmAgent**: For intelligent reasoning, dynamic tool selection, and conversational interactions
- **SequentialAgent**: For pipelines where tasks must execute in order with state passing
- **ParallelAgent**: For independent tasks that can run concurrently
- **LoopAgent**: For iterative refinement with termination conditions
- **Multi-Agent System**: For complex tasks requiring specialized sub-agents

**Anti-Pattern**: Using SequentialAgent when tasks are independent (use ParallelAgent instead)

### Multi-Agent System Design

**Multi-agent systems** are applications where different agents collaborate or coordinate to achieve larger goals through composition of multiple `BaseAgent` instances.

#### ADK Primitives for Agent Composition

**1. Agent Hierarchy (Parent-Child Relationships)**

- Create tree structures by passing agent instances to `sub_agents` parameter
- Framework automatically sets `parent_agent` attribute on each child
- **Single Parent Rule**: An agent instance can only be added as a sub-agent once
- Navigate hierarchy using `agent.parent_agent` or `agent.find_agent(name)`

**2. Workflow Agents as Orchestrators**

Specialized agents that manage execution flow of their sub-agents:

- **SequentialAgent**: Executes sub-agents one after another in order
  - Passes the _same_ InvocationContext sequentially
  - Ideal for pipelines where output of one step feeds into the next
  - State changes persist across steps

- **ParallelAgent**: Executes sub-agents concurrently
  - Modifies `InvocationContext.branch` for each child (e.g., `ParentBranch.ChildName`)
  - All parallel children access the _same shared_ `session.state`
  - Use distinct state keys to avoid race conditions
  - Events from sub-agents may be interleaved

- **LoopAgent**: Executes sub-agents sequentially in a loop
  - Stops when `max_iterations` is reached
  - Stops when any sub-agent returns Event with `escalate=True` in EventActions
  - Passes the _same_ InvocationContext in each iteration
  - State changes persist across loop iterations

**3. Interaction & Communication Mechanisms**

**a) Shared Session State (`session.state`)**
- Most fundamental communication method for agents in same invocation
- One agent writes: `context.state['data_key'] = processed_data`
- Another agent reads: `data = context.state.get('data_key')`
- Use `output_key` property on LlmAgent to automatically save results to state
- Access state in instructions using `{key_name}` syntax
- Asynchronous, passive communication ideal for pipelines
- Temporary state (`temp:`) is shared within same InvocationContext

**b) LLM-Driven Delegation (Agent Transfer)**
- Leverages LLmAgent's understanding to dynamically route tasks
- LLM generates: `transfer_to_agent(agent_name='target_agent_name')`
- AutoFlow intercepts and routes execution to target agent
- Requires clear `instructions` on when to transfer
- Target agents need distinct `descriptions` for LLM decision-making
- Transfer scope (parent, sub-agent, siblings) is configurable
- Dynamic, flexible routing based on LLM interpretation

**c) Explicit Invocation (AgentTool)**
- Treat another BaseAgent instance as a callable function/tool
- Wrap target agent in `AgentTool` and include in parent's `tools` list
- When parent LLM calls the AgentTool, framework executes target agent
- Captures final response, forwards state/artifact changes back
- Returns response as tool result
- Synchronous, explicit, controlled invocation like any other tool

#### Common Multi-Agent Patterns

**1. Coordinator/Dispatcher Pattern**
- Central LlmAgent manages several specialized sub-agents
- Routes incoming requests to appropriate specialist
- Uses LLM-Driven Delegation or AgentTool for routing
- Requires clear descriptions on sub-agents

```
coordinator (LlmAgent)
├── billing_agent (specialist)
├── support_agent (specialist)
└── sales_agent (specialist)
```

**2. Sequential Pipeline Pattern**
- SequentialAgent with sub-agents in fixed order
- Multi-step process where output of one feeds into next
- Uses Shared Session State for data passing
- Earlier agents write results (via `output_key`)
- Later agents read from `context.state`

```
SequentialAgent
├── validator → state['validation_status']
├── processor → state['result']
└── reporter (reads state['result'])
```

**3. Parallel Fan-Out/Gather Pattern**
- ParallelAgent runs multiple sub-agents concurrently
- Often followed by aggregation agent in SequentialAgent
- Execute independent tasks simultaneously to reduce latency
- Sub-agents write to distinct state keys
- Gather agent reads multiple state keys

```
SequentialAgent
├── ParallelAgent (fan-out)
│   ├── fetch_api1 → state['api1_data']
│   └── fetch_api2 → state['api2_data']
└── synthesizer (gather - reads both state keys)
```

**4. Hierarchical Task Decomposition**
- Multi-level tree where higher-level agents break down complex goals
- Delegates sub-tasks to lower-level agents
- Uses LLM-Driven Delegation or AgentTool
- Results returned up the hierarchy

```
report_writer (high-level)
└── research_assistant (mid-level, as AgentTool)
    ├── web_searcher (low-level, as AgentTool)
    └── summarizer (low-level, as AgentTool)
```

**5. Review/Critique Pattern (Generator-Critic)**
- Two agents in SequentialAgent: Generator and Critic/Reviewer
- Improves quality/validity of generated output
- Generator uses `output_key` to save output
- Reviewer reads that state key and provides feedback
- Reviewer might save feedback to another state key

```
SequentialAgent
├── generator → state['draft_text']
└── reviewer (reads state['draft_text']) → state['review_status']
```

**6. Iterative Refinement Pattern**
- LoopAgent with agents that work on task over multiple iterations
- Progressively improve result stored in session state
- Terminates on `max_iterations` or quality threshold met
- Checking agent sets `escalate=True` when satisfactory

```
LoopAgent (max_iterations=5)
├── code_refiner → state['current_code']
├── quality_checker → state['quality_status']
└── stop_checker (escalates if state['quality_status'] == 'pass')
```

**7. Human-in-the-Loop Pattern**
- Integrates human intervention points within workflow
- Implemented using custom Tool that pauses execution
- Tool sends request to external system (UI, ticketing)
- Waits for human input and returns response to agent
- Can use LLM-Driven Delegation to conceptual "Human Agent"
- State holds task details; callbacks manage interaction flow

```
SequentialAgent
├── prepare_request → state['approval_amount'], state['approval_reason']
├── request_approval (calls external_approval_tool) → state['human_decision']
└── process_decision (reads state['human_decision'])
```

**8. Human-in-the-Loop with Policy**
- More structured approach using PolicyEngine
- SecurityPlugin intercepts tool calls and consults PolicyEngine
- PolicyEngine's `evaluate()` method decides if confirmation needed
- Returns `PolicyOutcome.CONFIRM` to pause execution
- Application presents confirmation request to user
- User confirmation sent as FunctionResponse to proceed

#### Multi-Agent Design Guidelines

**Architecture Selection:**
- Root orchestrator coordinates sub-agents
- Sub-agents are specialists with focused capabilities
- Each sub-agent should be independently testable
- Define clear interfaces between agents via state

**Communication Strategy:**
- Use Shared State for data passing in pipelines
- Use LLM-Driven Delegation for dynamic routing
- Use AgentTool for explicit, controlled invocation
- Use distinct state keys to avoid collisions

**Pattern Combination:**
- Mix and match patterns as needed
- Example: Coordinator + Sequential Pipeline + Parallel Fan-Out
- Example: Hierarchical Decomposition + Iterative Refinement
- Example: Sequential Pipeline + Review/Critique + Human-in-the-Loop

**Best Practices:**
- Start with simplest pattern that solves the problem
- Add complexity only when needed
- Test each agent independently before integration
- Document agent hierarchy and communication flows
- Monitor performance and optimize bottlenecks

### Tool Design Principles

**Tools should be:**

- **Focused**: One tool, one function
- **Documented**: Clear docstring for LLM
- **Typed**: Use type hints for parameters and returns
- **Tested**: Unit tests for each tool
- **Stateless** (when possible): Use ToolContext only when state is needed
- **Error-Handling**: Return error messages, don't raise exceptions

**Tool Confirmation**: Require confirmation for:
- Destructive operations (delete, modify)
- External actions (send email, post to API)
- Financial transactions
- Sensitive data access

## Development Workflow

### Phase 0: Specification

1. Define agent purpose and capabilities
2. Identify interaction scenarios (prioritized)
3. Specify required tools and sub-agents
4. Define success criteria and evaluation metrics

**Output**: `spec.md` with clear agent requirements

### Phase 1: Architecture & Design

1. Select appropriate agent architecture
2. Design tool interfaces and implementations
3. Write agent instructions (prompts)
4. Plan state management strategy
5. Document agent architecture

**Output**: `plan.md`, `agent-architecture.md`, `tool-specifications.md`, `prompts/`

### Phase 2: Implementation

1. Setup ADK project structure
2. Implement tools with tests
3. Implement agents (start with simplest scenario)
4. Test each scenario independently
5. Integrate scenarios incrementally

**Output**: Working agent code, tests, evaluation results

### Phase 3: Evaluation & Refinement

1. Run AgentEvaluator on all scenarios
2. Test with real users (if possible)
3. Refine instructions based on results
4. Optimize performance and cost
5. Document learnings

**Output**: Production-ready agent

### Phase 4: Deployment

1. Choose deployment target (local, Agent Engine, Cloud Run)
2. Configure observability
3. Setup CI/CD (if applicable)
4. Deploy and monitor
5. Iterate based on production feedback

**Output**: Deployed agent with monitoring

## Quality Gates

### Before Moving to Implementation

- [ ] Agent purpose is clear and focused
- [ ] All scenarios are independently testable
- [ ] Tool requirements are documented
- [ ] Success criteria are measurable
- [ ] Architecture is appropriate for the task

### Before Deployment

- [ ] All scenarios tested and passing
- [ ] Evaluation metrics meet success criteria
- [ ] Error handling tested
- [ ] Observability configured
- [ ] Documentation complete (README, .env.example)
- [ ] Dependencies locked (requirements.txt)

## Anti-Patterns to Avoid

### ❌ Mega-Agent Anti-Pattern

**Problem**: One agent trying to do everything

**Solution**: Break into specialized agents with clear responsibilities

### ❌ Vague Instructions Anti-Pattern

**Problem**: Instructions like "You are a helpful assistant"

**Solution**: Specific instructions with examples: "You analyze financial data and provide investment recommendations. When users ask about stocks, use the stock_analysis tool..."

### ❌ Undocumented Tools Anti-Pattern

**Problem**: Tools without docstrings or with generic descriptions

**Solution**: Clear, specific docstrings: "Searches the company database for employee records. Parameters: name (str) - employee name to search. Returns: dict with employee details or error message."

### ❌ State Collision Anti-Pattern

**Problem**: Multiple agents using the same state key like "result"

**Solution**: Unique, descriptive keys: "market_analysis_result", "risk_assessment_result"

### ❌ Sequential for Independent Tasks Anti-Pattern

**Problem**: Using SequentialAgent when tasks don't depend on each other

**Solution**: Use ParallelAgent for independent tasks to improve performance

### ❌ Ignoring Errors Anti-Pattern

**Problem**: Tools that raise exceptions or agents that crash on errors

**Solution**: Catch exceptions, return error messages, handle gracefully

### ❌ Wrong Workflow Agent Anti-Pattern

**Problem**: Using SequentialAgent when tasks are independent, or not using LoopAgent for iterative refinement

**Solution**: 
- Use ParallelAgent for independent concurrent tasks
- Use SequentialAgent only when order matters and state passes between steps
- Use LoopAgent for iterative refinement with termination conditions

### ❌ Unclear Agent Transfer Anti-Pattern

**Problem**: LLM-driven delegation without clear instructions or descriptions

**Solution**: 
- Provide specific instructions on when to transfer
- Give sub-agents distinct, descriptive `description` fields
- Test transfer scenarios explicitly

### ❌ State Key Collision in Parallel Agents Anti-Pattern

**Problem**: Parallel sub-agents writing to the same state key causing race conditions

**Solution**: Use distinct state keys for each parallel agent (e.g., `api1_data`, `api2_data`)

### ❌ Deep Hierarchy Anti-Pattern

**Problem**: Too many levels of agent nesting making system hard to understand and debug

**Solution**: Keep hierarchy shallow (2-3 levels max), use flat patterns when possible

### ❌ Missing Escalation Logic Anti-Pattern

**Problem**: LoopAgent without proper termination conditions running until max_iterations

**Solution**: Implement checking agent that sets `escalate=True` when quality threshold is met

## Governance

### Constitution Authority

This constitution is **non-negotiable** during agent development. Any violations must be:

1. Explicitly documented in the implementation plan
2. Justified with clear reasoning
3. Approved before proceeding
4. Tracked in the "Complexity Tracking" section

### Amendments

To amend this constitution:

1. Document the proposed change and rationale
2. Discuss with the team
3. Update this document
4. Communicate changes to all developers
5. Update templates and tools to reflect changes

### Compliance

All agent implementations must:

- Follow these principles
- Pass constitution checks in the planning phase
- Document any justified violations
- Be reviewed for compliance before deployment

### Continuous Improvement

This constitution should evolve based on:

- Lessons learned from agent development
- New ADK features and best practices
- Production experience and feedback
- Industry best practices

**Version**: 1.0.0  
**Ratified**: [DATE]  
**Last Amended**: [DATE]  
**Next Review**: [DATE + 6 months]

---

## Quick Reference

### ✅ DO

- Give agents single, clear responsibilities
- Document all tools with descriptive docstrings
- Use unique, descriptive state keys
- Write evaluation tests before implementation
- Enable observability and logging
- Use ParallelAgent for independent tasks
- Handle errors gracefully
- Test each scenario independently
- Choose appropriate models for tasks
- Cache static instructions
- Use workflow agents (Sequential, Parallel, Loop) for orchestration
- Provide clear descriptions for sub-agents in multi-agent systems
- Use `output_key` to explicitly save agent results to state
- Implement proper escalation logic in LoopAgent
- Keep agent hierarchy shallow (2-3 levels max)
- Use distinct state keys in ParallelAgent to avoid race conditions
- Test each agent independently before integration
- Document agent hierarchy and communication flows

### ❌ DON'T

- Create mega-agents that do everything
- Leave tools undocumented
- Reuse state keys across agents
- Skip testing
- Ignore observability
- Use SequentialAgent for independent tasks
- Let tools raise unhandled exceptions
- Skip error scenario testing
- Use expensive models for simple tasks
- Put dynamic content in static_instruction
- Use LLM-driven delegation without clear instructions
- Create deep agent hierarchies (>3 levels)
- Have parallel agents write to same state keys
- Use LoopAgent without proper termination conditions
- Add an agent instance as sub-agent to multiple parents
- Mix workflow patterns without clear reasoning

---

**Remember**: These principles exist to make agent development predictable, maintainable, and successful. When in doubt, refer back to these core principles.
