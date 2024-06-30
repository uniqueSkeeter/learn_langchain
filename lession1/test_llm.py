import os

from langchain_community.chat_models import QianfanChatEndpoint
from langchain_core.tracers import ConsoleCallbackHandler

BAIDU_LLM = QianfanChatEndpoint(
    model="ERNIE-Lite-8K"
)
BAIDU_LLM.invoke("你是谁",config = {"callbacks": [ConsoleCallbackHandler()]})