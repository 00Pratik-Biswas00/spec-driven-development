# ADK Agent Development Context

Auto-generated from all agent plans. Last updated: [DATE]

## Active ADK Technologies

[EXTRACTED FROM ALL PLAN.MD FILES]

### ADK Version & Dependencies

- **ADK Version**: [e.g., google-adk 1.0.0]
- **Python Version**: [e.g., Python 3.10+]
- **Primary Models**: [e.g., gemini-2.5-flash, gemini-2.5-pro]

### Agent Architectures in Use

- **LlmAgent**: [List agents using LlmAgent]
- **SequentialAgent**: [List agents using SequentialAgent]
- **ParallelAgent**: [List agents using ParallelAgent]
- **LoopAgent**: [List agents using LoopAgent]
- **Multi-Agent Systems**: [List complex multi-agent systems]

## ADK Project Structure

```text
[ACTUAL STRUCTURE FROM PLANS]

Standard ADK Structure:
[agent_name]/
├── agent.py                     # Main agent definition (root_agent)
├── prompt.py                    # Agent instructions (code module)
├── config.py                    # Configuration (optional)
├── tools/                       # Custom tools
│   └── [tool_name].py
├── sub_agents/                  # Sub-agents (if multi-agent)
│   └── [sub_agent_name]/
├── callbacks/                   # Callbacks (optional)
├── deployment/                  # Deployment scripts
├── tests/                       # Tests
├── eval/                        # Evaluation (optional)
└── README.md                    # Agent documentation
```

## Common ADK Commands

### Development Commands

```bash
# Create new agent project
adk create [agent_name]

# Run agent interactively (CLI)
adk run [agent_name]

# Run agent with web interface
adk web [agent_name]
adk web --port 8000

# Run tests
pytest tests/
pytest eval/

# Run specific test
pytest tests/test_agent.py -v
```

### Deployment Commands

```bash
# Deploy to Vertex AI Agent Engine
python deployment/deploy.py --create

# List deployed agents
python deployment/deploy.py --list

# Test deployed agent
python deployment/test_deployment.py --resource_id=<id> --user_id=<user>

# Delete deployed agent
python deployment/deploy.py --delete --resource_id=<id>
```

### Environment Setup

```bash
# Set up for API access
export GOOGLE_API_KEY='your-api-key-here'

# Set up for Vertex AI access
export GOOGLE_GENAI_USE_VERTEXAI=true
export GOOGLE_CLOUD_PROJECT='your-project-id'
export GOOGLE_CLOUD_LOCATION='us-central1'

# Authenticate with Google Cloud
gcloud auth application-default login
gcloud auth application-default set-quota-project $GOOGLE_CLOUD_PROJECT
```

## ADK Code Patterns

### LlmAgent Pattern

```python
from google.adk.agents import LlmAgent
from google.adk.tools import FunctionTool

# Define tools
def my_tool(param: str) -> dict:
    """Clear description for the LLM"""
    return {"result": param}

# Create agent
root_agent = LlmAgent(
    name="agent_name",
    model="gemini-2.5-flash",
    description="Agent description for tool selection",
    instruction="You are a helpful assistant...",
    tools=[FunctionTool(func=my_tool)],
    output_key="result"  # Save to state
)
```

### SequentialAgent Pattern

```python
from google.adk.agents import LlmAgent, SequentialAgent

# Create sub-agents
agent_1 = LlmAgent(name="step1", output_key="step1_result", ...)
agent_2 = LlmAgent(name="step2", instruction="Process {step1_result}", ...)

# Create pipeline
root_agent = SequentialAgent(
    name="pipeline",
    sub_agents=[agent_1, agent_2]
)
```

### ParallelAgent Pattern

```python
from google.adk.agents import LlmAgent, ParallelAgent

# Create independent agents
agent_a = LlmAgent(name="task_a", output_key="result_a", ...)
agent_b = LlmAgent(name="task_b", output_key="result_b", ...)

# Create parallel executor
root_agent = ParallelAgent(
    name="parallel",
    sub_agents=[agent_a, agent_b]
)
```

### Multi-Agent System Pattern

```python
from google.adk.agents import LlmAgent, SequentialAgent
from google.adk.tools import AgentTool

# Create specialized sub-agents
sub_agent_1 = LlmAgent(name="specialist_1", ...)
sub_agent_2 = LlmAgent(name="specialist_2", ...)

# Create orchestrator with sub-agents as tools
root_agent = LlmAgent(
    name="orchestrator",
    model="gemini-2.5-pro",
    instruction="Coordinate sub-agents to solve complex tasks",
    tools=[
        AgentTool(agent=sub_agent_1),
        AgentTool(agent=sub_agent_2)
    ]
)
```

### Tool Creation Pattern

```python
from google.adk.tools import FunctionTool, ToolContext

# Simple function tool
def simple_tool(param: str) -> dict:
    """Tool description for LLM - be specific!"""
    return {"result": f"Processed: {param}"}

# Tool with context (state access)
def stateful_tool(param: str, tool_context: ToolContext) -> dict:
    """Tool with state access"""
    # Read state
    previous = tool_context.state.get("key", "default")
    
    # Write state
    tool_context.state["key"] = "new_value"
    
    return {"result": param, "previous": previous}

# Tool with confirmation
tool_with_confirm = FunctionTool(
    func=dangerous_operation,
    require_confirmation=True
)
```

### State Management Pattern

```python
# Agent saves to state
agent_a = LlmAgent(
    name="agent_a",
    output_key="data"  # Saves output to state["data"]
)

# Agent reads from state
agent_b = LlmAgent(
    name="agent_b",
    instruction="Process {data}"  # Reads state["data"]
)

# Access state in tools
def my_tool(tool_context: ToolContext) -> dict:
    value = tool_context.state.get("data")
    tool_context.state["processed"] = True
    return {"status": "success"}
```

## ADK Best Practices

### Agent Design

✅ **DO**:
- Give each agent a single, clear responsibility
- Write specific, actionable instructions
- Use descriptive agent names
- Document agent purpose in description field
- Test agents independently before integration

❌ **DON'T**:
- Create mega-agents that do everything
- Use vague or ambiguous instructions
- Give agents overlapping responsibilities
- Skip agent descriptions

### Tool Development

✅ **DO**:
- Write clear docstrings for every tool (LLM reads these!)
- Use type hints for parameters and return values
- Handle errors gracefully and return helpful messages
- Log tool calls for debugging
- Use ToolContext for state access

❌ **DON'T**:
- Create tools without documentation
- Ignore errors or let exceptions propagate
- Use tools for side effects without returning results
- Forget to test tools independently

### State Management

✅ **DO**:
- Use unique, descriptive state keys
- Document what each state key contains
- Use output_key to save agent results to state
- Reference state variables in instructions with {key}

❌ **DON'T**:
- Reuse state keys across different agents
- Use generic keys like "result" or "data"
- Forget to initialize state keys
- Assume state keys exist without checking

### Performance

✅ **DO**:
- Use ParallelAgent for independent tasks
- Cache static instructions with static_instruction
- Minimize state - only store what's needed
- Use output_schema for structured output
- Reuse Runner across requests

❌ **DON'T**:
- Use SequentialAgent for independent tasks
- Put dynamic content in static_instruction
- Store large objects in state
- Create new Runner for each request

### Testing

✅ **DO**:
- Write unit tests for all tools
- Test agent behavior with pytest
- Use AgentEvaluator for conversation quality
- Test error handling and edge cases
- Test with `adk run` during development

❌ **DON'T**:
- Skip testing tools independently
- Only test happy paths
- Forget to test multi-turn conversations
- Skip evaluation tests

## Recent Agent Changes

[LAST 3 AGENTS AND WHAT THEY ADDED]

## Common Tool Integrations

### Google Search

```python
from google.adk.tools import google_search

agent = LlmAgent(
    tools=[google_search],
    ...
)
```

### Vertex AI Search

```python
from google.adk.tools import VertexAiSearchTool

search_tool = VertexAiSearchTool(
    data_store_id="my-datastore"
)
```

### BigQuery

```python
from google.adk.tools.bigquery import BigQueryToolset

bq_toolset = BigQueryToolset(
    project_id="my-project",
    dataset_id="my-dataset"
)
```

### OpenAPI Tools

```python
from google.adk.tools.openapi_tool import OpenApiToolset

api_toolset = OpenApiToolset(
    spec_url="https://api.example.com/openapi.json",
    auth_config={"type": "bearer", "token": "..."}
)
```

## Observability Setup

### OpenTelemetry Tracing

```python
# Automatic tracing enabled by default
# View traces in console during development
```

### BigQuery Analytics

```python
from google.adk.observability import BigQueryAnalyticsPlugin

plugin = BigQueryAnalyticsPlugin(
    project_id="my-project",
    dataset_id="agent_analytics"
)
```

### AgentOps Integration

```python
# Configure in environment
export AGENTOPS_API_KEY='your-key'
```

## Deployment Patterns

### Local Development

```python
# agent.py defines root_agent
# Run with: adk run [agent_name]
# Or: adk web [agent_name]
```

### Vertex AI Agent Engine

```python
# deployment/deploy.py
from vertexai.preview import reasoning_engines

agent = reasoning_engines.ReasoningEngine.create(
    agent_module="[agent_name].agent",
    requirements=["google-adk"],
    ...
)
```

### Cloud Run

```dockerfile
# Dockerfile
FROM python:3.10
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "server.py"]
```

## Environment Variables Reference

```bash
# API Access
GOOGLE_API_KEY=<your-api-key>

# Vertex AI Access
GOOGLE_GENAI_USE_VERTEXAI=true
GOOGLE_CLOUD_PROJECT=<project-id>
GOOGLE_CLOUD_LOCATION=<location>

# Optional: Storage for deployment
GOOGLE_CLOUD_STORAGE_BUCKET=<bucket-name>

# Optional: Observability
AGENTOPS_API_KEY=<agentops-key>
```

## Troubleshooting

### Common Issues

**Agent not responding**:
- Check model configuration
- Verify API key or Vertex AI access
- Check agent instructions are clear
- Review tool docstrings

**Tools not being called**:
- Verify tool docstrings are descriptive
- Check tool is registered in agent.tools
- Review agent instructions mention tool usage
- Test tool independently

**State not persisting**:
- Verify output_key is set
- Check state key names are unique
- Ensure ToolContext is used in tools
- Review state flow between agents

**Deployment failures**:
- Check all dependencies in requirements.txt
- Verify environment variables are set
- Test locally with `adk run` first
- Review deployment logs

## Resources

- **ADK Documentation**: https://google.github.io/adk-docs/
- **ADK Python GitHub**: https://github.com/google/adk-python
- **ADK Samples**: https://github.com/google/adk-samples
- **PyPI Package**: https://pypi.org/project/google-adk/

<!-- MANUAL ADDITIONS START -->
<!-- Add project-specific patterns, conventions, and notes here -->
<!-- These will be preserved during updates -->
<!-- MANUAL ADDITIONS END -->
