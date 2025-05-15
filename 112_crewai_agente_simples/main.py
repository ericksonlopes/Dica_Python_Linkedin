# pip install crewai langchain-openai

import os

from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI

os.environ['OPENAI_API_KEY'] = "SUA_CHAVE"

# Configura seu modelo LLM
llm = ChatOpenAI(model="gpt-4o", temperature=0)

# Cria o agente
pesquisador = Agent(
    role="Pesquisador de curiosidades",
    goal="Responder perguntas com base no conhecimento fornecido",
    backstory="É um especialista em responder perguntas com clareza.",
    llm=llm
)

# Define a tarefa
tarefa = Task(
    description="Responda: Por que o céu é azul?",
    expected_output="Uma explicação simples e científica de por que o céu é azul",
    agent=pesquisador
)

# Cria a equipe e roda
equipe = Crew(
    agents=[pesquisador],
    tasks=[tarefa],
    verbose=True  # Mostra os passos
)

resultado = equipe.kickoff()
print("\n✅ Resultado final:\n", resultado)
