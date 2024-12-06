import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# Load environment variables from the .env file
load_dotenv()

# Required environment variables:
# ALPHA_VANTAGE_API_KEY: API key for Alpha Vantage to fetch stock data.
ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
# NEWS_API_KEY: API key for NewsAPI to fetch news articles.
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
# TWILIO_ACCOUNT_SID: Twilio account SID for sending messages.
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
# TWILIO_AUTH_TOKEN: Twilio authentication token for API access.
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
# TWILIO_PHONE: Your Twilio phone number to send messages from.
from_phone = os.getenv("TWILIO_PHONE")
# RECEIVER_PHONE: The phone number to send messages to.
to_phone = os.getenv("RECEIVER_PHONE")

# Get yesterday's closing stock price.
parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": ALPHA_VANTAGE_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=parameters)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterdays_closing_data = data_list[0]["4. close"]

# Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]["4. close"]

# Find the positive difference and indicate whether the stock is up a percentage or down a percentage
pos_difference = float(yesterdays_closing_data) - float(day_before_yesterday_data)
up_down = None
if pos_difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

# Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
average_value = (float(yesterdays_closing_data) + float(day_before_yesterday_data)) / 2
percent_difference = round((pos_difference / average_value) * 100)

# If percentage is greater than five, send an SMS text to the users phone
if abs(percent_difference) > 5:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "q": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_data = news_response.json()

    # Creates a list containing the first three articles pertaining to the stock
    first_three_articles = news_data["articles"][:3]

    # Create a new list of the first 3 articles headline and description using list comprehension.
    article_headline_description = [f"{STOCK_NAME}: {up_down}{percent_difference}% \nHeadline: {articles['title']}. \nBrief: {articles['description']}" for articles in first_three_articles]

    # Send each article as a separate message via Twilio.
    client = Client(account_sid, auth_token)
    for articles in article_headline_description:
        message = client.messages.create(
          from_=from_phone,
          body=articles,
          to=to_phone
        )