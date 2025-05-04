# Nitza Physo – Wellness Game  (Mostly Physiotherapy Exercise and support) Platform !

## Created for the **Nitzanim Hackathon – 2025 !

🎮 **Nitza Physio** is an interactive wellness platform designed to promote physical therapy and mental well-being through games, breathing exercises, and a supportive AI chatbot.

## ✨ Features

- 💬 **AI Chatbot** powered by GPT-4o via Azure OpenAI (Hebrew support for welcome only, main chat in English)
- ✅ **User-friendly main menu** with smooth navigation
- 🧘 **Breathing exercises** to encourage relaxation
- 🧠 **Memory game** to enhance cognitive abilities
- ✋ **Hand tracking game** using camera input (if enabled)
- 🔊 **Background music** toggle (on/off)
- 👤 **User profile system**


## 🛠 Technologies

- `Python`
- `Pygame`
- `Azure OpenAI API` (for chatbot responses)
- `MediaPipe` (for hand tracking game)
- Hebrew font: `Alef-Regular.ttf`

## 🚀 Getting Started

1. Install the required dependencies:
    ```bash
    pip install pygame openai mediapipe
    ```

2. Make sure `AzureChatAPI.py` includes your Azure OpenAI credentials.

3. Run the main application:
    ```bash
    python main.py
    ```

## 📁 Project Structure
Nitza_Physooo/
├── main.py
├── CONSTANTS.py
├── Chatbot.py
├── AzureChatAPI.py
├── BUTTONS.py
├── Breath_excersise.py
├── Hand_Tracking.py
├── Memory_game.py
├── profile_manager.py
├── crown.png
├── image_2025-04-08_142824057.jpg
└── fonts/
└── Alef-Regular.ttf
