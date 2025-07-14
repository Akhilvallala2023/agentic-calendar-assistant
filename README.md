# 🤖 AI Calendar Assistant with Google Meet Integration

A **fully agentic** calendar assistant built with the **OpenAI Agents SDK** that transforms natural language into Google Calendar events with **automatic Google Meet links**.

## ✨ Key Features

🧠 **Smart Natural Language Processing** - "Book lunch with Sarah next Friday at 1pm"  
🤖 **OpenAI Agents SDK** - Built with the official agentic framework  
📧 **Automatic Attendee Invitations** - Just mention an email and they're invited  
🔗 **Google Meet Links** - Auto-generated for meetings with attendees  
📅 **Google Calendar Integration** - Real events in your calendar  
⏰ **Smart Date/Time Parsing** - Handles "tomorrow", "next week", etc.  
🗑️ **Event Management** - Create, list, delete, and reschedule events  

## 🚀 Quick Start

```bash
# Clone and setup
git clone <your-repo>
cd Scheduling

# Always activate venv first!
source venv/bin/activate && python simple_calendar_agent.py
```

## 💬 Example Usage

### Simple Event Creation
```
🧑 You: Book gym session tomorrow at 6pm for 1 hour
🤖: Your gym session has been booked for tomorrow at 6 PM. 
    View it here: [Calendar Link](https://calendar.google.com/...)
```

### Meeting with Google Meet Link
```
🧑 You: Schedule call with John at 3pm, email: john@company.com
🤖: Meeting with John scheduled for today at 3:00 PM. 
    👤 Attendee invited: john@company.com
    🔗 Google Meet: https://meet.google.com/xyz-abc-def
```

### Event Management
```
🧑 You: List my upcoming events
🤖: 📅 Upcoming Events:
    1. **Team Meeting** - Monday, Dec 18 at 2:00 PM
    2. **Lunch with Sarah** - Tuesday, Dec 19 at 12:30 PM

🧑 You: Cancel my lunch with Sarah
🤖: 🗑️ Event 'Lunch with Sarah' has been deleted.

🧑 You: Move team meeting to 3pm tomorrow
🤖: ⏰ Event 'Team Meeting' has been rescheduled to Tuesday, Dec 19 at 3:00 PM.
```

## 🏗️ Technical Architecture

### Modern Agent Framework
```python
# Clean @function_tool decorators
@function_tool
def create_calendar_event(summary: str, start_datetime: str, 
                         attendee_email: str = None):
    """Create calendar event with Google Meet integration."""
    
    # Auto-generate Meet link when attendee present
    if attendee_email:
        event['conferenceData'] = {
            'createRequest': {
                'conferenceSolutionKey': {'type': 'hangoutsMeet'},
                'requestId': str(uuid.uuid4())
            }
        }
    
# Agent with comprehensive tool set
agent = Agent(
    name="SimpleCalendarAgent",
    tools=[create_calendar_event, list_upcoming_events, 
           delete_event, reschedule_event, ...]
)
```

### Google Meet Integration
- **Automatic Detection** - Mentions email → Creates Meet link
- **Seamless Invitations** - Calendar invites with Meet link included
- **Zero Configuration** - Works out of the box with Google Calendar API

## 📁 Project Structure

```
📦 Scheduling/
├── 🤖 simple_calendar_agent.py     # Main OpenAI Agents SDK agent
├── 🔧 calendar_tools.py            # Google Calendar + Meet tools
├── 📦 requirements.txt             # Dependencies
├── 🚀 run_calendar.sh              # Quick start script
├── 🔐 .env                         # OpenAI API key
├── 🗝️ credentials.json             # Google OAuth credentials
├── 🎫 token.json                   # Google auth token
└── 📚 README.md                    # This file
```

## 🛠️ Smart Features

### Natural Language Understanding
```python
# These all work perfectly:
"Book a meeting with Michael tomorrow at 5pm"
"Schedule lunch next Friday at 1pm" 
"Book call with Sarah at 2pm, email: sarah@company.com"
"Cancel my doctor appointment"
"Move meeting with John to next Tuesday at 3pm"
```

### Intelligent Email Detection
The agent automatically detects emails in various formats:
- `"email: john@company.com"`
- `"john@company.com"`  
- `"his email is john@company.com"`
- `"contact sarah@startup.co"`

### Event Management Operations
- **Create** - Natural language → Calendar event
- **List** - View upcoming events with IDs
- **Delete** - By event ID or title search
- **Reschedule** - Change time/date for existing events
- **Invite** - Automatic attendee invitations + Meet links

## 🔧 Setup Requirements

### 1. Google Calendar API Setup
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create new project or select existing
3. Enable Google Calendar API
4. Create OAuth 2.0 credentials
5. Download `credentials.json` to project root

### 2. OpenAI API Key
```bash
# Add to .env file
OPENAI_API_KEY=sk-proj-your-api-key-here
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## 🚀 Running the Agent

### Option 1: Quick Script
```bash
./run_calendar.sh
```

### Option 2: Manual
```bash
source venv/bin/activate
python simple_calendar_agent.py
```

### Option 3: Direct Python
```python
import asyncio
from simple_calendar_agent import run_agent

asyncio.run(run_agent())
```

## 🎯 What Makes This Truly Agentic

✅ **OpenAI Agents SDK** - Official framework, not custom wrapper  
✅ **@function_tool** decorators - Modern tool integration pattern  
✅ **Agent() declaration** - Proper agentic architecture  
✅ **Runner.run()** execution - True agentic orchestration  
✅ **Context Awareness** - Understands dates, times, preferences  
✅ **Tool Chaining** - Can perform multi-step operations  

## 📊 Feature Comparison

| Feature | Basic Calendar | This Agent |
|---------|---------------|------------|
| Natural Language | ❌ | ✅ |
| Google Meet Links | ❌ | ✅ Auto-generated |
| Smart Date Parsing | ❌ | ✅ |
| Attendee Invitations | ❌ | ✅ |
| Event Management | ❌ | ✅ Full CRUD |
| Agentic Framework | ❌ | ✅ OpenAI SDK |

## 🔒 Security & Privacy

- **OAuth 2.0** - Secure Google authentication
- **Local Storage** - Tokens stored locally only
- **API Keys** - Environment variables only
- **No Data Collection** - Everything stays on your machine

## 🐛 Troubleshooting

### Common Issues

**"No module named 'agents'"**
```bash
pip install openai-agents>=0.1.0
```

**"Calendar API not enabled"**
- Enable Google Calendar API in Cloud Console
- Regenerate credentials.json

**"Invalid token"**
- Delete `token.json` and re-authenticate
- Check OAuth scopes in credentials

### Debug Mode
```python
# Add to simple_calendar_agent.py for debugging
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **OpenAI** - For the Agents SDK framework
- **Google** - For Calendar API and Meet integration
- **Python Community** - For excellent libraries

---

**Ready for AI-powered calendar management?** 🚀  
Your assistant is powered by OpenAI Agents SDK with Google Meet integration!

### 📞 Support

Need help? Open an issue or reach out:
- 📧 Email: [Your Email]
- 🐛 Issues: [GitHub Issues]
- 📖 Docs: [Documentation Link]

**Happy Scheduling!** 📅✨ 