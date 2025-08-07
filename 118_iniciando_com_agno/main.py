import os
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from textwrap import dedent

# Definindo a chave da API do OpenAI
os.environ["OPENAI_API_KEY"] = "sua chave_api_openai"

# Criando um agente com instruções personalizadas
agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    instructions=dedent("""\
        Você é um programador Python experiente com um toque de humor! 🐍
        Pense em você como um mestre da codificação que adora compartilhar conhecimento de forma divertida e
        envolvente.
    """),
    markdown=True,
)

# Executando o agente para obter uma explicação sobre Python
response = agent.run("Explique resumidamente o que é python").content

# Imprimindo a resposta formatada
print(response)

# Exemplo de resposta esperada
"""
Python é uma linguagem de programação de alto nível, interpretada e de propósito geral.
Ela é conhecida por sua sintaxe clara e legível, o que a torna ideal para
iniciantes e especialistas. Python suporta múltiplos paradigmas de programação,
incluindo programação orientada a objetos, funcional e imperativa.
"""
