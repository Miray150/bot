from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config_ import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
# Регистрация обработчика для всех текстовых сообщений используя декоратор
@dp.message_handler()
async def echo_message(msg: types.Message): #асинхронная функиция для пересылки сообщения
    #msg - обьект сообщения который содержит данные о полученном сообщении и его отприавление
    await bot.forward_message(msg.from_user.id, msg.from_user.id, msg.message_id)
    #msg.from_user.id - уникальный индификатор пользователя отправляющего сообщение


if __name__ == "__main__":
    executor.start_polling(dp)