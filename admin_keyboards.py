from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def generate_admin_main_menu():
    markup = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn_add_category = KeyboardButton(text='📝 Kategoriya qo`shish')
    btn_add_product = KeyboardButton(text='🛍 Tovar qo`shish')
    btn_count_users = KeyboardButton(text='👨‍👩‍👦‍👦 Foydalanuvchilar soni')
    btn_mailing = KeyboardButton(text='📩 Habarnomalar jo`natish')
    btn_del_category = KeyboardButton(text='❌ Kategoriya o`chirish')
    btn_del_product = KeyboardButton(text='❌ Tovar o`chirish')

    markup.add(btn_add_category,
               btn_add_product,
               btn_count_users,
               btn_mailing,
               btn_del_category,
               btn_del_product)
    return markup


def generate_btn_back():
    markup = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn_back = KeyboardButton(text='⬅ Ortga')
    markup.add(btn_back)
    return markup


def generate_btn_yes_no():
    markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn_yes = KeyboardButton(text='✅ Tasdiqlash')
    btn_no = KeyboardButton(text='❌ Bekor qilish')
    btn_back = KeyboardButton(text='⬅ Ortga')
    markup.add(btn_yes, btn_no, btn_back)
    return markup
