import requests
import random
import time
import pytz
from datetime import datetime

# === Required Settings ===
BOT_TOKEN = '7788331565:AAHCEOlBuYIYT-rgqiWkdrr-llr30V9-yDw'
CHANNEL_ID = '-1002167505208'  # Replace with your channel ID

# === Promotion Messages ===
promotion_messages = [
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

    """🚀📈 Trade Like a Beast with Bullman Capital!
💹 We drop REAL setups – not useless signals
🎯 Clean charts, sniper entries, daily updates
🔗 https://pric.app/_Pv7r
📤 DM payment slip to @TeamBullmanCapital NOW!"""
]

# === Load Morning Messages from File ===
def load_morning_messages(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

morning_messages = load_morning_messages("Good_Morning_Traders_Messages.txt")

# === Timezone (IST) ===
IST = pytz.timezone('Asia/Kolkata')

# === Fixed Sending Times (24-hr format)
fixed_send_times = ['10:00', '13:00', '16:00', '19:00', '22:00', '23:30']
morning_time = '09:00'

# === Track Last Sent Times Per Day ===
last_sent_times = {}
print("Current time is:", now.strftime("%H:%M:%S"))

# === Send Message Function ===
def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        'chat_id': CHANNEL_ID,
        'text': text,
        'parse_mode': 'HTML'
    }
    response = requests.post(url, data=data)
    status = response.status_code
    print(f"[{datetime.now(IST).strftime('%H:%M:%S')}] Sent message. Status: {status}")

# === Main Bot Loop ===
print("Bot started... waiting for fixed time windows.")

while True:
    now = datetime.now(IST)
    current_time = now.strftime('%H:%M')
    today = now.strftime('%Y-%m-%d')

    # === Morning Message (Mon–Fri only)
    if now.weekday() < 5 and current_time == morning_time:
        key = f"{today}-morning"
        if not last_sent_times.get(key):
            msg = random.choice(morning_messages)
            send_message(msg)
            last_sent_times[key] = True

    # === Promotional Messages at 3hr intervals
    for send_time in fixed_send_times:
        key = f"{today}-{send_time}"
        if current_time == send_time and not last_sent_times.get(key):
            msg = random.choice(promotion_messages)
            send_message(msg)
            last_sent_times[key] = True

    time.sleep(30)
