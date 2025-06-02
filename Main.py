📡 SecureChain Daily Crypto Signals Bot

""" Automated trading signals posted daily to:

🔸 SecureChain Telegram Channel: https://t.me/SecureChainSignals

🔸 Crypto Signal Analysis Group: https://t.me/cryptosignanalysis


Promotes investments through:

🌐 Apwxico.com — blockchain-powered trading with high ROI

📞 WhatsApp contact: https://wa.me/message/GH53ISFH45EWG1


#CryptoSignals #Apwxico #DailyTrades """

import os import requests import datetime from telegram import Bot from dotenv import load_dotenv

=== Load Environment Variables ===

load_dotenv()

=== CONFIG ===

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN') CHANNEL_ID = '@SecureChainSignals' GROUP_ID = '@cryptosignanalysis'

WHATSAPP_LINK = 'https://wa.me/message/GH53ISFH45EWG1' APWXICO_LINK = 'https://apwxico.com'

=== Fetch Live Market Data from CoinGecko ===

def fetch_market_data(): url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,binancecoin&vs_currencies=usd' response = requests.get(url) prices = response.json() return [ { 'symbol': 'BTC/USDT', 'action': 'LONG', 'entry': f"{prices['bitcoin']['usd']:,}", 'tp1': f"{prices['bitcoin']['usd'] * 1.02:,.0f}", 'tp2': f"{prices['bitcoin']['usd'] * 1.03:,.0f}", 'sl': f"{prices['bitcoin']['usd'] * 0.98:,.0f}" }, { 'symbol': 'ETH/USDT', 'action': 'LONG', 'entry': f"{prices['ethereum']['usd']:,}", 'tp1': f"{prices['ethereum']['usd'] * 1.03:,.0f}", 'tp2': f"{prices['ethereum']['usd'] * 1.05:,.0f}", 'sl': f"{prices['ethereum']['usd'] * 0.97:,.0f}" }, { 'symbol': 'BNB/USDT', 'action': 'SHORT', 'entry': f"{prices['binancecoin']['usd']:,}", 'tp1': f"{prices['binancecoin']['usd'] * 0.97:,.0f}", 'tp2': f"{prices['binancecoin']['usd'] * 0.95:,.0f}", 'sl': f"{prices['binancecoin']['usd'] * 1.02:,.0f}" } ]

def format_signal(signal): return f""" 📊 {signal['symbol']} Signal ➡️ Action: {signal['action']} 🎯 Entry: {signal['entry']} ✅ TP1: {signal['tp1']} ✅ TP2: {signal['tp2']} ❌ Stop Loss: {signal['sl']} """

def generate_post(): today = datetime.datetime.now().strftime('%B %d, %Y') header = f"🚀 Daily Crypto Signals – {today}" body = "\n".join([format_signal(sig) for sig in fetch_market_data()]) pitch = f""" 🔗 Invest with Confidence: Apwxico.com 💸 Join our blockchain-powered auto-trading platform for high ROI. 📞 Have questions? Chat with us: WhatsApp Link

#CryptoSignals #Apwxico #DailyTrades """ return f"{header}\n{body}\n{pitch}"

def post_to_telegram(): bot = Bot(token=TELEGRAM_TOKEN) message = generate_post() bot.send_message(chat_id=CHANNEL_ID, text=message, parse_mode='Markdown') bot.send_message(chat_id=GROUP_ID, text=message, parse_mode='Markdown')

if name == 'main': post_to_telegram()

