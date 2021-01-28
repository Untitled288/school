from tqdm.auto import tqdm
import vk_api
import sqlite3 as sql
import time
import datetime
import random
import json
 
connection = sql.connect("school.sqlite", check_same_thread=False)
 
q = connection.cursor()
 
q.execute('''CREATE TABLE IF NOT EXISTS user_info
(
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
User_ID INTEGER,
Right_Answers INTEGER,
Question INTEGER,
Answer INTEGER,
Ownment Varchar(100)
)
''')

#New_User INTEGER,----------1
#Right_Answers INTEGER,-----2
#Question INTEGER,----------3
#Answer INTEGER,------------4


connection.commit()
connection.close()

#key - 08e6ca9fdfb207440611316a078057b6aaef7b3b1cacbc4fbaa49cc4b60aaac6da563596fdccf11198dff
# test - 3206cad2b6d1f200d4beb5c7af16d5ac786010363c203ca31184fb0f102bb3b8ee68348b40c6ce824b766

token = "08e6ca9fdfb207440611316a078057b6aaef7b3b1cacbc4fbaa49cc4b60aaac6da563596fdccf11198dff"
 
vk = vk_api.VkApi(token=token)
vk._auth_token()

print("Загрузка локального сервера...")
for i in tqdm(range(15)):
    time.sleep(0.02)

print("Успешно!")
#-------------------------------------------------------------------------------------------
def get_button(label, color, payload=""):
    return {
        "action": {
            "type": "text",
            "payload": json.dumps(payload),
            "label": label
            
        },
        "color": color
    }

menu = {
    "one_time": False,
    "buttons": [
    
    [get_button(label="Играть", color="positive")],
    [get_button(label="Информация", color="default")]
    
    ]
}

menu = json.dumps(menu, ensure_ascii=False).encode('utf-8')
menu = str(menu.decode('utf-8'))

#----------------------------------------------------------

characteristic = {
    "one_time": False,
    "buttons": [
    
    [get_button(label="Раскольников Радион", color="default")],
    [get_button(label="Мармеладов Семён", color="default")],
    [get_button(label="Мармеладова София", color="default")],
    [get_button(label="Алёна Ивановна", color="default")],
    
    ]
}

characteristic = json.dumps(characteristic, ensure_ascii=False).encode('utf-8')
characteristic = str(characteristic.decode('utf-8'))

#----------------------------------------------------------

yes_or_no = {
    "one_time": False,
    "buttons": [
    [
    get_button(label="Да", color="positive"),
    get_button(label="Нет", color="negative")
    ]
    ]
}

yes_or_no = json.dumps(yes_or_no, ensure_ascii=False).encode('utf-8')
yes_or_no = str(yes_or_no.decode('utf-8'))

#----------------------------------------------------------

game1 = {
    "one_time": False,
    "buttons": [
    
    [get_button(label="Наказание и приступление", color="default")],
    [get_button(label="Я не знаю", color="positive")],
    [get_button(label="Преступление и наказание", color="default")],
    [get_button(label="Вернуться в меню", color="primary")]
    
    ]
}

game1 = json.dumps(game1, ensure_ascii=False).encode('utf-8')
game1 = str(game1.decode('utf-8'))

#----------------------------------------------------------

game2 = {
    "one_time": False,
    "buttons": [
    
    [get_button(label="Фёдор Достоевский", color="default")],
    [get_button(label="Александр Пушкин", color="positive")],
    [get_button(label="Грета Тумберг", color="default")],
    [get_button(label="Вернуться в меню", color="primary")]
    
    ]
}

game2 = json.dumps(game2, ensure_ascii=False).encode('utf-8')
game2 = str(game2.decode('utf-8'))

#----------------------------------------------------------

game3 = {
    "one_time": False,
    "buttons": [
    
    [get_button(label="Радион Раскольников", color="default")],
    [get_button(label="Родион Раскольников", color="positive")],
    [get_button(label="Радион Роскольников", color="default")],
    [get_button(label="Вернуться в меню", color="primary")]
    
    ]
}

game3 = json.dumps(game3, ensure_ascii=False).encode('utf-8')
game3 = str(game3.decode('utf-8'))

#----------------------------------------------------------

game4 = {
    "one_time": False,
    "buttons": [
    
    [get_button(label="Иван Мармеладов", color="default")],
    [get_button(label="Семён Мармеладов", color="positive")],
    [get_button(label="Александр Мармеладов", color="default")],
    [get_button(label="Вернуться в меню", color="primary")]
    
    ]
}

game4 = json.dumps(game4, ensure_ascii=False).encode('utf-8')
game4 = str(game4.decode('utf-8'))

#----------------------------------------------------------

game5 = {
    "one_time": False,
    "buttons": [
    
    [get_button(label="1874", color="default")],
    [get_button(label="1846", color="positive")],
    [get_button(label="1866", color="default")],
    [get_button(label="Вернуться в меню", color="primary")]
    
    ]
}

game5 = json.dumps(game5, ensure_ascii=False).encode('utf-8')
game5 = str(game5.decode('utf-8'))

#----------------------------------------------------------

game6 = {
    "one_time": False,
    "buttons": [
    
    [get_button(label="Мрачность", color="default")],
    [get_button(label="Страх", color="positive")],
    [get_button(label="Шизофренизм", color="default")],
    [get_button(label="Радость", color="positive")],
    [get_button(label="Вернуться в меню", color="primary")]
    
    ]
}

game6 = json.dumps(game6, ensure_ascii=False).encode('utf-8')
game6 = str(game6.decode('utf-8'))

#----------------------------------------------------------

game7 = {
    "one_time": False,
    "buttons": [
    
    [get_button(label="Дворник", color="default")],
    [get_button(label="На улице", color="positive")],
    [get_button(label="Друга", color="default")],
    [get_button(label="купил", color="positive")],
    [get_button(label="Вернуться в меню", color="primary")]
    
    ]
}

game7 = json.dumps(game7, ensure_ascii=False).encode('utf-8')
game7 = str(game7.decode('utf-8'))

#----------------------------------------------------------

game8 = {
    "one_time": False,
    "buttons": [
    
    [get_button(label="Сдавала жильё", color="default")],
    [get_button(label="Ничем", color="positive")],
    [get_button(label="Процентщица", color="default")],
    [get_button(label="Магазин", color="positive")],
    [get_button(label="Вернуться в меню", color="primary")]
    
    ]
}

game8 = json.dumps(game8, ensure_ascii=False).encode('utf-8')
game8 = str(game8.decode('utf-8'))

#----------------------------------------------------------

game9 = {
    "one_time": False,
    "buttons": [
    
    [get_button(label="Золотое кольцо", color="default")],
    [get_button(label="Серебреное кольцо", color="positive")],
    [get_button(label="Золотой портсигар", color="default")],
    [get_button(label="Серебреный портсигар", color="positive")],
    [get_button(label="Вернуться в меню", color="primary")]
    
    ]
}

game9 = json.dumps(game9, ensure_ascii=False).encode('utf-8')
game9 = str(game9.decode('utf-8'))

#----------------------------------------------------------

game10 = {
    "one_time": False,
    "buttons": [
    
    [get_button(label="Прогул", color="default")],
    [get_button(label="Пьянтсво", color="positive")],
    [get_button(label="Маленькая зарплата", color="default")],
    [get_button(label="Просто по приколу", color="positive")],
    [get_button(label="Вернуться в меню", color="primary")]
    
    ]
}

game10 = json.dumps(game10, ensure_ascii=False).encode('utf-8')
game10 = str(game10.decode('utf-8'))

#----------------------------------------------------------

game11 = {
    "one_time": False,
    "buttons": [
    
    [get_button(label="9 ноября 1821", color="default")],
    [get_button(label="10 ноября 1821", color="positive")],
    [get_button(label="11 ноября 1821", color="default")],
    [get_button(label="12 ноября 1821", color="positive")],
    [get_button(label="Вернуться в меню", color="primary")]
    
    ]
}

game11 = json.dumps(game11, ensure_ascii=False).encode('utf-8')
game11 = str(game11.decode('utf-8'))

#----------------------------------------------------------

game12 = {
    "one_time": False,
    "buttons": [
    
    [get_button(label="Немецкий шляпник", color="default")],
    [get_button(label="Дурак", color="positive")],
    [get_button(label="Французкие башмаки", color="default")],
    [get_button(label="Немецкий часовщик", color="positive")],
    [get_button(label="Вернуться в меню", color="primary")]
    
    ]
}

game12 = json.dumps(game12, ensure_ascii=False).encode('utf-8')
game12 = str(game12.decode('utf-8'))

#----------------------------------------------------------

game13 = {
    "one_time": False,
    "buttons": [
    
    [get_button(label="Взаимосвязь с британским романтизмом", color="default")],
    [get_button(label="Взаимосвязь с русским романтизмом", color="positive")],
    [get_button(label="Взаимосвязь с французским романтизмом", color="default")],
    [get_button(label="Взаимосвязь с немецким романтизмом", color="positive")],
    [get_button(label="Вернуться в меню", color="primary")]
    
    ]
}

game13 = json.dumps(game13, ensure_ascii=False).encode('utf-8')
game13 = str(game13.decode('utf-8'))

#----------------------------------------------------------

game14 = {
    "one_time": False,
    "buttons": [
    
    [get_button(label="Продать шляпу", color="default")],
    [get_button(label="Снять шляпу", color="positive")],
    [get_button(label="Сменить шляпу", color="default")],
    [get_button(label="Купить шляпу", color="positive")],
    [get_button(label="Вернуться в меню", color="primary")]
    
    ]
}

game14 = json.dumps(game14, ensure_ascii=False).encode('utf-8')
game14 = str(game14.decode('utf-8'))

#----------------------------------------------------------

game15 = {
    "one_time": False,
    "buttons": [
    
    [get_button(label="Юрист", color="default")],
    [get_button(label="Продавец шляп", color="positive")],
    [get_button(label="Безработный", color="default")],
    [get_button(label="Процентщик", color="positive")],
    [get_button(label="Вернуться в меню", color="primary")]
    
    ]
}

game15 = json.dumps(game15, ensure_ascii=False).encode('utf-8')
game15 = str(game15.decode('utf-8'))



#----------------------------------------------------------------------------------------------------
while True:
    #Проверка отправки сообщения 
    messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"}) 
    if messages["count"] >= 1: 
        id = messages["items"][0]["last_message"]["from_id"] 
        body = messages["items"][0]["last_message"]["text"]
        if body.lower() == "характеристика героев":
            connection = sql.connect('school.sqlite', check_same_thread=False)
            q = connection.cursor()
            q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
            result = q.fetchall()
            connection.commit()
            connection.close()
            if len(result) == 0:
                vk.method("messages.send", {"peer_id": id, "message": "Ой!\nПохоже ваш id небыл найден!\nНапишите \"начать\", чтобы мы зарегестрировали ваш id.", "random_id": random.randint(1, 2147483647)})
            else:
                vk.method("messages.send", {"peer_id": id, "message": "Выберите персонажа:", "keyboard": characteristic, "random_id": random.randint(1, 2147483647)})
        elif body.lower() == "информация":
            connection = sql.connect('school.sqlite', check_same_thread=False)
            q = connection.cursor()
            q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
            result = q.fetchall()
            connection.commit()
            connection.close()
            if len(result) == 0:
                vk.method("messages.send", {"peer_id": id, "message": "Ой!\nПохоже ваш id небыл найден!\nНапишите \"начать\", чтобы мы зарегестрировали ваш id.", "random_id": random.randint(1, 2147483647)})
            else:
                vk.method("messages.send", {"peer_id": id, "message": "Времени было убито на это: 3 часа\nСоздано на языке програмированния: python\n\nРома делал: программу, бота, игру\nДенис делал: характеристику персонажей.", "random_id": random.randint(1, 2147483647)})
        elif body.lower() == "раскольников радион":
            connection = sql.connect('school.sqlite', check_same_thread=False)
            q = connection.cursor()
            q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
            result = q.fetchall()
            connection.commit()
            connection.close()
            if len(result) == 0:
                vk.method("messages.send", {"peer_id": id, "message": "Ой!\nПохоже ваш id небыл найден!\nНапишите \"начать\", чтобы мы зарегестрировали ваш id.", "random_id": random.randint(1, 2147483647)})
            else:
                vk.method("messages.send", {"peer_id": id, "message": "Ф. И.: Раскольников Родио\n\nСтатус: Бывший студент университета, забросивший занятия на юридическом факультете\n\nХарактер: Мрачен, задумчив и замкнут.", "random_id": random.randint(1, 2147483647)})
                vk.method("messages.send", {"peer_id": id, "message": "Родион Раскольников находится в крайне бедственном положении. У него нет денег, чтобы отдать долги за квартиру, оплатить учёбу. Юноша умён и образован, горд и независим. Унизительное материальное положение, в котором он оказался, делают его угрюмым и замкнутым.", "random_id": random.randint(1, 2147483647)})
                vk.method("messages.send", {"peer_id": id, "message": "Его раздражает общение с людьми. Любая помощь со стороны близкого друга Дмитрия Разумихина или пожилой матери кажется ему унизительной.", "random_id": random.randint(1, 2147483647)})
                vk.method("messages.send", {"peer_id": id, "message": "Непомерная гордыня, больное самолюбие и нищенское состояние порождают в голове Раскольникова некую идею. Суть которой состоит, в подразделении людей на два разряда: обычных и право имеющих. Думая о своём великом предназначении, «тварь ли я дрожащая или право имею? герой готовится к преступлению. Он считает, что совершив убийство старухи, проверит свои идеи, сможет начать новую жизнь и осчастливить человечество.", "random_id": random.randint(1, 2147483647)})
        #--------------------------------------------game
        #------------------------------------------------
        #------------------------------------------------
        elif body.lower() == "играть":
            connection = sql.connect('school.sqlite', check_same_thread=False)
            q = connection.cursor()
            q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
            result = q.fetchall()
            connection.commit()
            connection.close()
            if len(result) == 0:
                vk.method("messages.send", {"peer_id": id, "message": "Ой!\nПохоже ваш id небыл найден!\nНапишите \"начать\", чтобы мы зарегестрировали ваш id.", "random_id": random.randint(1, 2147483647)})
            else:
                connection = sql.connect('school.sqlite', check_same_thread=False)
                q = connection.cursor()
                q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                result = q.fetchall()
                info = result[0][2]
                q.execute("UPDATE user_info SET Question = '%s' WHERE User_ID = '%s'" % (result[0][3] + 1, id))
                connection.commit()
                connection.close()
                vk.method("messages.send", {"peer_id": id, "message": "Вопрос №1\nКак называется роман \"Преступление и наказание\"?", "keyboard": game1, "random_id": random.randint(1, 2147483647)})
        elif body.lower() == "преступление и наказание":#-------2
            connection = sql.connect('school.sqlite', check_same_thread=False)
            q = connection.cursor()
            q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
            result = q.fetchall()
            connection.commit()
            connection.close()
            if len(result) == 0:
                vk.method("messages.send", {"peer_id": id, "message": "Ой!\nПохоже ваш id небыл найден!\nНапишите \"начать\", чтобы мы зарегестрировали ваш id.", "random_id": random.randint(1, 2147483647)})
            else:
                connection = sql.connect('school.sqlite', check_same_thread=False)
                q = connection.cursor()
                q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                result = q.fetchall()
                info = result[0][2]
                q.execute("UPDATE user_info SET Right_Answers = '%s' WHERE User_ID = '%s'" % (result[0][2] + 1, id))
                q.execute("UPDATE user_info SET Question = '%s' WHERE User_ID = '%s'" % (result[0][3] + 1, id))
                connection.commit()
                connection.close()
                vk.method("messages.send", {"peer_id": id, "message": "Правильно!\nВыполнено 1 из 15 вопросов.", "random_id": random.randint(1, 2147483647)})
                time.sleep(1)
                vk.method("messages.send", {"peer_id": id, "message": "Вопрос №2\nКто написал роман \"Преступление и наказание\"?", "keyboard": game2, "random_id": random.randint(1, 2147483647)})
        elif body.lower() == "фёдор достоевский":#-------3
            connection = sql.connect('school.sqlite', check_same_thread=False)
            q = connection.cursor()
            q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
            result = q.fetchall()
            connection.commit()
            connection.close()
            if len(result) == 0:
                vk.method("messages.send", {"peer_id": id, "message": "Ой!\nПохоже ваш id небыл найден!\nНапишите \"начать\", чтобы мы зарегестрировали ваш id.", "random_id": random.randint(1, 2147483647)})
            else:
                connection = sql.connect('school.sqlite', check_same_thread=False)
                q = connection.cursor()
                q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                result = q.fetchall()
                q.execute("UPDATE user_info SET Right_Answers = '%s' WHERE User_ID = '%s'" % (result[0][2] + 1, id))
                q.execute("UPDATE user_info SET Question = '%s' WHERE User_ID = '%s'" % (result[0][3] + 1, id))
                connection.commit()
                connection.close()
                vk.method("messages.send", {"peer_id": id, "message": "Правильно!\nВыполнено 2 из 15 вопросов.", "random_id": random.randint(1, 2147483647)})
                time.sleep(1)
                vk.method("messages.send", {"peer_id": id, "message": "Вопрос №3\nКак зовут главного героя?", "keyboard": game3, "random_id": random.randint(1, 2147483647)})
        elif body.lower() == "родион раскольников":#-------4
            connection = sql.connect('school.sqlite', check_same_thread=False)
            q = connection.cursor()
            q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
            result = q.fetchall()
            connection.commit()
            connection.close()
            if len(result) == 0:
                vk.method("messages.send", {"peer_id": id, "message": "Ой!\nПохоже ваш id небыл найден!\nНапишите \"начать\", чтобы мы зарегестрировали ваш id.", "random_id": random.randint(1, 2147483647)})
            else:
                connection = sql.connect('school.sqlite', check_same_thread=False)
                q = connection.cursor()
                q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                result = q.fetchall()
                q.execute("UPDATE user_info SET Right_Answers = '%s' WHERE User_ID = '%s'" % (result[0][2] + 1, id))
                q.execute("UPDATE user_info SET Question = '%s' WHERE User_ID = '%s'" % (result[0][3] + 1, id))
                connection.commit()
                connection.close()
                vk.method("messages.send", {"peer_id": id, "message": "Правильно!\nВыполнено 3 из 15 вопросов.", "random_id": random.randint(1, 2147483647)})
                time.sleep(1)
                vk.method("messages.send", {"peer_id": id, "message": "Вопрос №4\nКак зовут отца Софьи Мармеладовой?", "keyboard": game4, "random_id": random.randint(1, 2147483647)})
        elif body.lower() == "семён мармеладов":#-------5
            connection = sql.connect('school.sqlite', check_same_thread=False)
            q = connection.cursor()
            q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
            result = q.fetchall()
            connection.commit()
            connection.close()
            if len(result) == 0:
                vk.method("messages.send", {"peer_id": id, "message": "Ой!\nПохоже ваш id небыл найден!\nНапишите \"начать\", чтобы мы зарегестрировали ваш id.", "random_id": random.randint(1, 2147483647)})
            else:
                connection = sql.connect('school.sqlite', check_same_thread=False)
                q = connection.cursor()
                q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                result = q.fetchall()
                q.execute("UPDATE user_info SET Right_Answers = '%s' WHERE User_ID = '%s'" % (result[0][2] + 1, id))
                q.execute("UPDATE user_info SET Question = '%s' WHERE User_ID = '%s'" % (result[0][3] + 1, id))
                connection.commit()
                connection.close()
                vk.method("messages.send", {"peer_id": id, "message": "Правильно!\nВыполнено 4 из 15 вопросов.", "random_id": random.randint(1, 2147483647)})
                time.sleep(1)
                vk.method("messages.send", {"peer_id": id, "message": "Вопрос №5\nВ каком году был написан этот роман?", "keyboard": game5, "random_id": random.randint(1, 2147483647)})
        elif body.lower() == "1866":#-------6
            connection = sql.connect('school.sqlite', check_same_thread=False)
            q = connection.cursor()
            q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
            result = q.fetchall()
            connection.commit()
            connection.close()
            if len(result) == 0:
                vk.method("messages.send", {"peer_id": id, "message": "Ой!\nПохоже ваш id небыл найден!\nНапишите \"начать\", чтобы мы зарегестрировали ваш id.", "random_id": random.randint(1, 2147483647)})
            else:
                connection = sql.connect('school.sqlite', check_same_thread=False)
                q = connection.cursor()
                q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                result = q.fetchall()
                q.execute("UPDATE user_info SET Right_Answers = '%s' WHERE User_ID = '%s'" % (result[0][2] + 1, id))
                q.execute("UPDATE user_info SET Question = '%s' WHERE User_ID = '%s'" % (result[0][3] + 1, id))
                connection.commit()
                connection.close()
                vk.method("messages.send", {"peer_id": id, "message": "Правильно!\nВыполнено 5 из 15 вопросов.", "random_id": random.randint(1, 2147483647)})
                time.sleep(1)
                vk.method("messages.send", {"peer_id": id, "message": "Вопрос №6\nЧто символизируют жёлтые обои?", "keyboard": game6, "random_id": random.randint(1, 2147483647)})
        elif body.lower() == "шизофренизм":#-------7
            connection = sql.connect('school.sqlite', check_same_thread=False)
            q = connection.cursor()
            q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
            result = q.fetchall()
            connection.commit()
            connection.close()
            if len(result) == 0:
                vk.method("messages.send", {"peer_id": id, "message": "Ой!\nПохоже ваш id небыл найден!\nНапишите \"начать\", чтобы мы зарегестрировали ваш id.", "random_id": random.randint(1, 2147483647)})
            else:
                connection = sql.connect('school.sqlite', check_same_thread=False)
                q = connection.cursor()
                q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                result = q.fetchall()
                q.execute("UPDATE user_info SET Right_Answers = '%s' WHERE User_ID = '%s'" % (result[0][2] + 1, id))
                q.execute("UPDATE user_info SET Question = '%s' WHERE User_ID = '%s'" % (result[0][3] + 1, id))
                connection.commit()
                connection.close()
                vk.method("messages.send", {"peer_id": id, "message": "Правильно!\nВыполнено 6 из 15 вопросов.", "random_id": random.randint(1, 2147483647)})
                time.sleep(1)
                vk.method("messages.send", {"peer_id": id, "message": "Вопрос №7\nУ кого Раскольников взял топор?", "keyboard": game7, "random_id": random.randint(1, 2147483647)})
        elif body.lower() == "дворник":#-------8
            connection = sql.connect('school.sqlite', check_same_thread=False)
            q = connection.cursor()
            q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
            result = q.fetchall()
            connection.commit()
            connection.close()
            if len(result) == 0:
                vk.method("messages.send", {"peer_id": id, "message": "Ой!\nПохоже ваш id небыл найден!\nНапишите \"начать\", чтобы мы зарегестрировали ваш id.", "random_id": random.randint(1, 2147483647)})
            else:
                connection = sql.connect('school.sqlite', check_same_thread=False)
                q = connection.cursor()
                q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                result = q.fetchall()
                q.execute("UPDATE user_info SET Right_Answers = '%s' WHERE User_ID = '%s'" % (result[0][2] + 1, id))
                q.execute("UPDATE user_info SET Question = '%s' WHERE User_ID = '%s'" % (result[0][3] + 1, id))
                connection.commit()
                connection.close()
                vk.method("messages.send", {"peer_id": id, "message": "Правильно!\nВыполнено 7 из 15 вопросов.", "random_id": random.randint(1, 2147483647)})
                time.sleep(1)
                vk.method("messages.send", {"peer_id": id, "message": "Вопрос №8\nЧем занималась Алёна Ивановна?", "keyboard": game8, "random_id": random.randint(1, 2147483647)})
        elif body.lower() == "процентщица":#-------9
            connection = sql.connect('school.sqlite', check_same_thread=False)
            q = connection.cursor()
            q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
            result = q.fetchall()
            connection.commit()
            connection.close()
            if len(result) == 0:
                vk.method("messages.send", {"peer_id": id, "message": "Ой!\nПохоже ваш id небыл найден!\nНапишите \"начать\", чтобы мы зарегестрировали ваш id.", "random_id": random.randint(1, 2147483647)})
            else:
                connection = sql.connect('school.sqlite', check_same_thread=False)
                q = connection.cursor()
                q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                result = q.fetchall()
                q.execute("UPDATE user_info SET Right_Answers = '%s' WHERE User_ID = '%s'" % (result[0][2] + 1, id))
                q.execute("UPDATE user_info SET Question = '%s' WHERE User_ID = '%s'" % (result[0][3] + 1, id))
                connection.commit()
                connection.close()
                vk.method("messages.send", {"peer_id": id, "message": "Правильно!\nВыполнено 8 из 15 вопросов.", "random_id": random.randint(1, 2147483647)})
                time.sleep(1)
                vk.method("messages.send", {"peer_id": id, "message": "Вопрос №9\nЧто последнее принёс Раскольников Алёне Ивановне?", "keyboard": game9, "random_id": random.randint(1, 2147483647)})
        elif body.lower() == "серебреный портсигар":#-------10
            connection = sql.connect('school.sqlite', check_same_thread=False)
            q = connection.cursor()
            q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
            result = q.fetchall()
            connection.commit()
            connection.close()
            if len(result) == 0:
                vk.method("messages.send", {"peer_id": id, "message": "Ой!\nПохоже ваш id небыл найден!\nНапишите \"начать\", чтобы мы зарегестрировали ваш id.", "random_id": random.randint(1, 2147483647)})
            else:
                connection = sql.connect('school.sqlite', check_same_thread=False)
                q = connection.cursor()
                q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                result = q.fetchall()
                q.execute("UPDATE user_info SET Right_Answers = '%s' WHERE User_ID = '%s'" % (result[0][2] + 1, id))
                q.execute("UPDATE user_info SET Question = '%s' WHERE User_ID = '%s'" % (result[0][3] + 1, id))
                connection.commit()
                connection.close()
                vk.method("messages.send", {"peer_id": id, "message": "Правильно!\nВыполнено 9 из 15 вопросов.", "random_id": random.randint(1, 2147483647)})
                time.sleep(1)
                vk.method("messages.send", {"peer_id": id, "message": "Вопрос №10\nПо какой причине Мармеладов уволился с работы?", "keyboard": game10, "random_id": random.randint(1, 2147483647)})
        elif body.lower() == "пьянтсво":#-------11
            connection = sql.connect('school.sqlite', check_same_thread=False)
            q = connection.cursor()
            q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
            result = q.fetchall()
            connection.commit()
            connection.close()
            if len(result) == 0:
                vk.method("messages.send", {"peer_id": id, "message": "Ой!\nПохоже ваш id небыл найден!\nНапишите \"начать\", чтобы мы зарегестрировали ваш id.", "random_id": random.randint(1, 2147483647)})
            else:
                connection = sql.connect('school.sqlite', check_same_thread=False)
                q = connection.cursor()
                q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                result = q.fetchall()
                q.execute("UPDATE user_info SET Right_Answers = '%s' WHERE User_ID = '%s'" % (result[0][2] + 1, id))
                q.execute("UPDATE user_info SET Question = '%s' WHERE User_ID = '%s'" % (result[0][3] + 1, id))
                connection.commit()
                connection.close()
                vk.method("messages.send", {"peer_id": id, "message": "Правильно!\nВыполнено 10 из 15 вопросов.", "random_id": random.randint(1, 2147483647)})
                time.sleep(1)
                vk.method("messages.send", {"peer_id": id, "message": "Вопрос №11\nКогда родился Достоевский?", "keyboard": game11, "random_id": random.randint(1, 2147483647)})
        elif body.lower() == "11 ноября 1821":#-------12
            connection = sql.connect('school.sqlite', check_same_thread=False)
            q = connection.cursor()
            q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
            result = q.fetchall()
            connection.commit()
            connection.close()
            if len(result) == 0:
                vk.method("messages.send", {"peer_id": id, "message": "Ой!\nПохоже ваш id небыл найден!\nНапишите \"начать\", чтобы мы зарегестрировали ваш id.", "random_id": random.randint(1, 2147483647)})
            else:
                connection = sql.connect('school.sqlite', check_same_thread=False)
                q = connection.cursor()
                q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                result = q.fetchall()
                q.execute("UPDATE user_info SET Right_Answers = '%s' WHERE User_ID = '%s'" % (result[0][2] + 1, id))
                q.execute("UPDATE user_info SET Question = '%s' WHERE User_ID = '%s'" % (result[0][3] + 1, id))
                connection.commit()
                connection.close()
                vk.method("messages.send", {"peer_id": id, "message": "Правильно!\nВыполнено 11 из 15 вопросов.", "random_id": random.randint(1, 2147483647)})
                time.sleep(1)
                vk.method("messages.send", {"peer_id": id, "message": "Вопрос №12\nКак звали Раскольникого?", "keyboard": game12, "random_id": random.randint(1, 2147483647)})
        elif body.lower() == "немецкий шляпник":#-------13
            connection = sql.connect('school.sqlite', check_same_thread=False)
            q = connection.cursor()
            q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
            result = q.fetchall()
            connection.commit()
            connection.close()
            if len(result) == 0:
                vk.method("messages.send", {"peer_id": id, "message": "Ой!\nПохоже ваш id небыл найден!\nНапишите \"начать\", чтобы мы зарегестрировали ваш id.", "random_id": random.randint(1, 2147483647)})
            else:
                connection = sql.connect('school.sqlite', check_same_thread=False)
                q = connection.cursor()
                q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                result = q.fetchall()
                q.execute("UPDATE user_info SET Right_Answers = '%s' WHERE User_ID = '%s'" % (result[0][2] + 1, id))
                q.execute("UPDATE user_info SET Question = '%s' WHERE User_ID = '%s'" % (result[0][3] + 1, id))
                connection.commit()
                connection.close()
                vk.method("messages.send", {"peer_id": id, "message": "Правильно!\nВыполнено 12 из 15 вопросов.", "random_id": random.randint(1, 2147483647)})
                time.sleep(1)
                vk.method("messages.send", {"peer_id": id, "message": "Вопрос №13\nПочему его звали \"немецкий шляпник\"?", "keyboard": game13, "random_id": random.randint(1, 2147483647)})
        elif body.lower() == "взаимосвязь с немецким романтизмом":#-------14
            connection = sql.connect('school.sqlite', check_same_thread=False)
            q = connection.cursor()
            q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
            result = q.fetchall()
            connection.commit()
            connection.close()
            if len(result) == 0:
                vk.method("messages.send", {"peer_id": id, "message": "Ой!\nПохоже ваш id небыл найден!\nНапишите \"начать\", чтобы мы зарегестрировали ваш id.", "random_id": random.randint(1, 2147483647)})
            else:
                connection = sql.connect('school.sqlite', check_same_thread=False)
                q = connection.cursor()
                q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                result = q.fetchall()
                q.execute("UPDATE user_info SET Right_Answers = '%s' WHERE User_ID = '%s'" % (result[0][2] + 1, id))
                q.execute("UPDATE user_info SET Question = '%s' WHERE User_ID = '%s'" % (result[0][3] + 1, id))
                connection.commit()
                connection.close()
                vk.method("messages.send", {"peer_id": id, "message": "Правильно!\nВыполнено 13 из 15 вопросов.", "random_id": random.randint(1, 2147483647)})
                time.sleep(1)
                vk.method("messages.send", {"peer_id": id, "message": "Вопрос №14\nЧто забыл сделать Раскольников перед убийством?", "keyboard": game14, "random_id": random.randint(1, 2147483647)})
        elif body.lower() == "сменить шляпу":#-------15
            connection = sql.connect('school.sqlite', check_same_thread=False)
            q = connection.cursor()
            q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
            result = q.fetchall()
            connection.commit()
            connection.close()
            if len(result) == 0:
                vk.method("messages.send", {"peer_id": id, "message": "Ой!\nПохоже ваш id небыл найден!\nНапишите \"начать\", чтобы мы зарегестрировали ваш id.", "random_id": random.randint(1, 2147483647)})
            else:
                connection = sql.connect('school.sqlite', check_same_thread=False)
                q = connection.cursor()
                q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                result = q.fetchall()
                q.execute("UPDATE user_info SET Right_Answers = '%s' WHERE User_ID = '%s'" % (result[0][2] + 1, id))
                q.execute("UPDATE user_info SET Question = '%s' WHERE User_ID = '%s'" % (result[0][3] + 1, id))
                connection.commit()
                connection.close()
                vk.method("messages.send", {"peer_id": id, "message": "Правильно!\nВыполнено 14 из 15 вопросов.", "random_id": random.randint(1, 2147483647)})
                time.sleep(1)
                vk.method("messages.send", {"peer_id": id, "message": "Вопрос №15\nКакова будущая специальность Раскольникова?", "keyboard": game15, "random_id": random.randint(1, 2147483647)})
        elif body.lower() == "юрист":#-------end
            connection = sql.connect('school.sqlite', check_same_thread=False)
            q = connection.cursor()
            q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
            result = q.fetchall()
            connection.commit()
            connection.close()
            if len(result) == 0:
                vk.method("messages.send", {"peer_id": id, "message": "Ой!\nПохоже ваш id небыл найден!\nНапишите \"начать\", чтобы мы зарегестрировали ваш id.", "random_id": random.randint(1, 2147483647)})
            else:
                connection = sql.connect('school.sqlite', check_same_thread=False)
                q = connection.cursor()
                q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                result = q.fetchall()
                q.execute("UPDATE user_info SET Right_Answers = '%s' WHERE User_ID = '%s'" % (result[0][2] + 1, id))
                connection.commit()
                connection.close()
                connection = sql.connect('school.sqlite', check_same_thread=False)
                q = connection.cursor()
                q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                result = q.fetchall()
                q.execute("UPDATE user_info SET Right_Answers = '%s' WHERE User_ID = '%s'" % (0, id))
                q.execute("UPDATE user_info SET Question = '%s' WHERE User_ID = '%s'" % (0, id))
                info_right_answers = result[0][2]
                connection.commit()
                connection.close()
                vk.method("messages.send", {"peer_id": id, "message": "Правильно!\nВыполнено 15 из 15 вопросов.", "random_id": random.randint(1, 2147483647)})
                time.sleep(1)
                vk.method("messages.send", {"peer_id": id, "message": "Привильно выполненых заданий " + str(info_right_answers) + " из 15.", "keyboard": menu, "random_id": random.randint(1, 2147483647)})
        elif body.lower() == "!info stats":
            connection = sql.connect('school.sqlite', check_same_thread=False)
            q = connection.cursor()
            q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
            result = q.fetchall()
            connection.commit()
            connection.close()
            if len(result) == 0:
                vk.method("messages.send", {"peer_id": id, "message": "Ой!\nПохоже ваш id небыл найден!\nНапишите \"начать\", чтобы мы зарегестрировали ваш id.", "random_id": random.randint(1, 2147483647)})
            else:
                connection = sql.connect('school.sqlite', check_same_thread=False)
                q = connection.cursor()
                q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                result = q.fetchall()
                info_right_answers = result[0][2]
                info_question = result[0][3]
                connection.commit()
                connection.close()
                vk.method("messages.send", {"peer_id": id, "message": "Right_Answers = " + str(info_right_answers) + "\nQustion = " + str(info_question), "random_id": random.randint(1, 2147483647)})
        elif body.lower() == "!set menu":
            connection = sql.connect('school.sqlite', check_same_thread=False)
            q = connection.cursor()
            q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
            result = q.fetchall()
            connection.commit()
            connection.close()
            if len(result) == 0:
                vk.method("messages.send", {"peer_id": id, "message": "Ой!\nПохоже ваш id небыл найден!\nНапишите \"начать\", чтобы мы зарегестрировали ваш id.", "random_id": random.randint(1, 2147483647)})
            else:
                connection = sql.connect('school.sqlite', check_same_thread=False)
                q = connection.cursor()
                q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                result = q.fetchall()
                q.execute("UPDATE user_info SET Right_Answers = '%s' WHERE User_ID = '%s'" % (0, id))
                q.execute("UPDATE user_info SET Question = '%s' WHERE User_ID = '%s'" % (0, id))
                connection.commit()
                connection.close()
                vk.method("messages.send", {"peer_id": id, "message": "set menu", "keyboard": menu, "random_id": random.randint(1, 2147483647)})
        elif body.lower() == "!set question 0":
            connection = sql.connect('school.sqlite', check_same_thread=False)
            q = connection.cursor()
            q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
            result = q.fetchall()
            connection.commit()
            connection.close()
            if len(result) == 0:
                vk.method("messages.send", {"peer_id": id, "message": "Ой!\nПохоже ваш id небыл найден!\nНапишите \"начать\", чтобы мы зарегестрировали ваш id.", "random_id": random.randint(1, 2147483647)})
            else:
                connection = sql.connect('school.sqlite', check_same_thread=False)
                q = connection.cursor()
                q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                result = q.fetchall()
                q.execute("UPDATE user_info SET Right_Answers = '%s' WHERE User_ID = '%s'" % (0, id))
                q.execute("UPDATE user_info SET Question = '%s' WHERE User_ID = '%s'" % (0, id))
                connection.commit()
                connection.close()
                vk.method("messages.send", {"peer_id": id, "message": "set 0", "keyboard": menu, "random_id": random.randint(1, 2147483647)})
        elif body.lower() == "вернуться в меню":
            connection = sql.connect('school.sqlite', check_same_thread=False)
            q = connection.cursor()
            q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
            result = q.fetchall()
            connection.commit()
            connection.close()
            if len(result) == 0:
                vk.method("messages.send", {"peer_id": id, "message": "Ой!\nПохоже ваш id небыл найден!\nНапишите \"начать\", чтобы мы зарегестрировали ваш id.", "random_id": random.randint(1, 2147483647)})
            else:
                vk.method("messages.send", {"peer_id": id, "message": "При выходе в меню ваш пргресс будет утерян!", "keyboard": yes_or_no, "random_id": random.randint(1, 2147483647)})
        elif body.lower() == "да":
            connection = sql.connect('school.sqlite', check_same_thread=False)
            q = connection.cursor()
            q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
            result = q.fetchall()
            connection.commit()
            connection.close()
            if len(result) == 0:
                vk.method("messages.send", {"peer_id": id, "message": "Ой!\nПохоже ваш id небыл найден!\nНапишите \"начать\", чтобы мы зарегестрировали ваш id.", "random_id": random.randint(1, 2147483647)})
            else:
                connection = sql.connect('school.sqlite', check_same_thread=False)
                q = connection.cursor()
                q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                result = q.fetchall()
                q.execute("UPDATE user_info SET Right_Answers = '%s' WHERE User_ID = '%s'" % (0, id))
                q.execute("UPDATE user_info SET Question = '%s' WHERE User_ID = '%s'" % (0, id))
                connection.commit()
                connection.close()
                vk.method("messages.send", {"peer_id": id, "message": "Меню:", "keyboard": menu, "random_id": random.randint(1, 2147483647)})
        elif body.lower() == "нет":
            connection = sql.connect('school.sqlite', check_same_thread=False)
            q = connection.cursor()
            q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
            result = q.fetchall()
            if len(result) == 0:
                connection.commit()
                connection.close()
                vk.method("messages.send", {"peer_id": id, "message": "Ой!\nПохоже ваш id небыл найден!\nНапишите \"начать\", чтобы мы зарегестрировали ваш id.", "random_id": random.randint(1, 2147483647)})
            else:
                info_question = result[0][3]
                if info_question > 0:
                    if info_question == 1:
                        connection.commit()
                        connection.close()
                        vk.method("messages.send", {"peer_id": id, "message": "Вопрос №1\nКак называется роман \"Преступление и наказание\"?", "keyboard": game1, "random_id": random.randint(1, 2147483647)})
                    elif info_question == 2:
                        connection.commit()
                        connection.close()
                        vk.method("messages.send", {"peer_id": id, "message": "Вопрос №2\nКто написал роман \"Преступление и наказание\"?", "keyboard": game2, "random_id": random.randint(1, 2147483647)})
                    elif info_question == 3:
                        connection.commit()
                        connection.close()
                        vk.method("messages.send", {"peer_id": id, "message": "Вопрос №3\nКак зовут главного героя?", "keyboard": game3, "random_id": random.randint(1, 2147483647)})
                    elif info_question == 4:
                        connection.commit()
                        connection.close()
                        vk.method("messages.send", {"peer_id": id, "message": "Вопрос №4\nКак зовут отца Софьи Мармеладовой?", "keyboard": game4, "random_id": random.randint(1, 2147483647)})
                    elif info_question == 5:
                        connection.commit()
                        connection.close()
                        vk.method("messages.send", {"peer_id": id, "message": "Вопрос №5\nВ каком году был написан этот роман?", "keyboard": game5, "random_id": random.randint(1, 2147483647)})
                    elif info_question == 6:
                        connection.commit()
                        connection.close()
                        vk.method("messages.send", {"peer_id": id, "message": "Вопрос №6\nЧто символизируют жёлтые обои?", "keyboard": game6, "random_id": random.randint(1, 2147483647)})
                    elif info_question == 7:
                        connection.commit()
                        connection.close()
                        vk.method("messages.send", {"peer_id": id, "message": "Вопрос №7\nУ кого Раскольников взял топор?", "keyboard": game7, "random_id": random.randint(1, 2147483647)})
                    elif info_question == 8:
                        connection.commit()
                        connection.close()
                        vk.method("messages.send", {"peer_id": id, "message": "Вопрос №8\nЧем занималась Алёна Ивановна?", "keyboard": game8, "random_id": random.randint(1, 2147483647)})
                    elif info_question == 9:
                        connection.commit()
                        connection.close()
                        vk.method("messages.send", {"peer_id": id, "message": "Вопрос №9\nЧто последнее принёс Раскольников Алёне Ивановне?", "keyboard": game9, "random_id": random.randint(1, 2147483647)})
                    elif info_question == 10:
                        connection.commit()
                        connection.close()
                        vk.method("messages.send", {"peer_id": id, "message": "Вопрос №10\nПо какой причине Мармеладов уволился с работы?", "keyboard": game10, "random_id": random.randint(1, 2147483647)})
                    elif info_question == 11:
                        connection.commit()
                        connection.close()
                        vk.method("messages.send", {"peer_id": id, "message": "Вопрос №11\nКогда родился Достоевский?", "keyboard": game11, "random_id": random.randint(1, 2147483647)})
                    elif info_question == 12:
                        connection.commit()
                        connection.close()
                        vk.method("messages.send", {"peer_id": id, "message": "Вопрос №12\nКак звали Раскольникого?", "keyboard": game12, "random_id": random.randint(1, 2147483647)})
                    elif info_question == 13:
                        connection.commit()
                        connection.close()
                        vk.method("messages.send", {"peer_id": id, "message": "Вопрос №13\nПочему его звали \"немецкий шляпник\"?", "keyboard": game13, "random_id": random.randint(1, 2147483647)})
                    elif info_question == 14:
                        connection.commit()
                        connection.close()
                        vk.method("messages.send", {"peer_id": id, "message": "Вопрос №14\nЧто забыл сделать Раскольников перед убийством?", "keyboard": game14, "random_id": random.randint(1, 2147483647)})
                    elif info_question == 15:
                        connection.commit()
                        connection.close()
                        vk.method("messages.send", {"peer_id": id, "message": "Вопрос №15\nКакова будущая специальность Раскольникова?", "keyboard": game15, "random_id": random.randint(1, 2147483647)})

                    else:
                        vk.method("messages.send", {"peer_id": id, "message": "Произошла ошибка sy-0001-1\nInfo_question - значение за предалми списка!\nКод строки 832.\nКоманда \"!set question 0\" для починки.", "random_id": random.randint(1, 2147483647)})
                    
                else:
                    connection.commit()
                    connection.close()
                    time.sleep(0.1)
        else:
            connection = sql.connect('school.sqlite', check_same_thread=False)
            q = connection.cursor()
            q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
            result = q.fetchall()
            connection.commit()
            connection.close()
            if len(result) == 0:
                connection = sql.connect('school.sqlite', check_same_thread=False)
                q = connection.cursor()
                q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                result = q.fetchall()
                q.execute("INSERT INTO user_info (User_ID, Right_Answers, Question, Answer) VALUES ('%s', '%s', '%s', '%s')" % (id, 0, 0, 0))
                connection.commit()
                connection.close()
                vk.method("messages.send", {"peer_id": id, "message": "Здравтсвуйте!", "keyboard": menu, "random_id": random.randint(1, 2147483647)})
            else:
                connection = sql.connect('school.sqlite', check_same_thread=False)
                q = connection.cursor()
                q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                result = q.fetchall()
                info_question = result[0][3]
                if info_question > 0:
                    if info_question == 1:
                        q.execute("UPDATE user_info SET Question = '%s' WHERE User_ID = '%s'" % (result[0][3] + 1, id))
                        connection.commit()
                        connection.close()
                        vk.method("messages.send", {"peer_id": id, "message": "Не правильно! Выполнено 1 из 15 вопросов.", "random_id": random.randint(1, 2147483647)})
                        vk.method("messages.send", {"peer_id": id, "message": "Вопрос №2\nКто написал роман \"Преступление и наказание\"?", "keyboard": game2, "random_id": random.randint(1, 2147483647)})
                    elif info_question == 2:
                        q.execute("UPDATE user_info SET Question = '%s' WHERE User_ID = '%s'" % (result[0][3] + 1, id))
                        connection.commit()
                        connection.close()
                        vk.method("messages.send", {"peer_id": id, "message": "Не правильно! Выполнено 2 из 15 вопросов.", "random_id": random.randint(1, 2147483647)})
                        vk.method("messages.send", {"peer_id": id, "message": "Вопрос №3\nКак зовут главного героя?", "keyboard": game3, "random_id": random.randint(1, 2147483647)})
                    elif info_question == 3:
                        q.execute("UPDATE user_info SET Question = '%s' WHERE User_ID = '%s'" % (result[0][3] + 1, id))
                        connection.commit()
                        connection.close()
                        vk.method("messages.send", {"peer_id": id, "message": "Не правильно! Выполнено 3 из 15 вопросов.", "random_id": random.randint(1, 2147483647)})
                        vk.method("messages.send", {"peer_id": id, "message": "Вопрос №4\nКак зовут отца Софьи Мармеладовой?", "keyboard": game4, "random_id": random.randint(1, 2147483647)})
                    elif info_question == 4:
                        q.execute("UPDATE user_info SET Question = '%s' WHERE User_ID = '%s'" % (result[0][3] + 1, id))
                        connection.commit()
                        connection.close()
                        vk.method("messages.send", {"peer_id": id, "message": "Не правильно! Выполнено 4 из 15 вопросов.", "random_id": random.randint(1, 2147483647)})
                        vk.method("messages.send", {"peer_id": id, "message": "Вопрос №5\nВ каком году был написан этот роман?", "keyboard": game5, "random_id": random.randint(1, 2147483647)})
                    elif info_question == 5:
                        q.execute("UPDATE user_info SET Question = '%s' WHERE User_ID = '%s'" % (result[0][3] + 1, id))
                        connection.commit()
                        connection.close()
                        vk.method("messages.send", {"peer_id": id, "message": "Не правильно! Выполнено 5 из 15 вопросов.", "random_id": random.randint(1, 2147483647)})
                        vk.method("messages.send", {"peer_id": id, "message": "Вопрос №6\nЧто символизируют жёлтые обои?", "keyboard": game6, "random_id": random.randint(1, 2147483647)})
                    elif info_question == 6:
                        q.execute("UPDATE user_info SET Question = '%s' WHERE User_ID = '%s'" % (result[0][3] + 1, id))
                        connection.commit()
                        connection.close()
                        vk.method("messages.send", {"peer_id": id, "message": "Не правильно! Выполнено 6 из 15 вопросов.", "random_id": random.randint(1, 2147483647)})
                        vk.method("messages.send", {"peer_id": id, "message": "Вопрос №7\nУ кого Раскольников взял топор?", "keyboard": game7, "random_id": random.randint(1, 2147483647)})
                    elif info_question == 7:
                        q.execute("UPDATE user_info SET Question = '%s' WHERE User_ID = '%s'" % (result[0][3] + 1, id))
                        connection.commit()
                        connection.close()
                        vk.method("messages.send", {"peer_id": id, "message": "Не правильно! Выполнено 7 из 15 вопросов.", "random_id": random.randint(1, 2147483647)})
                        vk.method("messages.send", {"peer_id": id, "message": "Вопрос №8\nЧем занималась Алёна Ивановна?", "keyboard": game8, "random_id": random.randint(1, 2147483647)})
                    elif info_question == 8:
                        q.execute("UPDATE user_info SET Question = '%s' WHERE User_ID = '%s'" % (result[0][3] + 1, id))
                        connection.commit()
                        connection.close()
                        vk.method("messages.send", {"peer_id": id, "message": "Не правильно! Выполнено 8 из 15 вопросов.", "random_id": random.randint(1, 2147483647)})
                        vk.method("messages.send", {"peer_id": id, "message": "Вопрос №9\nЧто последнее принёс Раскольников Алёне Ивановне?", "keyboard": game9, "random_id": random.randint(1, 2147483647)})
                    elif info_question == 9:
                        q.execute("UPDATE user_info SET Question = '%s' WHERE User_ID = '%s'" % (result[0][3] + 1, id))
                        connection.commit()
                        connection.close()
                        vk.method("messages.send", {"peer_id": id, "message": "Не правильно! Выполнено 9 из 15 вопросов.", "random_id": random.randint(1, 2147483647)})
                        vk.method("messages.send", {"peer_id": id, "message": "Вопрос №10\nПо какой причине Мармеладов уволился с работы?", "keyboard": game10, "random_id": random.randint(1, 2147483647)})
                    elif info_question == 10:
                        q.execute("UPDATE user_info SET Question = '%s' WHERE User_ID = '%s'" % (result[0][3] + 1, id))
                        connection.commit()
                        connection.close()
                        vk.method("messages.send", {"peer_id": id, "message": "Не правильно! Выполнено 10 из 15 вопросов.", "random_id": random.randint(1, 2147483647)})
                        vk.method("messages.send", {"peer_id": id, "message": "Вопрос №11\nКогда родился Достоевский?", "keyboard": game11, "random_id": random.randint(1, 2147483647)})
                    elif info_question == 11:
                        q.execute("UPDATE user_info SET Question = '%s' WHERE User_ID = '%s'" % (result[0][3] + 1, id))
                        connection.commit()
                        connection.close()
                        vk.method("messages.send", {"peer_id": id, "message": "Не правильно! Выполнено 11 из 15 вопросов.", "random_id": random.randint(1, 2147483647)})
                        vk.method("messages.send", {"peer_id": id, "message": "Вопрос №12\nКак звали Раскольникого?", "keyboard": game12, "random_id": random.randint(1, 2147483647)})
                    elif info_question == 12:
                        q.execute("UPDATE user_info SET Question = '%s' WHERE User_ID = '%s'" % (result[0][3] + 1, id))
                        connection.commit()
                        connection.close()
                        vk.method("messages.send", {"peer_id": id, "message": "Не правильно! Выполнено 12 из 15 вопросов.", "random_id": random.randint(1, 2147483647)})
                        vk.method("messages.send", {"peer_id": id, "message": "Вопрос №13\nПочему его звали \"немецкий шляпник\"?", "keyboard": game13, "random_id": random.randint(1, 2147483647)})
                    elif info_question == 13:
                        q.execute("UPDATE user_info SET Question = '%s' WHERE User_ID = '%s'" % (result[0][3] + 1, id))
                        connection.commit()
                        connection.close()
                        vk.method("messages.send", {"peer_id": id, "message": "Не правильно! Выполнено 13 из 15 вопросов.", "random_id": random.randint(1, 2147483647)})
                        vk.method("messages.send", {"peer_id": id, "message": "Вопрос №14\nЧто забыл сделать Раскольников перед убийством?", "keyboard": game14, "random_id": random.randint(1, 2147483647)})
                    elif info_question == 14:
                        q.execute("UPDATE user_info SET Question = '%s' WHERE User_ID = '%s'" % (result[0][3] + 1, id))
                        connection.commit()
                        connection.close()
                        vk.method("messages.send", {"peer_id": id, "message": "Не правильно! Выполнено 14 из 15 вопросов.", "random_id": random.randint(1, 2147483647)})
                        vk.method("messages.send", {"peer_id": id, "message": "Вопрос №15\nКакова будущая специальность Раскольникова?", "keyboard": game15, "random_id": random.randint(1, 2147483647)})
                    elif info_question == 15:
                        q.execute("UPDATE user_info SET Right_Answers = '%s' WHERE User_ID = '%s'" % (0, id))
                        q.execute("UPDATE user_info SET Question = '%s' WHERE User_ID = '%s'" % (0, id))
                        connection.commit()
                        connection.close()
                        vk.method("messages.send", {"peer_id": id, "message": "Не правильно! Выполнено 15 из 15 вопросов.", "random_id": random.randint(1, 2147483647)})
                        vk.method("messages.send", {"peer_id": id, "message": "Привильно выполненых заданий " + str(info_right_answers) + " из 15.", "keyboard": menu, "random_id": random.randint(1, 2147483647)})
                    else:
                        vk.method("messages.send", {"peer_id": id, "message": "Произошла ошибка sy-0001-1\nInfo_questio n - значение за предалми списка!\nКод строки 832.\nКоманда \"!set question 0\" для починки.", "random_id": random.randint(1, 2147483647)})
                    
                else:
                    vk.method("messages.send", {"peer_id": id, "message": "Произошла ошибка :(\nНа вопрос небыло найдено ответа...", "random_id": random.randint(1, 2147483647)})