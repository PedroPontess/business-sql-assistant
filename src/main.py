from dotenv import load_dotenv

from agent import build_agent
from database import get_db_connection


def main():
    load_dotenv()

    print("🚀 Starting Chinook Music Store AI Agent...")

    try:
        db = get_db_connection()
        agent_executor = build_agent(db)
    except Exception as e:
        print(f"❌ Critical Initialization Error: {e}")
        return

    print("\n🎵 Chinook Music Store AI Agent (Powered by Llama 3.3 & Groq)")
    print("---------------------------------------------------------")
    print("Example queries:")
    print("1. 'Which are the top 3 countries by sales?'")
    print("2. 'How much has the band AC/DC sold in total?'")
    print("3. 'Which Sales Support Agent managed the highest sales?'")
    print("---------------------------------------------------------\n")

    while True:
        try:
            query = input("You> ").strip()

            if query.lower() in ["exit", "quit"]:
                print("👋 Shutting down...")
                break

            if not query:
                continue

            response = agent_executor.invoke(query)
            print(f"\n🤖 AI: {response['output']}\n")

        except KeyboardInterrupt:
            print("\n👋 Forced exit.")
            break
        except Exception as e:
            print(f"❌ Execution Error: {e}")


if __name__ == "__main__":
    main()
