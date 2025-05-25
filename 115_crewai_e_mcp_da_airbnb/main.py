# pip install crewai "crewai-tools[mcp]"

from crewai import Agent, Task, Crew
from crewai_tools import MCPServerAdapter
from mcp import StdioServerParameters
import os

os.environ["OPENAI_API_KEY"] = "SUA_CHAVE_API_OPENAI"  # Sua chave da API OpenAI

# Configuração dos parâmetros do servidor MCP
server_params = StdioServerParameters(
    command="npx",
    args=["-y", "@openbnb/mcp-server-airbnb", "--ignore-robots-txt"],
)

# Iniciando o adaptador do servidor MCP
with MCPServerAdapter(server_params) as tools:
    # Criando um agente para interagir com o Airbnb
    agent = Agent(
        role="Especialista em Busca do Airbnb",
        goal="Buscar e analisar informações de acomodações no Airbnb",
        backstory="Um especialista em encontrar as melhores opções de acomodações no Airbnb",
        tools=tools,
        verbose=True,
    )

    # Criando uma tarefa para o agente
    task = Task(
        description="Buscar informações de acomodações no Airbnb no "
                    "capão dedondo com preço máximo de 100 reais por noite",
        expected_output="Lista de acomodações disponíveis com detalhes",
        agent=agent,
    )

    # Criando e executando a equipe
    crew = Crew(
        agents=[agent],
        tasks=[task],
        verbose=True,
    )

    # Executando a tarefa e imprimindo o resultado
    result = crew.kickoff()
    print(result)
