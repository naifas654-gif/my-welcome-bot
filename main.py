import os
import asyncio
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, ChatMemberHandler

TOKEN = "8737393959:AAGfNXQAKc6SEemkh07KfBASY2SbIVv5Pek"
CHANNEL_URL = "https://t.me/REDDEAD19/9" 

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def welcome_new_member(update: Update, context: ContextTypes.DEFAULT_TYPE):
    member = update.chat_member.new_chat_member
    if member.status in ["member", "administrator"]:
        user_name = member.user.first_name
        text = f"أهلاً بك يا {user_name} في مجموعتنا! 👋🏻\n\nنرجو منك قراءة القوانين بعناية لتجنب أي إزعاج."
        keyboard = [[InlineKeyboardButton("قوانين المجموعة 📜", url=CHANNEL_URL)]]
        
        await update.effective_chat.send_photo(
            photo="https://i.ibb.co/6ZzX5jQ/1000035103.jpg", 
            caption=text,
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

async def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(ChatMemberHandler(welcome_new_member, chat_member_types=ChatMemberHandler.ANY_CHAT_MEMBER))
    
    await app.initialize()
    await app.start()
    await app.updater.start_polling()
    await asyncio.Event().wait()

if __name__ == '__main__':
    asyncio.run(main())
