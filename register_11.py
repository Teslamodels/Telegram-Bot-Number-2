from aiogram import Router, F, types
from button import how_many


router_11 = Router()


@router_11.callback_query(F.data == "positive")
async def be_positive(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Ok, how much do you want?", reply_markup = how_many())


@router_11.callback_query(F.data == "negative")
async def dont_be_negative(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("The Product is successfully canceled 👍")


 
