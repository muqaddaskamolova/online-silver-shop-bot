from telebot import TeleBot
from telebot.types import Message
from bot_admin import *
from configs import *
from admin_keyboards import *
from queries import *

bot = TeleBot(TOKEN, parse_mode='HTML')


@bot.message_handler(commands=['start'])
def command_start(message: Message):
    chat_id = message.chat.id
    if chat_id == ADMIN_ID:
        admin(message)
    else:
        pass


def admin(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id,
                     """ <b>Assalomu alaykum hurmatli bot administratori! ✅
                      Quyidagilardan birini tanlang!👇👇 </b>""",
                     reply_markup=generate_admin_main_menu())


@bot.message_handler(func=lambda message: message.text == "📝 Kategoriya qo`shish" and message.chat.id == ADMIN_ID)
def ask_add_category_name(message: Message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id,
                           f"""<b>📝 Kategoriya nomini kiriting:</b>""",
                           reply_markup=generate_btn_back())

    bot.register_next_step_handler(msg, ask_agree_disagree_for_adding)


def ask_agree_disagree_for_adding(message: Message):
    chat_id = message.chat.id
    if message.text == "⬅ Ortga":
        admin(message)
    else:
        category_name = message.text
        msg = bot.send_message(chat_id, f"""<b>Ushbu Kategoriya qo`shishni tasdiqlang!</b>""",
                               reply_markup=generate_btn_yes_no())
        bot.register_next_step_handler(msg, submitting_add_category, category_name)


def submitting_add_category(message: Message, category_name):
    chat_id = message.chat.id
    if message.text == "✅ Tasdiqlash":
        insert_category(category_name)
        bot.send_message(chat_id, f"""<b>Kategoriya qo`shildi ✅</b>""")
        admin(message)
    elif message.text == "❌ Bekor qilish":
        bot.send_message(chat_id, f"""<b>Kategoriya qo`shish bekor qilindi❌ </b>""")
        admin(message)

    elif message.text == " ⬅ Ortga":
        bot.send_message(chat_id, f"""<b>Kategoriya qo`shish bekor qilindi❌ </b>""")
        admin(message)


@bot.message_handler(func=lambda message: message.text == "❌ Kategoriya o`chirish" and message.chat.id == ADMIN_ID)
def ask_del_category_name(message: Message):
    pass


@bot.message_handler(func=lambda message: message.text == "🛍 Tovar qo`shish" and message.chat.id == ADMIN_ID)
def ask_add_product_name(message: Message):
    pass


@bot.message_handler(func=lambda message: message.text == "❌ Tovar o`chirish" and message.chat.id == ADMIN_ID)
def ask_del_product_name(message: Message):
    pass


@bot.message_handler(
    func=lambda message: message.text == "👨‍👩‍👦‍👦 Foydalanuvchilar soni" and message.chat.id == ADMIN_ID)
def count_users(message: Message):
    pass


@bot.message_handler(func=lambda message: message.text == "📩  Habarnomalar jo`natish" and message.chat.id == ADMIN_ID)
def ask_method_mailing(message: Message):
    pass


bot.polling(none_stop=True)
