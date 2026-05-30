from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# O'z tokeningizni shu yerga qo'ying
TOKEN = "8581713859:AAHnJaxKtuTck7CZB275YHAbVV5djgAltC0"


# /start buyrug'i
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    foydalanuvchi = update.effective_user.first_name
    await update.message.reply_text(
        f"Salom, {foydalanuvchi}! 👋\n"
        "Men buyruqlar bilan ishlaydigan botman.\n\n"
        "Mavjud buyruqlar:\n"
        "/help — Yordam\n"
        "/haqida — Bot haqida\n"
        "/echo — Xabaringizni qaytarish"
    )


# /help buyrug'i
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📋 Buyruqlar ro'yxati:\n\n"
        "/start — Botni ishga tushirish\n"
        "/help — Yordam olish\n"
        "/haqida — Bot haqida ma'lumot\n"
        "/echo [matn] — Matningizni qaytaradi\n\n"
        "Misol: /echo Salom dunyo!"
    )


# /haqida buyrug'i
async def haqida(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Bu bot Python va python-telegram-bot\n"
        "kutubxonasi yordamida yaratilgan.\n\n"
        "Versiya: 1.0\n"
        "Muallif: Siz 😊"
    )


# /echo buyrug'i — foydalanuvchi yozgan matnni qaytaradi
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        matn = " ".join(context.args)
        await update.message.reply_text(f"🔁 {matn}")
    else:
        await update.message.reply_text(
            "Iltimos, matn kiriting.\nMisol: /echo Salom!"
        )


# Botni ishga tushirish
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # Buyruqlarni ro'yxatdan o'tkazish
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("haqida", haqida))
    app.add_handler(CommandHandler("echo", echo))

    print("✅ Bot ishga tushdi! To'xtatish uchun Ctrl+C bosing.")
    app.run_polling()


if __name__ == "__main__":
    main()