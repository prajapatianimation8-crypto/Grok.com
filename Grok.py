import os
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("8948331875:AAGOpnr-XMCiD29-8t0SmB-67WuiGCZRY88")
XAI_API_KEY = os.getenv("xai-Q3SERAkWOheXCdvDnhz1hOGWujtifNW12zT9L6JW1kK2yek7cOiyJ9rfYfwS4XCLaWu6XBRRyu8RCbUj")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Namaste! Main Grok AI hoon. Kya poochna hai?")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    
    # Grok API call
    headers = {
        "Authorization": f"Bearer {xai-Q3SERAkWOheXCdvDnhz1hOGWujtifNW12zT9L6JW1kK2yek7cOiyJ9rfYfwS4XCLaWu6XBRRyu8RCbUj}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "grok-4",  # ya grok-4.3 jo available ho
        "messages": [{"role": "user", "content": user_message}]
    }
    
    response = requests.post(
        "https://api.x.ai/v1/chat/completions",  # official endpoint
        json=payload,
        headers=headers
    )
    
    if response.status_code == 200:
        reply = response.json()["choices"][0]["message"]["content"]
        await update.message.reply_text(reply)
    else:
        await update.message.reply_text("Error aa gaya. Baad mein try karo.")

def main():
    app = Application.builder().token(8948331875:AAGOpnr-XMCiD29-8t0SmB-67WuiGCZRY88).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    print("Bot chal raha hai...")
    app.run_polling()

if __name__ == "__main__":
    main()
