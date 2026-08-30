from telegram import Update
from telegram.ext import Application, MessageHandler,CommandHandler, filters, ContextTypes
from config import TOKEN
async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я твой первый бот 🤖")
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я твой бот-помощник. Напиши /help, чтобы узнать, что я умею.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Доступные команды:\n/start — начать\n/help — это меню")
app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(MessageHandler(filters.TEXT, reply))
app.run_polling()

 