import telebot
import time
import random

bot = telebot.TeleBot("805991473:AAH2JCKq9smoHU2uO0hrbZp3jWjk3P1NNrw")
time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
code = random.randint(100000, 999999)
oplata2 = '\n ➖➖➖➖➖➖➖➖➖➖\n🥝 +79397178293\n➖➖➖➖➖➖➖➖➖➖\nКомментарий к платежу:\n💬' + str(code) + ' \n➖➖➖➖➖➖➖➖➖➖\n⏰ Время резерва: 2 мин.\n\nПосле зачисления средств, бот выдаст\nадрес в течении 3-х минут, обычно сразу.\nКоментарий указывать ОБЯЗАТЕЛЬНО.\nОплачивать необходимо ТОЧНУЮ сумму,\nОДНИМ  переводом с QIWI кошелька.\nОплата через терминал - НЕ ПРИНИМАЕТСЯ!!!\nСумма перевода, комментарий и номер\nкошелька -  должны быть ТОЧНЫМИ,\nкак указанно в реквизитах выше,\nиначе бот не выдаст вам адрес и вы потеряете\nсвои деньги.\nБудьте внимательны!'
file_id = "AgADAgAD-qsxG7JjYEqGY7FxLsqwiI_Xtw8ABAEAAwIAA20AA4awBgABFgQ"

keyboard2 = telebot.types.ReplyKeyboardMarkup(True, False)
keyboard2.row('💎Ск-Альфа "Кристалл"')
keyboard2.row('❄️Ск-Альфа Mdpv Мука')
keyboard2.row('💎МЕФ(мяу) КРИСТАЛИЧЕСКИЙ')
keyboard2.row('🍀 Бошки от Антошки Afgan Kush')
keyboard2.row('Вернуться в главное меню↩')

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('🛒Совершить покупку🛒',)
    user_markup.row('💻Кабинет💻','📋Прайс📋', '⁉Помощь⁉')
    user_markup.row('💱Обменник💱')
    bot.send_message(message.from_user.id, 'Привет, ' + message.from_user.first_name + ' \n Рады видеть тебя в нашей аптеке🏥\nТут самые качественные лекарства и низкие цены💊\n➖➖➖➖➖➖➖➖➖➖\n⚠️Что бы не платить деньги фейкам, \n‼️При оплате - сверяйте данные‼️\n👌🏻Актуальные контакты:\n👨‍⚕️Оператор:  👉🏻@Farmacevt007\n➖➖➖➖➖➖➖➖➖➖\nЧто бы перейти к покупке, нажмите на меню ниже 👇🏻', reply_markup=user_markup)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('🛒Совершить покупку🛒', )
    user_markup.row('💻Кабинет💻', '📋Прайс📋', '⁉Помощь⁉')
    user_markup.row('💱Обменник💱')
    if message.text == '💻Кабинет💻':
        bot.send_message(message.chat.id, "Ваши данные:\n" + "Ваше имя: " + message.chat.first_name + "\nВаш юзернейм: " + "@" +message.chat.username + "\nВаши покупки: 0")
    if message.text == '⁉Помощь⁉':
        bot.send_message(message.chat.id, "ПРАВИЛА ПРОВЕДЕНИЯ ОПЛАТЫ: \n ➖➖➖➖➖➖➖➖➖➖ \n ⭕️ Производить оплату нужно строго с QIWI кошелька на QIWI кошелёк \n⭕️ Оплата с терминала не принимается. Если Вы оплатите с терминала, вы потеряете свои деньги. \n⭕️ Оплачивать нужно точно такую же сумму, что указана в реквизитах. Если сумма оплаты будет меньше суммы стоимости товара, Вы не получите адрес, а деньги не будут возвращены.\n⭕️ Оплачивать товар нужно с комментарием, который указан в реквизитах. При вводе комментария, будьте особо внимательны! Если Вы введёте не верный комментарий, бот не увидит Ваш платёж и Вы потеряете свои деньги.\n⭕️ Оплачивать товар необходимо за тот  промежуток времени, что указан в реквизитах. Если Вы произведёте оплату позже указанного времени, Вы  потеряете свои деньги.\n➖➖➖➖➖➖➖➖➖➖\n⚠️Если так получилось, что средства не зачислились на счёт, а вы реально произвели оплату, напишите оперетору поддержки клиентов. Будьте готовы предоставить оператору чек об оплате по QIWI и номер заказа" )
        bot.send_message(message.chat.id, "‼️ ПРАВИЛА ПОДАЧИ ЗАЯВКИ НА  ПЕРЕЗАКЛАД‼️\n➖➖➖➖➖➖➖➖➖➖\n‼️ Заявка на перезаклад пишется ОДНИМ сообщением:\n✅ Номер заказа🔜\n✅ Время покупки🔜\n✅ Ваш id (можно посмотреть в личном кабинете)🔜\n✅ Город и наименование товара🔜\n✅ Подробное описание ситуации (почему не нашли)🔜 \n✅ Фото с места клада (не менее двух)🔜\n✅ Количество покупок в боте🔜\n⏰ Время рассмотрения заявки от 5 минуд до 48 часов🔜\n➖➖➖➖➖➖➖➖➖➖\n🆘 Важно 🆘\n‼️ Причины, по которым вам откажут в перезакладе:\n❌ Перезаклад перезаклада🔜\n❌ Подача заявки по истечению 3-х часов🔜\n❌ Фото не соответствующие фото заказа (отсутствие фото, не чёткое фото)🔜\n❌ Невнятное объяснение ситуации или её отсутствие🔜\n❌ Неадекватное поведение в сторону операторов (угрозы, оскорбления и т.д.)🔜\n❌ Менее 5 покупок в боте с одного аккаунта🔜\n⛔️ Не пытайтесь обмануть оператора. Частые заявки на перезвклад, приравниваются к попытке обмана.🔜\n🚷 Попытался обмануть оператора - получил бан🔜")
    if message.text == '💱Обменник💱':
        bot.send_message(message.chat.id, "bestchange.ru")
    if message.text == '📋Прайс📋':
        bot.send_message(message.chat.id, '📋Прайс:  \n\n💎Ск-Альфа "Кристалл"   -  0.5г 1100р  - 1г  1600р\n\n❄️Ск-Альфа Mdpv Мука  -  0.5 1100р    - 1г 1600р\n\n💎МЕФ(мяу) КРИСТАЛИЧЕСКИЙ  - 1г 1500р\n\n🍀 Бошки от Антошки Afgan Kush - 1г 1200р - 2г 2200р')
    if message.text == '🛒Совершить покупку🛒':
        keyboard1 = telebot.types.ReplyKeyboardMarkup(True, False)
        if message.text == '🛒Совершить покупку🛒':
            keyboard1 = telebot.types.ReplyKeyboardMarkup(True, False)
            keyboard1.row('Самара', 'Тольятти', 'Нижний Новогород')
            keyboard1.row('Арзамас', 'Казань', 'Ульяновск')
            keyboard1.row('СПБ', 'Москва', 'Ярославль')
            keyboard1.row('Владивосток', 'Краснодар', 'Сочи')
            keyboard1.row('Ростов на Дону')
            keyboard1.row('Вернуться в главное меню↩')
        bot.send_message(message.chat.id, '🏠Выберите город⤵', reply_markup=keyboard1)
    if message.text == 'Вернуться в главное меню↩':
        bot.send_message(message.chat.id, message.from_user.first_name + ', вы находитесь в главном меню. Что бы приобрести товар, нажмите кнопку совершить покупку', reply_markup=user_markup)
    if message.text == 'Самара':
        bot.send_message(message.chat.id, '🎁Выберете товар👇🏻', reply_markup=keyboard2)
    if message.text == 'Тольятти':
        bot.send_message(message.chat.id, '🎁Выберете товар👇🏻', reply_markup=keyboard2)
    if message.text == 'Нижний Новогород':
        bot.send_message(message.chat.id, '🎁Выберете товар👇🏻', reply_markup=keyboard2)
    if message.text == 'Арзамас':
        bot.send_message(message.chat.id, '🎁Выберете товар👇🏻', reply_markup=keyboard2)
    if message.text == 'Казань':
        bot.send_message(message.chat.id, '🎁Выберете товар👇🏻', reply_markup=keyboard2)
    if message.text == 'Ульяновск':
        bot.send_message(message.chat.id, '🎁Выберете товар👇🏻', reply_markup=keyboard2)
    if message.text == 'СПБ':
        bot.send_message(message.chat.id, '🎁Выберете товар👇🏻', reply_markup=keyboard2)
    if message.text == 'Москва':
        bot.send_message(message.chat.id, '🎁Выберете товар👇🏻', reply_markup=keyboard2)
    if message.text == 'Ярославль':
        bot.send_message(message.chat.id, '🎁Выберете товар👇🏻', reply_markup=keyboard2)
    if message.text == 'Владивосток':
        bot.send_message(message.chat.id, '🎁Выберете товар👇🏻', reply_markup=keyboard2)
    if message.text == 'Краснодар':
        bot.send_message(message.chat.id, '🎁Выберете товар👇🏻', reply_markup=keyboard2)
    if message.text == 'Сочи':
        bot.send_message(message.chat.id, '🎁Выберете товар👇🏻', reply_markup=keyboard2)
    if message.text == 'Ростов на Дону':
        bot.send_message(message.chat.id, '🎁Выберете товар👇🏻', reply_markup=keyboard2)
    if message.text == '💎Ск-Альфа "Кристалл"':
        price1 = telebot.types.ReplyKeyboardMarkup(True, False)
        price1.row('🎁0.5г 💸1100р')
        price1.row('🎁1г 💸1600р')
        price1.row('Вернуться в главное меню↩')
        bot.send_message(message.chat.id, '🎁Выберите цену товара👇🏻', reply_markup=price1)
    if message.text == '❄️Ск-Альфа Mdpv Мука':
        price1 = telebot.types.ReplyKeyboardMarkup(True, False)
        price1.row('🎁0.5г 💸1100р')
        price1.row('🎁1г 💸1600р')
        price1.row('Вернуться в главное меню↩')
        bot.send_message(message.chat.id, '🎁Выберите цену товара👇🏻', reply_markup=price1)
    if message.text == '💎МЕФ(мяу) КРИСТАЛИЧЕСКИЙ':
        price1 = telebot.types.ReplyKeyboardMarkup(True, False)
        price1.row('🎁1г 💸1500р')
        price1.row('Вернуться в главное меню↩')
        bot.send_message(message.chat.id, '🎁Выберите цену товара👇🏻', reply_markup=price1)
    if message.text == '🍀 Бошки от Антошки Afgan Kush':
        price1 = telebot.types.ReplyKeyboardMarkup(True, False)
        price1.row('🎁1г 💸1200р')
        price1.row('🎁2г 💸2200р')
        price1.row('Вернуться в главное меню↩')
        bot.send_message(message.chat.id, '🎁Выберите цену товара👇🏻', reply_markup=price1)
    if message.text == '🎁0.5г 💸1100р':
        price1 = telebot.types.ReplyKeyboardMarkup(True, False)
        price1.row('✅Проверить оплату✅')
        price1.row('🚫Отменить покупку🚫')
        ves = "0.5г"
        price = "1100"
        oplata = '\n🎁 Товар: ' + ves + '\n💵 Цена: ' + price + '₽\n ➖➖➖➖➖➖➖➖➖➖\n📆 Дата: ' + time + '\n👉 Оплатите ' + price + ' руб. на Qiwi кошелек:'
        bot.send_photo(message.chat.id, file_id)
        bot.send_message(message.chat.id, oplata + oplata2, reply_markup=price1)
    if message.text == '🎁1г 💸1600р':
        price1 = telebot.types.ReplyKeyboardMarkup(True, False)
        price1.row('✅Проверить оплату✅')
        price1.row('🚫Отменить покупку🚫')
        ves = "1г"
        price = "1600"
        oplata = '\n🎁 Товар: ' + ves + '\n💵 Цена: ' + price + '₽\n ➖➖➖➖➖➖➖➖➖➖\n📆 Дата: ' + time + '\n👉 Оплатите ' + price + ' руб. на Qiwi кошелек:'
        bot.send_photo(message.chat.id, file_id)
        bot.send_message(message.chat.id, oplata + oplata2, reply_markup=price1)
    if message.text == '🎁1г 💸1500р':
        price1 = telebot.types.ReplyKeyboardMarkup(True, False)
        price1.row('✅Проверить оплату✅')
        price1.row('🚫Отменить покупку🚫')
        ves = "1г"
        price = "1500"
        oplata = '\n🎁 Товар: ' + ves + '\n💵 Цена: ' + price + '₽\n ➖➖➖➖➖➖➖➖➖➖\n📆 Дата: ' + time + '\n👉 Оплатите ' + price + ' руб. на Qiwi кошелек:'
        bot.send_photo(message.chat.id, file_id)
        bot.send_message(message.chat.id, oplata + oplata2, reply_markup=price1)
    if message.text == '🎁1г 💸1200р':
        price1 = telebot.types.ReplyKeyboardMarkup(True, False)
        price1.row('✅Проверить оплату✅')
        price1.row('🚫Отменить покупку🚫')
        ves = "1г"
        price = "1200"
        oplata = '\n🎁 Товар: ' + ves + '\n💵 Цена: ' + price + '₽\n ➖➖➖➖➖➖➖➖➖➖\n📆 Дата: ' + time + '\n👉 Оплатите ' + price + ' руб. на Qiwi кошелек:'
        bot.send_photo(message.chat.id, file_id)
        bot.send_message(message.chat.id, oplata + oplata2, reply_markup=price1)
    if message.text == '🎁2г 💸2200р':
        price1 = telebot.types.ReplyKeyboardMarkup(True, False)
        price1.row('✅Проверить оплату✅')
        price1.row('🚫Отменить покупку🚫')
        ves = "2г"
        price = "2200"
        oplata = '\n🎁 Товар: ' + ves + '\n💵 Цена: ' + price + '₽\n ➖➖➖➖➖➖➖➖➖➖\n📆 Дата: ' + time + '\n👉 Оплатите ' + price + ' руб. на Qiwi кошелек:'
        bot.send_photo(message.chat.id, file_id)
        bot.send_message(message.chat.id, oplata + oplata2, reply_markup=price1)
    if message.text == '✅Проверить оплату✅':
        bot.send_message(message.chat.id, '🚫Прошло более 2 минут или же вы не оплатили товар🚫', reply_markup=user_markup)
        bot.send_message(message.chat.id, message.from_user.first_name + ', вы находитесь в главном меню. Что бы приобрести товар, нажмите кнопку совершить покупку')
    if message.text == '🚫Отменить покупку🚫':
        bot.send_message(message.chat.id, '🚫Отмена заказа🚫', reply_markup=user_markup)
        bot.send_message(message.chat.id, message.from_user.first_name + ', вы находитесь в главном меню. Что бы приобрести товар, нажмите кнопку совершить покупку')

bot.polling(none_stop=True, interval=0)