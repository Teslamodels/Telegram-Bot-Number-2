from aiogram import Router, F, types
from button import get_products


router_12 = Router()


@router_12.message(F.text == "⬅️ Back")
async def let_it_open(message: types.Message):
    await message.answer("Please, choose the page 😊", reply_markup = get_products())

