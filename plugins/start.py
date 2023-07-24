from pyrogram import Client, filters
from pyrogram import enums
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery


@Client.on_message(filters.command('start'))
async def start(client: Client, message: Message):
    await message.reply_chat_action(enums.ChatAction.UPLOAD_PHOTO)
    await message.reply_photo(
        'https://i.ibb.co/2FgQqwV/gaefswre.jpg',
        caption=f'Username : @{message.from_user.username}\nUserID : `{message.from_user.id}`\nLanguage : {message.from_user.language_code}',
        reply_markup=InlineKeyboardMarkup(
        [
            [
                                InlineKeyboardButton(text=f'{message.from_user.first_name}',
                                                     callback_data='first_name'),
                                InlineKeyboardButton(text='Github',
                                                     url='https://github.com/RealCuf')
            ],
        ]))


@Client.on_message(filters.command('userid'))
async def chatid(client: Client, message: Message):
    await message.reply_chat_action(enums.ChatAction.TYPING)
    await message.reply_text(
        f'Your UserID is :\n**{message.from_user.id}**\n\nUserIDs normally dont change, but you can ask me at any time with /userid what your current UserID is :)')