import requests
import random
import time
import pytz
from datetime import datetime
import schedule

# === Required Settings ===
BOT_TOKEN = '7788331565:AAHCEOlBuYIYT-rgqiWkdrr-llr30V9-yDw'
CHANNEL_ID = '-1002167505208'  # Replace with your private channel's numeric ID

# === Random Messages List ===
messages = [
    """⚠️💣 LIMITED SPOTS for Bullman Capital’s Personal Trades!
💸 Trades that actually make money – shared in REAL-TIME!
👉 Don’t wait – you’re missing pips every second
🔗 https://pric.app/_Pv7r
📲 Confirm with screenshot @TeamBullmanCapital 🔐""",

    """🔥📊 LIVE TRADES. NO SIGNAL BS. JUST REAL PROFITS!
Get into Bullman Capital’s exclusive trade vault 💼💰
💹 Full transparency – watch us trade LIVE
🔗 https://pric.app/_Pv7r
📤 Send payment screenshot to @TeamBullmanCapital""",

    """🧠💸 Smart Money Follows Smart Trades
Join Bullman Capital’s Private Trade Access 🔐
🎯 Real Charts, Real Results
💥 Become a part of the WINNING CIRCLE
🔗 https://pric.app/_Pv7r
📩 Proof to @TeamBullmanCapital for INSTANT entry 🚀""",

    """💹💥 Wanna TRADE like the PROS?
Bullman Capital's Personal Trades = 🔥🔥🔥
📉 LIVE Entries
📈 SL/TP Levels
💰 Consistent Results
👉 https://pric.app/_Pv7r
📲 Share screenshot with @TeamBullmanCapital""",

    """🎯📈 Follow the Trades of a Winning Team – Bullman Capital 💥
✅ Verified Results
✅ Daily Profits
✅ No Signal Noise – Just Real Trades
🔗 https://pric.app/_Pv7r
💌 Send payment screenshot to @TeamBullmanCapital and join now!.""",

    """🔥💸 Daily Profits. Zero Guesswork. Full Transparency. 💸🔥
⚡️ Tap into Bullman Capital’s PRIVATE trades – REAL setups 📊
🎯 Entry • SL • TP – all shared live
🔗 https://pric.app/_Pv7r
📤 DM proof to @TeamBullmanCapital to unlock access""",

    """🚨💥 BREAKING! Bullman Capital’s Real-Time Trades Are LIVE! 💥🚨
💹 Copy exact entries, exits, SL/TP from our private vault 💰
👉 https://pric.app/_Pv7r
📩 Send payment screenshot to @TeamBullmanCapital & GET IN!""",

""" 🚀📈 Trade Like a Beast with Bullman Capital!
💹 We drop REAL setups – not useless signals
🎯 Clean charts, sniper entries, daily updates
🔗 https://pric.app/_Pv7r
📤 DM payment slip to @TeamBullmanCapital NOW!"""
]

# === Fixed 9AM Message (Mon–Fri) ===
morning_msg = """📈 Good morning traders! Start your day with Bullman Capital’s expert insights.
Let’s dominate the market together. 💪"""

# === Timezone (IST) ===
IST = pytz.timezone('Asia/Kolkata')

# === Send Message Function ===
def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        'chat_id': CHANNEL_ID,
        'text': text,
        'parse_mode': 'HTML'
    }
    response = requests.post(url, data=data)
    print(f"[{datetime.now(IST).strftime('%H:%M:%S')}] Sent message. Status: {response.status_code}")

# === Message Senders ===
def send_random_msg():
    now = datetime.now(IST)
    if 10 <= now.hour <= 23:
        msg = random.choice(messages)
        send_message(msg)

def send_morning_msg():
    now = datetime.now(IST)
    if now.weekday() < 5:  # Monday–Friday
        send_message(morning_msg)

# === Random Scheduling ===
def schedule_random_times():
    hour = 10
    while hour <= 23:
        minute = random.randint(0, 59)
        t = f"{hour:02d}:{minute:02d}"
        schedule.every().day.at(t).do(send_random_msg)
        print(f"Scheduled random message at {t}")
        hour += random.choice([3, 4])

# === Start Logic ===
if __name__ == "__main__":
    # Send an immediate message on start
    print("Sending immediate message on startup...")
    send_random_msg()

    # Schedule morning message
    schedule.every().day.at("09:00").do(send_morning_msg)

    # Schedule daily random messages
    schedule_random_times()

    # Main loop
    print("Bot started and running...")
    while True:
        schedule.run_pending()
        time.sleep(10)
