from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
from config import TOKEN
async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я твой первый бот 🤖")
app = Application.builder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, reply))
app.run_polling()

 