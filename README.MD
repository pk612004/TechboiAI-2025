                               Techboi-AI – Your Personal AI Assistant

Ever wished for your own AI-powered assistant? Imagine sending emails without typing, searching Wikipedia without opening a browser, or even playing music with a simple voice command.
Meet Techboi-AI – a smart virtual assistant designed to make your daily tasks easier and more efficient!

  What Can Techboi-AI Do?

 -Send Emails & WhatsApp Messages – Hands-free communication at your command.
 -Play Music & Videos – Enjoy seamless entertainment with voice commands.
 -Fetch Wikipedia & Google Results – No more manual searches, just ask!
 -Open Apps & Websites – Quickly launch Google, YouTube, Notepad, Calculator, and more.
 -Get Weather Updates & News – Stay informed with real-time info.
 -Fun Interactions – Get jokes, random advice, and trending movies.

  Tech Stack & Key Components

  requests – Fetches real-time data from online sources.
  pyttsx3 – Converts text into speech for AI-powered responses.
  speech_recognition – Listens to and understands voice commands.
  decouple – Manages environment variables like API keys securely.
  datetime – Handles time-related queries & functionalities.
  random – Generates random jokes, advice, and more for a fun experience.
  pprint – Formats data neatly for better debugging and readability.  

  Project Structure

  online_ops.py – Manages web-based tasks like news fetching, weather updates, and Google/Wikipedia searches.
  os_ops.py – Handles system-related commands like opening Notepad, Calculator, and the Command Prompt.
  utils.py – Utility functions for greeting users and initializing the assistant.

  How to Use Techboi-AI
  1️ Installation & Setup
  Clone the repository and install dependencies:
  git clone https://github.com/pk612004/Techboi-AI.git
  pip install -r requirements.txt
  2️ Configure API Keys
  If using OpenAI or any external services, create a .env file and add your credentials:
  OPENAI_API_KEY=your_api_key
  3️ Run the AI Assistant
  python main.py
