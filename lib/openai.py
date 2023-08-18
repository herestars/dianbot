import os
import requests
import json
import openai
import config

openai.api_key = config.OPENAI_API_KEY
openai.api_base = config.OPENAI_ENDPOINT
openai.api_type = "azure"
openai.api_version = "2023-05-15"  # this may change in the future


class ChatMessage:
    role: str
    content: str


def send_to_openai(messages: list[dict[str, str]]) -> str:
    response = openai.ChatCompletion.create(
        engine=config.OPENAI_DEPLOYMENT_NAME,
        messages=messages,
    )
    return response['choices'][0]['message']['content']

async def send_to_openai_async(messages: list[dict[str, str]]) -> str:
    response = await openai.ChatCompletion.acreate(
        engine=config.OPENAI_DEPLOYMENT_NAME,
        messages=messages,
    )
    return response['choices'][0]['message']['content']