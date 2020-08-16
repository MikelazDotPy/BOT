import telebot
import qrcode
from PIL import Image
TOKEN = "1264467384:AAFEdn0dI2f80rh8YYbx_CUbuZ-LGIZa_eg"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=['text'])
def start_message(message):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=15,
        border=1,
    )
    qr.add_data(message.text)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qr.png")
    img = Image.open('g.png')
    watermark = Image.open('qr.png').convert("RGBA")

    img.paste(watermark, (138, 500), watermark)
    img.save("gg.png")
    bot.send_photo(message.chat.id, open('gg.png', 'rb'))


bot.polling()