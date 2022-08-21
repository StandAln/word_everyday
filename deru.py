#import telethon,shedule,random
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon import TelegramClient, sync, events
import schedule, time
import random

#api_id-id приложения (сессии) telegram,api_hash-hash приложения (сессии) telegram - получаем после создания приложения на https://my.telegram.org/apps
#message-отправляемое сообщение,user_id-telegram user_id получателя,access_hash-telegram hash получателя - можно получить используя print(client.get_entity('phone'))
api_id = 'XXX'
api_hash = 'XXX'
user_id=XXX
access_hash=XXX

# Создаем telegram сессию с нашими данными из API,имя любое (но постоянное)
client = TelegramClient('session_deutsch', api_id, api_hash)

#Объявляем получателя
receiver = InputPeerUser(user_id, access_hash)

#Открываем файл с словами,выбираем рандомное, и удаляем его из списка,перезаписывая файл
def get_word():
    dictionary = "./matveev.txt"
    with open(dictionary, "r+", encoding="utf-8") as input_dict:  
        words=input_dict.read().splitlines()
        wordoftheday=random.choice(words)
        input_dict.seek(0)
            
        for line in words:
            if wordoftheday not in line:
                input_dict.write(line+'\n')
        input_dict.truncate()
    message='Привет! Новое слово дня:\n🇩🇪🇩🇪\n{}\n🇩🇪🇩🇪'.format(wordoftheday)
    return message

#Функция отправки сообщения
def send_mess(message):
# Запуск сессии
    client.start()
# Отправляем сообщение
    client.send_message(receiver, message, parse_mode='html')
# Закрытие сессии
    client.disconnect()

#общая функция
def job():
    send_mess(get_word())

#Отправка сообщения по расписанию
schedule.every().day.at("09:32").do(job) 

#Цикл отсчёта времени для расписания
while True: 
    schedule.run_pending()
    time.sleep(1)