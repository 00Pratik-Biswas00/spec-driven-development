# ADK Agent Specification: [AGENT/FEATURE NAME]

**Feature Branch**: `[###-feature-name]`  
**Created**: [DATE]  
**Status**: Draft  
**Agent Type**: [LlmAgent | SequentialAgent | ParallelAgent | LoopAgent | CustomAgent | Multi-Agent System]  
**Input**: User description: "$ARGUMENTS"

## Agent Purpose & Capabilities *(mandatory)*

**Primary Goal**: [What problem does this agent solve? What value does it deliver?]

**Agent Persona**: [Describe the agent's role, expertise, and interaction style]

**Key Capabilities**:
- [Capability 1: e.g., "Analyze market data and generate insights"]
- [Capability 2: e.g., "Orchestrate sub-agents for specialized tasks"]
- [Capability 3: e.g., "Maintain conversation context across sessions"]

## User Interaction Scenarios *(mandatory)*

<!--
  IMPORTANT: Agent scenarios should be PRIORITIZED as user interaction flows ordered by importance.
  Each scenario must be INDEPENDENTLY TESTABLE - meaning if you implement just ONE of them,
  you should still have a viable MVP agent that delivers value.
  
  Assign priorities (P1, P2, P3, etc.) to each scenario, where P1 is the most critical.
  Think of each scenario as a standalone capability that can be:
  - Developed independently
  - Tested independently (with mock tools/sub-agents if needed)
  - Deployed independently
  - Demonstrated to users independently
  
  For multi-agent systems, each scenario may involve multiple agents working together.
-->

### Scenario 1 - [Brief Title] (Priority: P1) 🎯 MVP

**User Interaction Flow**: [Describe the conversation/interaction flow in plain language]

**Example Conversation**:
```
User: [Example user input]
Agent: [Expected agent response/action]
User: [Follow-up input]
Agent: [Expected agent response/action]
```

**Why this priority**: [Explain the value and why it has this priority level]

**Independent Test**: [Describe how this can be tested independently - e.g., "Can be fully tested by providing [input] and verifying [output/behavior]"]

**Agent Behavior Requirements**:

1. **Given** [conversation state], **When** [user input], **Then** [agent should respond/act]
2. **Given** [conversation state], **When** [user input], **Then** [agent should respond/act]
3. **Given** [error condition], **When** [user input], **Then** [agent should handle gracefully]

**Required Tools/Capabilities**: [List tools or sub-agents needed for this scenario]

---

### Scenario 2 - [Brief Title] (Priority: P2)

**User Interaction Flow**: [Describe the conversation/interaction flow]

**Example Conversation**:
```
User: [Example user input]
Agent: [Expected agent response/action]
```

**Why this priority**: [Explain the value and why it has this priority level]

**Independent Test**: [Describe how this can be tested independently]

**Agent Behavior Requirements**:

1. **Given** [conversation state], **When** [user input], **Then** [agent should respond/act]

**Required Tools/Capabilities**: [List tools or sub-agents needed]

---

### Scenario 3 - [Brief Title] (Priority: P3)

**User Interaction Flow**: [Describe the conversation/interaction flow]

**Example Conversation**:
```
User: [Example user input]
Agent: [Expected agent response/action]
```

**Why this priority**: [Explain the value and why it has this priority level]

**Independent Test**: [Describe how this can be tested independently]

**Agent Behavior Requirements**:

1. **Given** [conversation state], **When** [user input], **Then** [agent should respond/act]

**Required Tools/Capabilities**: [List tools or sub-agents needed]

---

[Add more scenarios as needed, each with an assigned priority]

### Edge Cases & Error Handling

<!--
  ACTION REQUIRED: Define how the agent handles edge cases and errors.
  ADK agents should handle errors gracefully and provide helpful responses.
-->

- **Invalid Input**: How does agent handle malformed or unexpected user input?
- **Tool Failures**: How does agent respond when a tool call fails?
- **Ambiguous Requests**: How does agent clarify unclear user intentions?
- **Rate Limits**: How does agent handle API rate limits or quota exhaustion?
- **Session Timeout**: How does agent handle session expiration or context loss?
- **Concurrent Requests**: How does agent handle multiple simultaneous requests (if applicable)?

## Agent Requirements *(mandatory)*

<!--
  ACTION REQUIRED: Define the agent's functional requirements.
  Focus on WHAT the agent must do, not HOW it's implemented.
-->

### Functional Requirements

- **AR-001**: Agent MUST [specific capability, e.g., "understand and respond to natural language queries"]
- **AR-002**: Agent MUST [specific capability, e.g., "call appropriate tools based on user intent"]  
- **AR-003**: Agent MUST [key interaction, e.g., "maintain conversation context across multiple turns"]
- **AR-004**: Agent MUST [data requirement, e.g., "store and retrieve user preferences from state"]
- **AR-005**: Agent MUST [behavior, e.g., "log all tool calls and responses for observability"]

*Example of marking unclear requirements:*

- **AR-006**: Agent MUST authenticate tool calls via [NEEDS CLARIFICATION: auth method not specified - API keys, OAuth, service accounts?]
- **AR-007**: Agent MUST retain conversation history for [NEEDS CLARIFICATION: retention period not specified - session only, 30 days, indefinitely?]

### Tool Requirements *(if agent uses tools)*

List the tools this agent needs to accomplish its goals:

- **Tool 1**: [Tool name/purpose, e.g., "Google Search - for web research"]
  - Input: [What parameters does it need?]
  - Output: [What does it return?]
  - Confirmation Required: [Yes/No - does user need to approve before execution?]

- **Tool 2**: [Tool name/purpose, e.g., "Database Query - for retrieving user data"]
  - Input: [What parameters does it need?]
  - Output: [What does it return?]
  - Confirmation Required: [Yes/No]

### Sub-Agent Requirements *(if multi-agent system)*

For multi-agent architectures, define the sub-agents:

- **Sub-Agent 1**: [Name and role, e.g., "Data Analyst - analyzes market data"]
  - Responsibility: [What is this agent responsible for?]
  - Input: [What does it receive from parent/other agents?]
  - Output: [What does it produce?]
  - Tools: [What tools does it use?]

- **Sub-Agent 2**: [Name and role]
  - Responsibility: [What is this agent responsible for?]
  - Input: [What does it receive?]
  - Output: [What does it produce?]
  - Tools: [What tools does it use?]

### State & Memory Requirements

- **State Keys**: [What state variables does the agent need to track? e.g., "user_preferences", "conversation_context", "analysis_results"]
- **Session Management**: [Does agent need persistent sessions? How long?]
- **Memory Services**: [Does agent need RAG memory, Vertex AI memory, or other memory services?]

## Success Criteria *(mandatory)*

<!--
  ACTION REQUIRED: Define measurable success criteria for the agent.
  These should be technology-agnostic and focus on agent behavior and user outcomes.
-->

### Measurable Outcomes

- **SC-001**: [Agent response quality, e.g., "Agent provides relevant responses to 95% of user queries"]
- **SC-002**: [Agent performance, e.g., "Agent responds within 3 seconds for 90% of interactions"]
- **SC-003**: [Tool usage accuracy, e.g., "Agent selects correct tool for task 90% of the time"]
- **SC-004**: [User satisfaction, e.g., "Users successfully complete their goal in 80% of conversations"]
- **SC-005**: [Error handling, e.g., "Agent gracefully handles and recovers from 100% of tool failures"]
- **SC-006**: [Multi-turn conversations, e.g., "Agent maintains context across 95% of multi-turn conversations"]

### Agent Quality Metrics

- **Accuracy**: [How accurate should the agent's responses be?]
- **Relevance**: [How relevant should tool calls and responses be to user intent?]
- **Completeness**: [Should agent provide comprehensive answers or concise summaries?]
- **Consistency**: [Should agent maintain consistent persona and behavior?]
- **Safety**: [What safety guardrails must the agent respect?]

### Performance Benchmarks

- **Response Latency**: [Target response time, e.g., "< 2 seconds for simple queries, < 10 seconds for complex analysis"]
- **Throughput**: [If applicable, e.g., "Handle 100 concurrent conversations"]
- **Token Efficiency**: [If cost is a concern, e.g., "Average conversation uses < 10K tokens"]
- **Tool Call Efficiency**: [e.g., "Minimize unnecessary tool calls, average 2-3 per conversation"]
