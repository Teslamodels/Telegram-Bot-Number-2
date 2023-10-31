from aiogram import Router, F, types
from aiogram.enums import ParseMode
from button import get_phones, send_options


router_8 = Router()


@router_8.message(F.text == "📱 Phones")
async def let_phones_open(message: types.Message):
    await message.delete()
    await message.answer("<b>Welcome to online phone shop</b>", reply_markup = get_phones(), parse_mode=ParseMode.HTML)


@router_8.message(F.text == "Tesla Phone P")
async def buy_this_phone_Tesla_Phone_P(message: types.Message):
    await message.delete()
    await message.answer_photo(photo = "https://ibb.co/2yFP661", caption = "Name: Tesla Phone P\n\nPrice: $1500\nColor: Black\nYear: 2025\nDescription: This is Elon Musk\n\nDefine the piece, if you want to buy", reply_markup = send_options)


@router_8.message(F.text == "Iphone 12")
async def buy_this_phone_12(message: types.Message):
    await message.delete()
    await message.answer_photo(photo = "https://ibb.co/9r1Dw6P", caption = "Name: Iphone 12\n\nPrice: $1200\nColor: Blue\nYear: 2020\nDescription: Best Tecnology\n\nDefine the piece, if you want to buy", reply_markup = send_options)


@router_8.message(F.text == "Redmi Note 12")
async def buy_this_phone_Redmi_Note_12(message: types.Message):
    await message.delete()
    await message.answer_photo(photo = "https://ibb.co/c2tvxCD", caption = "Name: Redmi Note 12\n\nPrice: $900\nColor: Black\nYear: 2022\nDescription: The China\n\nDefine the piece, if you want to buy", reply_markup = send_options)


@router_8.message(F.text == "Iphone 13")
async def buy_this_phone_Iphone_13(message: types.Message):
    await message.delete()
    await message.answer_photo(photo = "https://ibb.co/xYDBhBY", caption = "Name: Iphone 13\n\nPrice: $1500\nColor: Red\nYear: 2022\nDescription: Realy Good\n\nDefine the piece, if you want to buy", reply_markup = send_options)


@router_8.message(F.text == "SAMSUNG S21U")
async def buy_this_phone_SAMSUNG_S21U(message: types.Message):
    await message.delete()
    await message.answer_photo(photo = "https://ibb.co/0Q6fLcV", caption = "Name: SAMSUNG S21U\n\nPrice: $1000\nColor: Black\nYear: 2022\nDescription: Good\n\nDefine the piece, if you want to buy", reply_markup = send_options)


@router_8.message(F.text == "SAMSUNG S22U")
async def buy_this_phone_SAMSUNG_S22U(message: types.Message):
    await message.delete()
    await message.answer_photo(photo = "https://ibb.co/Tvjbx4h", caption = "Name: SAMSUNG S22U\n\nPrice: $1600\nColor: Red\nYear: 2023\nDescription: Better\n\nDefine the piece, if you want to buy", reply_markup = send_options)


@router_8.message(F.text.regexp(r"^(\d+)$"))
async def do_no(message: types.Message):
    await message.answer(f"{message.text} is added to basket 🤝")
