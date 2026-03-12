# 🌤️ Weather Telegram Bot

A Telegram bot that fetches real-time weather data for any Indian city using web scraping.

## 📸 Demo
Send /weather pune to the bot and get instant weather updates!

## ✨ Features
- 🌡️ Current temperature
- ☁️ Weather condition
- 💨 Wind speed & direction
- 📅 Hourly forecast
- 🏙️ Works for any Indian city

## 🛠️ Built With
- Python
- BeautifulSoup4 — web scraping
- pyTelegramBotAPI — telegram bot
- python-dotenv — secure token handling

## ⚙️ Setup

### 1. Clone this repo
git clone https://github.com/chirayukale2006-gif/weather-telegram-bot.git
cd weather-telegram-bot

### 2. Install dependencies
pip install -r requirements.txt

### 3. Create .env file
BOT_TOKEN=your_telegram_bot_token_here

### 4. Get your Bot Token
- Open Telegram
- Search @BotFather
- Send /newbot
- Copy the token into .env

### 5. Run the bot
python webscrap.py

## 📖 Commands
| Command | Description |
|---------|-------------|
| /start | Welcome message |
| /weather <city> | Get weather for any Indian city |
| /help | Show all commands |

## 💡 Example
/weather pune
/weather mumbai
/weather delhi

## 👨‍💻 Author
Chirayु Kale — built while learning Python & web scraping