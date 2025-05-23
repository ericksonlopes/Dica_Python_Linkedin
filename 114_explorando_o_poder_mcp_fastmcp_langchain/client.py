import os
import subprocess

from langchain.agents import initialize_agent, AgentType
from langchain.chat_models import ChatOpenAI
from langchain.tools import Tool

os.environ["OPENAI_API_KEY"] = ""


# Define a função para chamar o servidor MCP
def chamar_mcp_ferramenta(input_str: str) -> str:
    """Chama o servidor MCP via subprocess e envia input_str"""
    process = subprocess.Popen(
        ['python', 'server.py'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout, stderr = process.communicate(input_str)
    return stdout.strip()


# Defina suas ferramentas como objetos Tool do LangChain
tools = [
    Tool(
        name="Somar",
        func=lambda x: chamar_mcp_ferramenta(f"somar {x}"),
        description="Soma dois números inteiros. Exemplo: '8 10'"
    )
]

# Inicializa o agente
llm = ChatOpenAI(temperature=0)  # LLM da OpenAI (necessário OPENAI_API_KEY no env)
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Teste
if __name__ == "__main__":
    pergunta = input("Qual soma deseja fazer?: ")
    resposta = agent.run(pergunta)
    print("\n🤖 Resposta:", resposta)
