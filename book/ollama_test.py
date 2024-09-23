import time # 시간 측정
import langchain
from langchain_ollama import ChatOllama

from langchain_core.globals import set_llm_cache
from langchain_core.caches import InMemoryCache

set_llm_cache(InMemoryCache())

llm = ChatOllama(
    model="gemma2:2b",
    temperature=0.5
    # other params...
)

print(llm.invoke("세종대왕 맥북사건 알아?"))