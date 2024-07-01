import os

from langchain_community.chat_models import QianfanChatEndpoint
from langchain_core.tracers import ConsoleCallbackHandler


os.environ['LANGCHAIN_TRACING_V2']="true"
os.environ['LANGCHAIN_PROJECT']="learn_langchain"


# 免费等模型 ERNIE-Speed-128K ERNIE-Speed-8K ERNIE Speed-AppBuilder ERNIE-Lite-8K
# ERNIE-Lite-8K-0922 ERNIE-Lite-AppBuilder-8K ERNIE-Tiny-8K Yi-34B-Chat
BAIDU_LLM = QianfanChatEndpoint(
    model="ERNIE-Speed-8K"
)
BAIDU_LLM.invoke("你是谁", config={"callbacks": [ConsoleCallbackHandler()]})
