from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder


def main_markup():
    return ReplyKeyboardMarkup(resize_keyboard = True, keyboard = [
        [KeyboardButton(text = "🧾 Sign up")]
])


def get_markup():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text = "accept", callback_data = "✅ accept"))
    builder.add(InlineKeyboardButton(text = "cancel", callback_data = "❌ cancel"))
    return builder.as_markup()


products = ["📱 Phones", "🍔 Food", "🚘 Cars"]

def get_products():
    builder_2 = ReplyKeyboardBuilder()
    for product in products:
        builder_2.add(KeyboardButton(text = product))
    builder_2.adjust(1)
    return builder_2.as_markup(resize_keyboard = True)


product_no_1 = ["Iphone 12", "SAMSUNG S21U", "Iphone 13", "Redmi Note 12", "Tesla Phone P", "SAMSUNG S22U"]

def get_phones():
    builder_3 = ReplyKeyboardBuilder()
    for phone in product_no_1:
        builder_3.add(KeyboardButton(text = phone))
    builder_3.add(KeyboardButton(text = "⬅️ Back"))
    builder_3.adjust(2)
    return builder_3.as_markup(resize_keyboard = True)


product_no_2 = ["🍔 Burger", "🍕 Pizza", "🌭 Hot-Dog"]

def get_foods():
    builder_4 = ReplyKeyboardBuilder()
    for food in product_no_2:
        builder_4.add(KeyboardButton(text = food))
    builder_4.add(KeyboardButton(text = "⬅️ Back"))
    builder_4.adjust(1)
    return builder_4.as_markup(resize_keyboard = True)


product_no_3 = ["Tesla", "GM"]

def get_cars():
    builder_5 = ReplyKeyboardBuilder()
    for car in product_no_3:
        builder_5.add(KeyboardButton(text = car))
    builder_5.add(KeyboardButton(text = "⬅️ Back"))
    builder_5.adjust(1)
    return builder_5.as_markup(resize_keyboard = True)


send_options = InlineKeyboardMarkup(inline_keyboard = [
        [InlineKeyboardButton(text = "Yes, i want to buy it", callback_data = "positive")],
        [InlineKeyboardButton(text = "No, i don't want to buy it", callback_data = "negative")],
])


def how_many(piece = 9):
    builder_6 = ReplyKeyboardBuilder()
    for i in range(1, piece + 1):
        builder_6.add(KeyboardButton(text = str(i)))
    builder_6.add(KeyboardButton(text = "⬅️ Back"))
    builder_6.adjust(3)
    return builder_6.as_markup(resize_keyboard = True)
    
