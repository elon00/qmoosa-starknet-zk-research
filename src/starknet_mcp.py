"""
Starknet Model Context Protocol (MCP) Router & Agentic Execution Engine.
Dynamically routes AI tool calls to Starknet RPC and Cairo Smart Contracts.
"""

import os
import json
import urllib.request

DEFAULT_RPC_URL = "https://api.cartridge.gg/x/starknet/sepolia"

class StarknetMCPRouter:
    def __init__(self):
        self.rpc_url = os.getenv("STARKNET_RPC_URL", DEFAULT_RPC_URL)
        self.model_name = os.getenv("MODEL_NAME", "default")
        self.active_provider = self._detect_llm_provider()

    def _detect_llm_provider(self) -> str:
        if os.getenv("GEMINI_API_KEY"):
            return "GOOGLE_GEMINI"
        elif os.getenv("ANTHROPIC_API_KEY"):
            return "ANTHROPIC_CLAUDE"
        elif os.getenv("OPENAI_API_KEY"):
            return "OPENAI_GPT"
        return "LOCAL_SIMULATION_MODE"

    def execute_rpc(self, method: str, params: list = None) -> dict:
        """Executes a JSON-RPC tool-call over Starknet RPC."""
        payload = {
            "jsonrpc": "2.0",
            "method": method,
            "params": params or [],
            "id": 1
        }
        req = urllib.request.Request(
            self.rpc_url,
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json", "User-Agent": "StarknetMCP/1.0"}
        )
        try:
            with urllib.request.urlopen(req, timeout=5) as response:
                return json.loads(response.read().decode("utf-8"))
        except Exception as e:
            return {"error": str(e), "rpc_url": self.rpc_url}

    def get_server_metadata(self) -> dict:
        """Exposes standard MCP server tool declarations for AI agents."""
        return {
            "name": "Starknet-MCP-Router",
            "version": "1.0.0",
            "provider": self.active_provider,
            "rpc_endpoint": self.rpc_url,
            "tools": [
                {"name": "starknet_blockNumber", "description": "Fetches the latest Starknet block height."},
                {"name": "starknet_chainId", "description": "Returns the active chain ID (SN_SEPOLIA)."},
                {"name": "cairo_query_research", "description": "Queries research data from ResearchRegistry Cairo contract."}
            ]
        }
