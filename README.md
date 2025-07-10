# 🤖 OpenAI Agents SDK Calendar Assistant

A **fully agentic** calendar assistant built with the **OpenAI Agents SDK** that transforms natural language into Google Calendar events.

## 🎯 What Makes This Truly Agentic

✅ **OpenAI Agents SDK** - Built with the official framework  
✅ **@function_tool** decorators - Clean, modern tool integration  
✅ **Agent() declaration** - Proper agent architecture  
✅ **Runner.run()** execution - Agentic orchestration  
✅ **Natural Language Processing** - Understands conversational requests  

## 🚀 Quick Start

```bash
# Always activate venv first!
source venv/bin/activate && python simple_calendar_agent.py
```

## 💬 Example Usage

```
🧑 You: Book a meeting with John tomorrow at 3pm
🤖: Your meeting with John has been booked for tomorrow at 3 PM. 
    You can view or edit the event [here](https://calendar.google.com/...)
```

## 🏗️ Agentic Architecture

```python
# Modern @function_tool decorators
@function_tool
def create_calendar_event(summary: str, start_datetime: str, ...):
    """Create a calendar event."""
    # Google Calendar API integration
    
# Agent declaration with tools
agent = Agent(
    name="SimpleCalendarAgent",
    instructions="You are a calendar assistant...",
    tools=[create_calendar_event, list_upcoming_events]
)

# Agentic execution
response = await Runner.run(agent, [{"role": "user", "content": user_input}])
```

## 📁 Project Structure

```
📦 Scheduling/
├── 🤖 simple_calendar_agent.py     # Main agent with OpenAI Agents SDK
├── 🔧 calendar_tools.py            # @function_tool decorated tools
├── 📦 requirements.txt             # Dependencies with openai-agents
├── 🔐 .env                         # OpenAI API key
├── 🗝️ credentials.json             # Google OAuth credentials
├── 🎫 token.json                   # Google auth token
└── 📜 run_calendar.sh              # Easy run script
```

## 🛠️ Agentic Features

- 🧠 **Natural Language Understanding** - "Book lunch with Sarah next Friday"
- 🤖 **Agent-Based Architecture** - OpenAI Agents SDK integration
- 🔧 **Modern Tool Framework** - @function_tool decorators
- 📅 **Google Calendar Integration** - Real calendar events
- 🕐 **Smart Date Parsing** - Handles relative dates
- ⚡ **Instant Booking** - Events appear immediately

## 📝 How It Works

1. **User Input**: "Book a meeting with Michael tomorrow at 5pm"
2. **Agent Processing**: OpenAI Agents SDK parses the request
3. **Tool Execution**: @function_tool creates the calendar event
4. **Response**: Agent confirms with Google Calendar link

## 🔧 Technical Stack

- **OpenAI Agents SDK** - Official agentic framework
- **Google Calendar API** - Real calendar integration
- **@function_tool** - Modern tool declarations
- **Agent/Runner** - Agentic execution pattern

## ⚠️ Important

**Always activate the virtual environment:**
```bash
source venv/bin/activate && python simple_calendar_agent.py
```

---

**Ready for agentic calendar management?** 🚀 Your AI assistant is powered by the OpenAI Agents SDK! 