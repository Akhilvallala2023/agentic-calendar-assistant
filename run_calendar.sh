#!/bin/bash
# Simple script to run the calendar agent with venv activated
# Usage: ./run_calendar.sh

echo "🚀 Starting AI Calendar Assistant..."
echo "📅 Activating virtual environment..."

# Navigate to script directory
cd "$(dirname "$0")"

# Activate virtual environment and run the calendar agent
source venv/bin/activate && python simple_calendar_agent.py 