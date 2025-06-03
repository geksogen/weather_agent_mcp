import gradio as gr
from smolagents import CodeAgent
from smolagents.mcp_client import MCPClient
from smolagents import LiteLLMModel

mcp_client = MCPClient(
    ## Try this working example on the hub:
    {"url": "http://mcp_server:8000/sse"}

    )
tools = mcp_client.get_tools()

model = LiteLLMModel(model_id="ollama/qwen2.5:7b", api_base="http://81.94.150.136:11434")
agent = CodeAgent(tools=[*tools], model=model)

demo = gr.ChatInterface(
    fn=lambda message, history: str(agent.run(message)),
    type="messages",
    examples=["what is the weather like in Moscow now?"],
    title="Agent with MCP Tools",
    description="This is a simple agent that uses MCP tools to answer questions.",
)
demo.launch()