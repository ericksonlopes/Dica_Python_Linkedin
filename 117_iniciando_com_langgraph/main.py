# pip install langgraph "langchain[openai]"
import os
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage
from langgraph.constants import START, END
from langgraph.graph import StateGraph
from langgraph.graph.message import add_messages
from typing import Annotated
from typing_extensions import TypedDict

# Define a chave da API do OpenAI
os.environ["OPENAI_API_KEY"] = "sk-..."


# Define o tipo de estado para o gráfico de estados
class State(TypedDict):
    messages: Annotated[list, add_messages]


# Cria um construtor de gráfico de estados
graph_builder = StateGraph(State)

# Inicializa o modelo de chat com o OpenAI GPT-4
llm = init_chat_model("openai:gpt-4o")


# Função do chatbot que invoca o modelo com as mensagens do estado
def chatbot(state: State):
    return {"messages": [llm.invoke(state["messages"])]}


# Adiciona as arestas e nós ao gráfico
graph_builder.add_edge(START, "chatbot")
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge("chatbot", END)

# Compila o fluxo de trabalho
workflow = graph_builder.compile()

# Pergunta para o chatbot
ask = "Olá, tudo bem?"
resultado = workflow.invoke({"messages": [HumanMessage(content=ask)]})

# Imprime a resposta do chatbot
print(resultado["messages"][-1].content)
