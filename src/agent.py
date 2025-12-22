import os

from langchain_community.agent_toolkits import create_sql_agent
from langchain_community.utilities import SQLDatabase
from langchain_groq import ChatGroq

SYSTEM_MESSAGE = """ 
You are an expert in SQL and Data Analysis. You are working with the 'Chinook' database, which represents a digital music store. 
Key tables: 
- Album, Artist, Customer, Employee, Genre, Invoice, InvoiceLine, MediaType, Playlist, PlaylistTrack, Track

Rules: 
1. Never invent tables or columns. Always verify the schema first. 
2. For sales totals, use the 'Invoice' table. 
3. For questions involving money or revenue, the relevant field is usually 'Total' in the Invoice table. 
4. Do not generate DELETE or UPDATE queries under any circumstances. 
"""


def build_agent(db: SQLDatabase):
    """
    Constructs the SQL Agent using Llama 3.3 and Groq.

    Args:
        db (SQLDatabase): The active database connection wrapper.

    Returns:
        AgentExecutor: The executable LangChain agent ready to process queries.

    Raises:
        EnvironmentError: If GROQ_API_KEY is missing.
    """
    if not os.getenv("GROQ_API_KEY"):
        raise EnvironmentError("GROQ_API_KEY not found in environment variables.")

    llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)

    return create_sql_agent(
        llm=llm,
        db=db,
        agent_type="openai-tools",
        prefix=SYSTEM_MESSAGE,
        verbose=False,
        # handle_parsing_errors is crucial: if the LLM generates malformed SQL,
        # this allows the agent to see the error and correct itself in the next step.
        agent_executor_kwargs={"handle_parsing_errors": True},
    )
