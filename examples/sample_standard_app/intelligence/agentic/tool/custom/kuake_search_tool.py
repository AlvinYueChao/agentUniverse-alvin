# !/usr/bin/env python3
# -*- coding:utf-8 -*-
import json
# @Time    :
# @Author  :
# @Email   :
# @FileName: kuake_search_tool.py
from typing import Optional

from agentuniverse.agent.action.tool.tool import Tool, ToolInput
from agentuniverse.base.util.env_util import get_from_env
from pydantic import Field
import requests

class KuakeSearchTool(Tool):

    kuake_api_key: Optional[str] = Field(default_factory=lambda: get_from_env("KUAKE_API_KEY"))
    kuake_app_id: Optional[str] = Field(default_factory=lambda: get_from_env("KUAKE_APP_ID"))

    def execute(self, input: str):
        res = requests.post(f'https://dashscope.aliyuncs.com/api/v1/apps/{self.kuake_app_id}/completion',
                     data=json.dumps({
                        "input": {
                            "prompt": input
                        },
                        "parameters": {},
                        "debug": {}
                    }),
        headers={'Content-Type': 'application/json','Authorization': f'Bearer {self.kuake_api_key}'})
        if res.status_code != 200:
            return ''
        return res.json()
