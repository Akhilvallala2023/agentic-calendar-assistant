import os
import datetime
from dotenv import load_dotenv
from openai import OpenAI
from agents import Agent, Runner
from calendar_tools import (
    create_calendar_event,
    list_upcoming_events,
    delete_event,
    reschedule_event,
    reschedule_event_by_title,
    delete_event_by_title
)

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
    "Delete my meeting with Sarah"
    "Move meeting with Sam to tomorrow at 6pm"
    "Cancel my lunch appointment"
    "Reschedule my doctor appointment to next week"
- Extract event details: summary, start_datetime, duration, event_id
- Use tools to create, delete, reschedule, or list calendar events
- For rescheduling/deleting: Try to find events by title first, then by ID if needed
- Confirm actions with friendly replies

If no duration is provided, default to 60 minutes.
Always use ISO format for start_datetime. Default timezone: America/New_York.
""",
    tools=[
        create_calendar_event,
        list_upcoming_events,
        delete_event,
        reschedule_event,
        reschedule_event_by_title,
        delete_event_by_title
    ]
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
