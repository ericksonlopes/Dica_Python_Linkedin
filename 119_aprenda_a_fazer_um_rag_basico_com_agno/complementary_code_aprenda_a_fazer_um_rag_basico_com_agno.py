# pip install agno openai lancedb pandas pypdf
import os

from agno.agent import Agent
from agno.embedder.openai import OpenAIEmbedder
from agno.knowledge.pdf import PDFKnowledgeBase
from agno.models.openai import OpenAIChat
from agno.vectordb.lancedb import LanceDb

os.environ["OPENAI_API_KEY"] = "sua chave_api_openai"

knowledge_base = PDFKnowledgeBase(
    path="sample_data/livro_da_minha_vida.pdf",
    vector_db=LanceDb(
        table_name="content",
        uri="tmp/lancedb",
        embedder=OpenAIEmbedder(id="text-embedding-3-small")
    ),
)

# Carrega o conteúdo do PDF na base de conhecimento
knowledge_base.load()

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    knowledge=knowledge_base,
    add_references=True,
    search_knowledge=False,
    markdown=True
)

agent.print_response(
    "Qual é o dia do meu nascimento?", stream=True
)
