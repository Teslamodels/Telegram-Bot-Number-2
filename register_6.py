from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from state import RegisterState
from button import get_products


router_6 = Router()


@router_6.callback_query(F.data == '✅ accept', RegisterState.confirm)
async def choose_accept(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    print(data)
    await call.message.delete()
    await call.message.answer("😎 accepted", reply_markup = get_products())
    await call.message.answer("If you want to buy foods, phone or cars, put button that in the below")
    await state.clear()
