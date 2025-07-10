import os
import datetime
from dotenv import load_dotenv
from openai import OpenAI
from agents import Agent, Runner
from calendar_tools import create_calendar_event, list_upcoming_events

# Load environment variables
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Get today's date for context
now = datetime.datetime.now()
today_str = now.strftime("%A, %B %d, %Y")
tomorrow_str = (now + datetime.timedelta(days=1)).strftime('%Y-%m-%dT17:00:00')

# Define the agent
agent = Agent(
    name="SimpleCalendarAgent",
    instructions=f"""
You are a helpful calendar assistant. Today's date is {today_str}.

Your job is to:
- Understand natural language requests like:
    "Book a meeting with Michael tomorrow at 5pm for 1 hour"
    "Schedule lunch next Friday at 1pm"
- Extract event details: summary, start_datetime, duration
- Use tools to create or list calendar events
- Confirm with friendly replies

Examples:
- "tomorrow at 5pm" = {tomorrow_str}
- "next Friday at 1pm" = (calculate next Friday from today, set 13:00)
- "today at 3pm" = use {now.strftime('%Y-%m-%d')}T15:00:00

If no duration is provided, default to 60 minutes.
Always use ISO format for start_datetime. Default timezone: America/New_York.
""",
    tools=[create_calendar_event, list_upcoming_events]
)

async def run_agent():
    print("📅 Calendar Assistant (Agent SDK Version)")
    print("Type your scheduling request (or 'exit' to quit).")
    while True:
        user_input = input("🧑 You: ").strip()
        if user_input.lower() in {"exit", "quit"}:
            print("👋 Goodbye!")
            break
        response = await Runner.run(agent, [{"role": "user", "content": user_input}])
        print("🤖:", response.final_output)

# To run from script
if __name__ == "__main__":
    import asyncio
    asyncio.run(run_agent())
