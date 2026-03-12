# 🌤️ Telegram Weather Bot

A simple **Python Telegram bot** that provides real-time weather information for Indian cities.  
Users can request weather updates by sending commands directly in Telegram.

The bot scrapes weather data from **timeanddate.com** and replies with current weather conditions.

---

## 🚀 Features

- Get current weather for any Indian city
- Telegram command-based interaction
- Web scraping using BeautifulSoup
- Multi-user support
- Lightweight Python backend automation project

---

## 🛠 Technologies Used

- Python
- Requests
- BeautifulSoup
- pyTelegramBotAPI (telebot)
- Telegram Bot API

---

## 📂 Project Structure

```
├── webscrap.py   
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/weather-telegram-bot.git
cd weather-telegram-bot
```

---

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install requests beautifulsoup4 pyTelegramBotAPI
```

---

## 🔑 Setup Bot Token

Create a bot using **@BotFather** on Telegram and get your bot token.

Then add the token to your script:

```python
BOT_TOKEN = "YOUR_BOT_TOKEN"
```

For better security, use environment variables:

```python
import os
BOT_TOKEN = os.environ.get("BOT_TOKEN")
```

---

## ▶️ Running the Bot

Run the bot with:

```bash
python bot.py
```

The bot will start listening for commands from Telegram.

---

## 💬 Bot Commands

| Command | Description |
|--------|-------------|
| `/start` | Show welcome message |
| `/help` | Display help and commands |
| `/weather <city>` | Get current weather for a city |

Example:

```
/weather pune
/weather mumbai
/weather delhi
```

---

## 🌍 Example Output

```
City: Pune
Time: 19:30
Temperature: 30°C
Weather: Partly Cloudy
Wind: 14 km/h
Forecast: 37 / 20 °C
```

---

## ☁️ Deployment

You can deploy this bot on free platforms such as:

- Render
- Railway
- PythonAnywhere

This allows the bot to run **24/7 without keeping your computer on**.

---

## 📚 Learning Outcomes

This project demonstrates:

- Python backend development
- Telegram bot creation
- API integration
- Web scraping
- Automation

---

## ⚠️ Security Note

Never commit your **Telegram bot token** to GitHub.

Use environment variables instead:

```python
import os
BOT_TOKEN = os.environ.get("BOT_TOKEN")
```

## 👨‍💻 Author

chirayu kale

Created as a **Python backend learning project** using Telegram bots and web scraping.