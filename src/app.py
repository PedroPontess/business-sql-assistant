import streamlit as st
from dotenv import load_dotenv

from agent import build_agent
from database import get_db_connection

st.set_page_config(page_title="Chinook AI Assistant", page_icon="🎵", layout="centered")


def initialize_session_state():
    """
    Initializes the session state for chat history.
    """
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "Hello! I am your SQL Data Assistant. Ask me about sales, customers, or tracks!",
            }
        ]


@st.cache_resource
def get_agent():
    """
    Initializes the DB and Agent.
    Cached to prevent reloading the LLM/DB connection on every interaction.
    """
    load_dotenv()
    try:
        db = get_db_connection()
        return build_agent(db)
    except Exception as e:
        st.error(f"Failed to initialize agent: {e}")
        return None


def main():
    st.title("🎵 Chinook Music Store AI")

    agent = get_agent()
    if not agent:
        st.stop()

    initialize_session_state()

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ask a question (e.g., 'Top selling artists?')..."):
        with st.chat_message("user"):
            st.markdown(prompt)

        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    response = agent.invoke(prompt)
                    output_text = response["output"]
                    st.markdown(output_text)

                    st.session_state.messages.append(
                        {"role": "assistant", "content": output_text}
                    )

                except Exception as e:
                    st.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
