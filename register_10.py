from aiogram import Router, F, types
from button import get_cars, send_options


router_10 = Router()


@router_10.message(F.text == "🚘 Cars")
async def let_cars_open(message: types.Message):
    await message.delete()
    await message.answer("Only Electric Cars", reply_markup = get_cars())


@router_10.message(F.text == "Tesla")
async def let_tesla_open(message: types.Message):
    await message.delete()
    await message.answer_photo(photo = "https://ibb.co/CBPLRZB", caption = "Name: Tesla Model S\n\nColor: Red\nPrice: $80000\nAuto: Electric\nYear: 2023\nDescription: The Car Of Century\n\nDefine the piece, if you want to buy", reply_markup = send_options)


@router_10.message(F.text == "GM")
async def let_gm_open(message: types.Message):
    await message.delete()
    await message.answer_photo(photo = "https://ibb.co/RCrbk33", caption = "Name: XT4\n\nColor: Blue\nPrice: $75000\nAuto: Automatic\nYear: 2022\nDescription: CONFIDEN\n\nDefine the piece, if you want to buy", reply_markup = send_options)


@router_10.message(F.text.regexp(r"^(\d+)$"))
async def do_no(message: types.Message):
    await message.answer(f"{message.text} is added to basket 🤝")


