from aiogram import Router, F, types
from button import get_foods, send_options


router_9 = Router()


@router_9.message(F.text == "🍔 Food")
async def let_foods_open(message: types.Message):
    await message.answer("It's just cheaper and better", reply_markup = get_foods())


@router_9.message(F.text == "🍔 Burger")
async def let_burger_open(message: types.Message):
    await message.delete()
    await message.answer_photo(photo = "https://ibb.co/fCxdk9s", caption = "Name: Burger\n\nAdded: Onion, Herb, Mayonnaise, Thin Potato and Beef Cutlet\nPrice: $10\nDescription: Big Burger\n\nDefine the piece, if you want to buy", reply_markup = send_options)


@router_9.message(F.text == "🍕 Pizza")
async def let_pizza_open(message: types.Message):
    await message.delete()
    await message.answer_photo(photo = "https://ibb.co/4gf42Nf", caption = "Name: Pizza\n\nAdded: Bulgarian, Bitter, Cheese, Onion and Bread\nPrice: $50\nDescription: Italian Pizza\n\nDefine the piece, if you want to buy", reply_markup = send_options)


@router_9.message(F.text == "🌭 Hot-Dog")
async def let_hotdog_open(message: types.Message):
    await message.delete()
    await message.answer_photo(photo = "https://ibb.co/XZMQ9gR", caption = "Name: HotDog\n\nAdded: Sousage, Yellow Mayonnaise and Bread\nPrice: $6\nDescription: Orginal HotDog\n\nDefine the piece, if you want to buy", reply_markup = send_options)


@router_9.message(F.text.regexp(r"^(\d+)$"))
async def do_no(message: types.Message):
    await message.answer(f"{message.text} is added to basket 🤝")
