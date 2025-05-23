import os
import asyncio
import logfire
logfire.configure()
logfire.instrument_pydantic_ai()
from dotenv import load_dotenv
from pydantic_ai import Agent, RunContext
from dataclasses import dataclass
from pydantic import BaseModel, Field
from pydantic_ai.mcp import MCPServerHTTP, MCPServerStdio
from utils import llm_models
load_dotenv()

mcp_server = MCPServerHTTP(url=os.getenv('MCP_SERVER_URL'))


# """You are an expert in creating architecture diagram from a code base.
#     Your task is to:
#     1. Use the available tool in the MCP server to parse code from the provided directory path.
#     2. Analyze the parsed code returned by the tool to create a architecture diagram based on C4 models
#
#     Return a script so that user can create the diagram in Mermaid"""
ingest_code_agent = Agent(
    llm_models.openrouter_model,
    output_type=str,
    system_prompt="""You are an expert in creating architecture diagram from a code base.
    Your task is to:
    1. Use the available tool in the MCP server to parse code from the provided directory path.
    2. Analyze the parsed code to create a concise documentation.

    Return the documentation""",
    mcp_servers=[mcp_server]
)

async def main(path: str = 'res_code'):
    async with ingest_code_agent.run_mcp_servers():
        #result = await agent.run('How many days between 2000-01-01 and 2025-03-18?')
        result = await ingest_code_agent.run(f"directory_path={path} and language=java")

    print(result.output)
    return result.output