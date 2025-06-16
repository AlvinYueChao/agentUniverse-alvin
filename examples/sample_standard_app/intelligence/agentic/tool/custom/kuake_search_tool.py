# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Time    :
# @Author  :
# @Email   :
# @FileName: kuake_search_tool.py
from typing import Optional, Dict, Any

import requests
from langchain_core.pydantic_v1 import BaseModel, Field as LangChainField
from pydantic import Field

from agentuniverse.agent.action.tool.tool import Tool
from agentuniverse.base.util.env_util import get_from_env


class KuakeSerperAPIWrapper(BaseModel):
    """Wrapper for Kuake Search API.
    
    This class provides a simple interface to interact with Kuake Search API.
    It handles the API authentication and request formatting.
    """

    kuake_api_key: str = LangChainField(description="The API key for Kuake Search")
    kuake_app_id: str = LangChainField(description="The App ID for Kuake Search")
    base_url: str = LangChainField(
        default="https://dashscope.aliyuncs.com/api/v1/apps/{app_id}/completion",
        description="The base URL for Kuake Search API"
    )

    def run(self, query: str) -> Dict[str, Any]:
        """Execute the search query.
        
        Args:
            query (str): The search query to be processed.
            
        Returns:
            Dict[str, Any]: The search results from Kuake API.
        """
        response = requests.post(
            self.base_url.format(app_id=self.kuake_app_id),
            json={
                "input": {
                    "prompt": query
                },
                "parameters": {},
                "debug": {}
            },
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {self.kuake_api_key}'
            }
        )
        
        if response.status_code != 200:
            return {}
            
        return response.json()


class KuakeSearchTool(Tool):
    """The Kuake search tool.

    Implement the execute method of Kuake search tool, using the KuakeSerperAPIWrapper to perform search operations.

    Note:
        You need to have a valid Kuake API key and App ID from Alibaba Cloud.
        Set them in your environment variables as KUAKE_API_KEY and KUAKE_APP_ID.
    """

    kuake_api_key: Optional[str] = Field(default_factory=lambda: get_from_env("KUAKE_API_KEY"))
    kuake_app_id: Optional[str] = Field(default_factory=lambda: get_from_env("KUAKE_APP_ID"))

    def execute(self, input: str) -> Dict[str, Any]:
        """Execute the Kuake search with the given input.

        Args:
            input (str): The search query to be processed.

        Returns:
            Dict[str, Any]: The search results from Kuake API.
        """
        search_api = KuakeSerperAPIWrapper(
            kuake_api_key=self.kuake_api_key,
            kuake_app_id=self.kuake_app_id
        )
        return search_api.run(query=input)
