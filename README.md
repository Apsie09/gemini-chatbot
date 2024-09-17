# Gemini Chatbot

Welcome to **Gemini Chatbot**, a console-based chatbot powered by the Gemini-Pro Large Language Model (LLM). This project offers a simple, interactive chat interface to engage with Gemini-Pro, providing real-time conversational capabilities from your terminal.

## Features

- **Text-to-Text Conversations**: Converse with the Gemini-Pro model to receive detailed, human-like responses.
- **Command-Line Interface**: A user-friendly command-line interface (CLI) that allows easy interaction with the chatbot.
- **Session Management**: You can start and end chat sessions at your convenience, with the option to save chat logs.
- **Extensibility**: The chatbot can be extended with more features or integrations as needed.

## Example Interaction
> How is the weather today?
>
> Gemini: The weather in your area looks sunny with a high of 25°C.

## Configuration
API Key: Ensure that you have a valid API key from the Gemini-Pro service and place it in the credentials.ini file.
Custom Commands: The chatbot can be extended to support custom commands or features. Refer to chatbot.py for examples.

## Tech Stack

- **Programming Language**: Python
- **Framework**: Custom-built Python CLI
- **Large Language Model (LLM)**: Gemini-Pro API
- **Environment Management**: Python `venv`
- **Configuration Management**: `.ini` file for API keys
- **External Libraries**: 
  - `requests` for handling API calls
  - `configparser` for managing configurations

