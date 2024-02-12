import telebot
from telebot import types
from datetime import datetime, timedelta
import random
import string
# Задаем токен для доступа к API бота
TOKEN = '5906387883:AAHquBg_WAMZGsqy7rubswZkqYejusxlLj0'
# Создаем экземпляр бота
bot = telebot.TeleBot(TOKEN)
admins = ['923617531', '253797531']
reports = []  # Переменная для хранения жалоб
# Создаем список вопросов и ответов
questions = [
    {
        'question': 'Годы правления Рюрика?',
        'answer': '862-879'
    },
    {
        'question': 'Чьи годы правления 862-879',
        'answer': 'Рюрик'
    },
    {
        'question': 'Годы правления Олега',
        'answer': '879-912'
    },
    {
        'question': 'Чьи годы правления - 879-912',
        'answer': 'Олег'
    },
    {
        'question': 'Годы правления Игоря',
        'answer': '912-945'
    },
    {
        'question': 'Чьи годы правления 912-945',
        'answer': 'Игорь'
    }, 
    {
        'question': 'Годы правления Ольги ',
        'answer': '945-964'
    },
    {
        'question': 'Чьи годы правления 945-964',
        'answer': 'Ольга'
    },
    {
        'question': 'Годы правления Святослава?',
        'answer': '964-972'
    },
    {
        'question': 'Чьи годы правления - 964-972',
        'answer': 'Святослав'
    },
    {
        'question': 'Годы правления Ярополка',
        'answer': '972-980'
    },
    {
        'question': 'Чьи годы правления 972-980',
        'answer': 'Ярополк'
    },
    {
        'question': 'Годы правления Владимира Красное солнышко',
        'answer': '980-1015'
    },
    {
        'question': 'Чьи годы правления 980-1015',
        'answer': 'Владимира Красное Солнышко'
    },
    {
        'question': 'Годы правление чьи Святополка Окаянного',
        'answer': '1015-1019'
    },
    {
        'question': 'Чьи годы правления 1015-1019',
        'answer': 'Святополка Окаянного'
    },
    {
        'question': 'Годы правления Ярослава Мудрого',
        'answer': '1019-1054'
    },
    {
        'question': 'Чьи годы правления 1019-1054',
        'answer': 'Ярослав мудрый'
    }, 
    {
        'question': 'Годы правления Владимира Мономаха',
        'answer': '1113-1125'
    },
    {
        'question': 'Чьи годы правления 1113-1125',
        'answer': 'Владимир Мономаха'
    },
    {
        'question': 'Годы правления Юрия долгорукого',
        'answer': '1125-1157'
    },
    {
        'question': 'Чьи годы правления - 1125-1157',
        'answer': 'Юрий долгорукий'
    },
    {
        'question': 'Годы правления Андрея Боголюбского',
        'answer': '1157-1174'
    },
    {
        'question': 'Чьи годы правления 1157-1174',
        'answer': 'Андрей Боголюбский'
    },
    {
        'question': 'Годы правления Всеволода Большое Гнездо',
        'answer': '1176-1212'
    },
    {
        'question': 'Чьи годы правления 1176 - 1212',
        'answer': 'Всеволод Большое Гнездо'
    },
    {
        'question': 'Годы правления Юрия Всеволодовича',
        'answer': '1218-1238'
    },
    {
        'question': 'Чьи годы правления 1218-1238',
        'answer': 'Юрий Всеволодович'
    },
    {
        'question': 'Годы правления Даниила Александровича',
        'answer': '1276-1303'
    },
    {
        'question': 'Чьи годы правления 1276-1303',
        'answer': 'Даниил Александрович '
    }, 
    {
        'question': 'Годы правления  Юрия Даниловича',
        'answer': '1303-1325'
    },
    {
        'question': 'Чьи годы правления 1303-1325',
        'answer': 'Юрий Данилович'
    },
    {
        'question': 'Чьи годы правления 1325-1340',
        'answer': 'Иван Калита'
    },
    {
        'question': 'Годы правления - Симеон гордый',
        'answer': '1340-1353'
    },
    {
        'question': 'Годы правления Ивана Красного',
        'answer': '1353-1359'
    },
    {
        'question': 'Чьи годы правления 1353-1359',
        'answer': 'Иван Красный'
    },
    {
        'question': 'Годы правления Дмитрий Донской',
        'answer': '1359-1389'
    },
    {
        'question': 'Чьи годы правления 1359-1389',
        'answer': 'Дмитрий Донской'
    },
    {
        'question': 'Годы правления Василия Первого',
        'answer': '1389-1325'
    },
    {
        'question': 'Чьи годы правления 1389-1425',
        'answer': 'Василий Первый'
    },
    {
        'question': 'Годы правления Василия второго',
        'answer': '1425-1462'
    },
    {
        'question': 'Чьи годы правления 1425-1462',
        'answer': 'Василий Второй'
    }, 
    {
        'question': 'Годы правления Василия третьего',
        'answer': '1505-1533'
    },
    {
        'question': 'Чьи годы правления 1505-1533',
        'answer': 'Василий третий'
    },
    {
        'question': 'Годы правления Ивана Грозного',
        'answer': '1533-1584'
    },
    {
        'question': 'Чьи годы правления 1533-1584',
        'answer': 'Елена Глинская'
    },
    {
        'question': 'Годы регенства Елены Глинской',
        'answer': '1533-1538'
    },
    {
        'question': 'Чьи годы правления 1533-1538',
        'answer': 'Елена Глинская'
    }, 
    {
        'question': 'Годы правления Фёдора Ивановича',
        'answer': '1584-1598'
    },
    {
        'question': 'Чьи годы правления 1584-1598',
        'answer': 'Федор Иванович'
    },
    {
        'question': 'Годы правления Бориса Годунова',
        'answer': '1598-1605'
    },
    {
        'question': 'Чьи годы правления 1598-1605',
        'answer': 'Борис Годунов'
    },
    {
        'question': 'Годы правления Лжедмитрия первого',
        'answer': '1605-1606'
    },
    {
        'question': 'Чьи годы правления 1605-1606',
        'answer': 'Лжедмитрий первый'
    }, 
    {
        'question': 'Годы правления Василия Шуйского',
        'answer': '1606-1610'
    },
    {
        'question': 'Чьи годы правления 1606-1610',
        'answer': 'Василий Шуйский'
    },
    {
        'question': 'Годы Семибоярщины',
        'answer': '1610-1612'
    },
    {
        'question': 'Чьи годы правления 1610-1612',
        'answer': 'Семибоярщина'
    },
    {
        'question': 'Годы правления Михаила Федоровича Романова',
        'answer': '1613-1645'
    },
    {
        'question': 'Чьи годы правления 1613-1645',
        'answer': 'Михаил Романов'
    },
    {
        'question': 'Годы правления Алексея Михайловича',
        'answer': '1645-1676'
    },
    {
        'question': 'Чьи Годы правления 1645-1676',
        'answer': 'Алексей Михайлович'
    },
    {
        'question': 'Годы правления Федора Алексеевича',
        'answer': '1676-1682'
    },
    {
        'question': 'Чьи годы правления 1676-1682',
        'answer': 'Федор Алексеевич'
    },
    {
        'question': 'Годы правления царевны Софьи',
        'answer': '1682-1689'
    },
    {
        'question': 'Чьи годы правления 1682-1689',
        'answer': 'царевна Софья'
    }, 
    {
        'question': 'Годы правления Петра первого',
        'answer': '1682-1725'
    },
    {
        'question': 'Чьи годы правления 1682-1725',
        'answer': 'Петр Первый'
    },
    {
        'question': 'Годы правления Екатерины первой',
        'answer': '1725-1727'
    },
    {
        'question': 'Чьи годы правления - 1725-1727',
        'answer': 'Екатирина первая'
    },
    {
        'question': 'Годы правления Петр Второй',
        'answer': '1727-1730'
    },
    {
        'question': 'Чьи годы правления 1727-1730',
        'answer': 'Петр второй'
    },
    {
        'question': 'Годы правления Анна Иоанновна',
        'answer': '1730-1740'
    },
    {
        'question': 'Чьи годы правления 1730-1740',
        'answer': 'Анна Иоанновна'
    },
    {
        'question': 'Годы правления Ивана Антоновича',
        'answer': '1740-1741'
    },
    {
        'question': 'Чьи годы правления 1740-1741',
        'answer': 'Иван Антонович'
    },
    {
        'question': 'Годы правления Елизаветы Первой',
        'answer': '1741-1761'
    },
    {
        'question': 'Чьи годы правления 1741-1761',
        'answer': 'Елизавета первая '
    }, 
    {
        'question': 'Годы правления Петра третьего',
        'answer': '1761-1762'
    },
    {
        'question': 'Чьи годы правление 1761-1762',
        'answer': 'Петр третий'
    },
    {
        'question': 'Годы правления Екатерины второй',
        'answer': '1762-1796'
    },
    {
        'question': 'Чьи годы правления - 1762-1796',
        'answer': 'Екатерина Вторая'
    },
    {
        'question': 'Годы правления Павла первого',
        'answer': '1796-1801'
    },
    {
        'question': 'Чьи годы правления 1796-1801',
        'answer': 'Павел первый'
    },
    {
        'question': 'Годы правления Александра первого',
        'answer': '1801-1825'
    },
    {
        'question': 'Чьи годы правления 1801-1825',
        'answer': 'Александр Первый'
    },
    {
        'question': 'Годы правления Николая первого',
        'answer': '1825-1855'
    },
    {
        'question': 'Чьи годы правления 1825-1855',
        'answer': 'Николай первый'
    },
    {
        'question': 'Годы правления Александра второго',
        'answer': '1855-1881'
    },
    {
        'question': 'Чьи годы правления 1855-1881',
        'answer': 'Александр второй'
    }, 
    {
        'question': 'Годы правления Александра третьего',
        'answer': '1881-1894'
    },
    {
        'question': 'Чьи годы правления 1881-1894',
        'answer': 'Александр третий'
    },
    {
        'question': 'Годы правления Николая второго',
        'answer': '1894-1917'
    },
    {
        'question': 'Чьи годы правления 1894-1917',
        'answer': 'Николай второй'
    },
    {
        'question': 'Годы управления Владимира Ильича Ленина',
        'answer': '1917-1924'
    },
    {
        'question': 'Чьи годы управления 1917-1924',
        'answer': 'Владимир Ленин'
    }, 
    {
        'question': 'Годы управления Иосифа Виссарионовича Сталина',
        'answer': '1922-1953'
    },
    {
        'question': 'Чьи годы управления 1922-1953',
        'answer': 'Иосиф Сталин'
    },
    {
        'question': 'Годы управления Ниикты Сергеевича Хрущёва.',
        'answer': '1953-1964'
    },
    {
        'question': 'Чьи годы управления 1953-1964',
        'answer': 'Никита Сергеевич Хрущёв'
    },
    {
        'question': 'Годы управления Леонида Ильича Брежнева',
        'answer': '1964-1982'
    },
    {
        'question': 'Чьи годы управления 1964-1982',
        'answer': 'Леонид Брежнев'
    },
    {
        'question': 'Годы управления Юрия Владимировича Андропова',
        'answer': '1982-1984'
    }, 
    {
        'question': 'Чьи годы управления 1982-1984',
        'answer': 'Юрий Андропов'
    },
    {
        'question': 'Годы управления Константина Устиновича Черненко',
        'answer': '1984-1985'
    },
    {
        'question': 'Чьи годы управления 1984-1985',
        'answer': 'Константин Черненко'
    },
    {
        'question': 'Годы управления Михаила Сергеевича Горбачева',
        'answer': '1985-1991'
    },
    {
        'question': 'Чьи годы управления 1985-1991',
        'answer': 'Михаил Горбачев'
    },
    {
        'question': 'Годы управления Бориса Николаевича Ельцина',
        'answer': '1991-2000'
    },
    {
        'question': 'Чьи годы управления 1991-2000',
        'answer': 'Борис Ельцин'
    },
    {
        'question': 'Годы управления Владимира Владимировича Путина (1 срок)',
        'answer': '2000-2008'
    },
    {
        'question': 'Чьи годы управления 2000-2008',
        'answer': 'Владимир Путин'
    },
    {
        'question': 'Годы управления Дмитрия Анатольевича Медведева',
        'answer': '2008-2012'
    },
    {
        'question': 'Чьи годы управления 2008-2012',
        'answer': 'Дмитрий Медведев'
    },
    {
        'question': 'Годы управления Владимира Владимировича Путина (2 срок)',
        'answer': '2012-2018'
    }, 
    {
        'question': 'Чьи годы управления сейчас?',
        'answer': 'Владимир Путин'
    },                                        
]

# Переменная для хранения текущего вопроса
current_question = None
# Переменная для хранения оставшихся попыток
remaining_attempts = 2
# Словарь для хранения статистики пользователей
user_stats = {}

# Словарь для хранения статистики использования бота
usage_stats = {
    'daily': 0,
    'answered_all_questions': 0
}

# Создаем объект ReplyKeyboardMarkup
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

# Создаем кнопку для статистики
stats_btn = types.KeyboardButton('/stats')
stats_btn.text = '/stats'  # Изменяем текст кнопки
stats_btn.callback_data = '/stats'  # Устанавливаем callback_data 

# Создаем кнопку для статистики
report_btn = types.KeyboardButton('/report')
report_btn.text = '/report'  # Изменяем текст кнопки
report_btn.callback_data = '/report'  # Устанавливаем callback_data 

# Добавляем кнопку в разметку
markup.add(stats_btn)
markup.add(report_btn)

@bot.message_handler(commands=['start'])
def send_question(message):
    # Увеличиваем счетчик использования бота за сутки
    usage_stats['daily'] += 1
    bot.reply_to(message, 'Привет! Я бот, который может проверить ваши знания по истории.', reply_markup=markup)
    global current_question, remaining_attempts
    try:
        # Выбираем случайный вопрос
        current_question = random.choice(questions)
        # Отправляем текущий вопрос
        bot.reply_to(message, f"Первый ваш вопрос: {current_question['question']}")
        # Сбрасываем количество оставшихся попыток
        remaining_attempts = 2                                           
    except IndexError:
        bot.reply_to(message, 'Произошла ошибка. Пожалуйста попробуйте снова /start')

@bot.message_handler(commands=['broadcast'])
def broadcast_message(message):
    if str(message.from_user.id) in admins:
        markup = types.ForceReply(selective=False)
        bot.reply_to(message, 'Введите текст рассылки:', reply_markup=markup)
        bot.register_next_step_handler(message, process_broadcast_step)
    else:
        bot.reply_to(message, 'Вы не являетесь администратором.')

def process_broadcast_step(message):
    text = message.text
    for user in user_stats.keys():
        bot.send_message(user, text)
    bot.send_message(message.from_user.id, text)

# Обработчик команды /activite
@bot.message_handler(commands=['activite'])
def activite(message):
 if str(message.from_user.id) in admins:

    today = datetime.now().date()
    week_ago = today - timedelta(days=7)
    month_ago = today - timedelta(days=30)
 
    daily_usage = usage_stats['daily']
    answered_all_questions = usage_stats['answered_all_questions']
    
    bot.send_message(message.chat.id, f"Статистика использования бота:\n"
                                      f"За всё время: {daily_usage}\n"
                                      f"Пользователей ответивших на все вопросы: {answered_all_questions}")
 else:
    bot.reply_to(message, 'Вы не являетесь администратором.')  

@bot.message_handler(commands=['report'])
def report_issue(message):
    markup = types.ForceReply(selective=False)
    bot.reply_to(message, 'Опишите проблему:', reply_markup=markup)
    bot.register_next_step_handler(message, process_report_step)

def process_report_step(message):
    report_id = generate_report_id()
    user_id = message.from_user.id
    issue_description = message.text
    report = {'id': report_id, 'user_id': user_id, 'issue_description': issue_description}
    # Добавить жалобу в переменную reports
    reports.append(report)
    bot.send_message(user_id, f'Ваша жалоба была зарегистрирована под номером {report_id}. Мы рассмотрим её в ближайшее время.')

    # Отправить сообщение администраторам о поступлении жалобы
    for admin_id in admins:
        bot.send_message(admin_id, f'Поступила жалоба. Идентификатор: {report_id}.')
        bot.send_message(admin_id, '/ask')

def generate_report_id():
    # Генерировать уникальный идентификатор для жалобы
    return ''.join(random.choices(string.digits, k=5))

@bot.message_handler(commands=['ask'])
def ask_admin(message):
    if str(message.from_user.id) in admins:
        if reports:
            markup = types.InlineKeyboardMarkup()
            for report in reports:
                report_btn = types.InlineKeyboardButton(text=f'Жалоба #{report["id"]}', callback_data=f'report_{report["id"]}')
                markup.add(report_btn)
            bot.reply_to(message, 'Выберите жалобу для ответа:', reply_markup=markup)
        else:
            bot.reply_to(message, 'Нет открытых жалоб.')
    else:
        bot.reply_to(message, 'Вы не являетесь администратором.')

@bot.callback_query_handler(func=lambda call: call.data.startswith('report_'))
def process_report_selection(call):
    report_id = call.data.split('_')[1]
    report_info = None
    for report in reports:
        if report['id'] == report_id:
            report_info = report
            break

    if report_info:
        user_id = report_info['user_id']
        issue_description = report_info['issue_description']
        markup = types.ForceReply(selective=False)
        bot.send_message(call.message.chat.id, f'Жалоба #{report_id} от пользователя {user_id}:\n{issue_description}\n\nВведите ответ:', reply_markup=markup)
        bot.register_next_step_handler(call.message, lambda message: process_response_to_report(message, user_id, report_id))
    else:
        bot.send_message(call.message.chat.id, f'Жалоба #{report_id} не найдена.')

def process_response_to_report(message, user_id, report_id):
    response_text = message.text
    bot.send_message(user_id, f'Ответ на вашу жалобу #{report_id}:\n{response_text}')
    remove_report_from_reports(report_id)
    bot.send_message(message.chat.id, f'Ответ на жалобу #{report_id} отправлен пользователю.')

def remove_report_from_reports(report_id):
    for report in reports:
        if report['id'] == report_id:
            reports.remove(report)
            break

@bot.message_handler(commands=['stats'])
def show_stats(message):
    if not user_stats:
        bot.reply_to(message, 'Статистика пуста, ответьте пожалуйста на один вопрос чтобы ваша статистика обновилась.')
    else:
        stats_message = 'Статистика:\n'
        for user, stats in user_stats.items():
            stats_message += f'Пользователь: {user}\n' \
                             f'Вопросов отвечено: {stats["answered"]}\n' \
                             f'Вопросов неправильно отвеченных: {stats["skipped"]}\n' \
                             f'---\n'
        bot.reply_to(message, stats_message)

@bot.message_handler(func=lambda message: True)
def check_answer(message):
    global current_question, remaining_attempts
    if current_question is None:
        bot.reply_to(message, 'Пожалуйста, используйте команду /start, чтобы начать проверку ваших знаний.')
        return

    # Получаем ответ пользователя и проверяем его
    user_answer = message.text.lower()
    correct_answer = current_question['answer'].lower()

    if user_answer == correct_answer:
        # Отправляем сообщение о правильном ответе
        bot.reply_to(message, 'Правильно! Вы переходите к следующему вопросу.')

        if len(questions) > 1:
            # Удаляем текущий вопрос из списка вопросов
            questions.remove(current_question)
            # Выбираем следующий случайный вопрос
            current_question = random.choice(questions)
            # Отправляем следующий вопрос
            bot.reply_to(message, f"Следующий вопрос: {current_question['question']}")
            # Сбрасываем количество оставшихся попыток
            remaining_attempts = 2
        else:
            # Все вопросы пройдены
            current_question = None
            bot.reply_to(message, 'Вы ответили на все вопросы. Поздравляю!')
            usage_stats['answered_all_questions'] += 1
 # Обновляем статистику пользоват
        user_id = message.from_user.id
        if user_id in user_stats:
            user_stats[user_id]['answered'] += 1
        else:
            user_stats[user_id] = {'answered': 1, 'skipped': 0}
    else:
        if remaining_attempts > 1:
            # У пользователя осталась хотя бы одна попытка
            bot.reply_to(message, f'Неправильно. У вас осталось {remaining_attempts - 1} попытка.')
            # Уменьшаем количество оставшихся попыток
            remaining_attempts -= 1
        else:
            # У пользователя не осталось попыток
            bot.reply_to(message, f'Неправильно. Правильный ответ: {correct_answer}. Перейдем к следующему вопросу.')

            if len(questions) > 1:
                # Удаляем текущий вопрос из списка вопросов
                questions.remove(current_question)
                # Выбираем следующий случайный вопрос
                current_question = random.choice(questions)
                # Отправляем следующий вопрос
                bot.reply_to(message, f"Следующий вопрос: {current_question['question']}")
                # Сбрасываем количество оставшихся попыток
                remaining_attempts = 2
            else:
                # Все вопросы пройдены
                current_question = None
                bot.reply_to(message, 'Вы ответили на все вопросы. Поздравляю!')
            # Обновляем статистику пользователя
            user_id = message.from_user.id
            if user_id in user_stats:
                user_stats[user_id]['skipped'] += 1
            else:
                user_stats[user_id] = {'answered': 0, 'skipped': 1}

# Запускаем бота
bot.infinity_polling()
