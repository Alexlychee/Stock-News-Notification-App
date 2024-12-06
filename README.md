# 🚀 Stock Price Notifier with News Alerts 📈📰

A Python-based automation tool that tracks the daily stock price movements of a specified company, compares recent changes, and sends SMS notifications with relevant news headlines if significant changes occur. This project uses **Alpha Vantage** for stock data, **NewsAPI** for news headlines, and **Twilio** for SMS notifications.

---

## 📋 Features
- Fetches daily stock data for a specified company using the Alpha Vantage API.
- Analyzes stock price changes and calculates the percentage difference between two consecutive days.
- Fetches top news headlines related to the company if the price change exceeds a specified threshold.
- Sends SMS alerts with stock performance and news headlines using Twilio.

---

## 💻 Tech Stack
- **Python**: Core programming language for implementation.
- **APIs**:
  - [Alpha Vantage](https://www.alphavantage.co): For stock market data.
  - [NewsAPI](https://newsapi.org): For news articles.
  - [Twilio](https://www.twilio.com): For sending SMS notifications.
- **Libraries**: 
  - `requests` for HTTP requests.
  - `twilio` for SMS integration.
  - `python-dotenv` for managing environment variables.

---

## ⚙️ Prerequisites
Ensure you have the following:
- Python 3.8 or above installed on your system.
- Access to the Alpha Vantage, NewsAPI, and Twilio services (create accounts if needed).
- Installed dependencies via `pip install -r requirements.txt`.

---

## 📂 Project Setup
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/Stock-News-Notification-App.git
   cd Stock-News-Notification-App
2. **Install required packages**:
   ```bash
   pip install -r requirements.txt
3. **Create a `.env` file in the root directory**:
   ```bash
   ALPHA_VANTAGE_API_KEY=your_alpha_vantage_api_key
   NEWS_API_KEY=your_news_api_key
   TWILIO_ACCOUNT_SID=your_twilio_account_sid
   TWILIO_AUTH_TOKEN=your_twilio_auth_token
   TWILIO_PHONE=your_twilio_phone_number
   RECEIVER_PHONE=receiver_phone_number
4. **Run the application**:
   ```bash
   python main.py

---

## 🛠️ How It Works
- The script fetches stock data from Alpha Vantage's API.
- Calculates the percentage change between the last two closing prices.
- If the change exceeds 5%, it queries NewsAPI for the latest company news.
- Sends SMS alerts with stock updates and news headlines via Twilio.
