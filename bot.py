from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

from constants.files import get_ready_file_name
from sort_file import sort_file


async def file_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    file = await context.bot.get_file(update.message.document)
    file_name = update.message.document.file_name
    await file.download_to_drive(file_name)
    sort_file(file_name)
    chat_id = update.message.chat_id
    document = open(get_ready_file_name(file_name), "rb")
    await context.bot.send_document(chat_id, document)

if __name__ == "__main__":
    app = ApplicationBuilder().token("6086619550:AAEZF8Dc9WCpORHm2tSPskRn9au4e1vGdvM").build()
    app.add_handler(MessageHandler(filters.Document.ALL, file_handler))
    print("running")
    app.run_polling()

