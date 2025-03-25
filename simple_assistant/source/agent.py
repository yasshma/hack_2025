"""Этот модуль определяет основную логику агента, включая процесс рассуждения и использование инструментов."""
import os
from rich.console import Console
import base64
from rich.panel import Panel
from rich.table import Table
from langchain_gigachat.chat_models import GigaChat
from langchain_core.messages import HumanMessage, AIMessage
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver

from source.prompts import agent_class, agent_sum_up  # Импортируем наш системный промпт
from source.utils import check_urgency

from dotenv import load_dotenv

import os
import base64

load_dotenv('./simple_assistant/config/.env')

client_id = os.getenv('CLIENT_ID')
secret = os.getenv('SECRET')
auth = os.getenv('AUTH')


credentials = f"{client_id}:{secret}"
encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

model = GigaChat(credentials=encoded_credentials,
                scope='GIGACHAT_API_PERS',
                verify_ssl_certs=False,
                auth_url="https://ngw.devices.sberbank.ru:9443/api/v2/oauth",
                # model='GigaChat',
                model='GigaChat-Max',
                streaming=False,
                profanity_check=True,
                #timeoutError=99999,
                top_p=0.1,
                temperature=0.01,
               )

agent1 = create_react_agent(
    model=model,
    tools=[],
    state_modifier=agent_class,  # Подключаем системный контекст
    checkpointer=MemorySaver()  # Добавляем объект из библиотеки LangGraph для сохранения памяти агента
)


agent2 = create_react_agent(
    model=model,
    tools=[],
    state_modifier=agent_sum_up,  # Подключаем системный контекст
    checkpointer=MemorySaver()  # Добавляем объект из библиотеки LangGraph для сохранения памяти агента
)
