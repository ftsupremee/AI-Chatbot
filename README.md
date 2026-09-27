AI CHATBOT
A desktop AI chatbot interface implemented in Python with PyQt5 and Groq API. Features include keypress triggers (enter key), styled GUI components, scrollable output handling and API response processing.

Features
-Desktop GUI: Native window interface implemented in PyQt5.
-nstant Keyboard Triggers: Using the enter key in the text field or clicking "Get answer" will send prompts.
-Scrollable Output: Using QScrollArea combined with word wrapping to view long responses.
-Fast Inference: Backed by Groq API's cloud LLM execution.
-Secure Key Management: Uses python-dotenv to securely load API keys from environment variables.

Prerequisites & Installation
1. Prerequisites
Ensure that you have python 3.10+ and git installed on your machine.

2. Virtual Environment
Open your terminal in the project directory and create a virtual environment:

```bash

# Navigate to project folder

cd chatbot

# Create virtual environment

python3 -m venv .venv

# Activate virtual environment

source .venv/bin/activate