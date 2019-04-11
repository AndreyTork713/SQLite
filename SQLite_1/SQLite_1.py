import sqlite3


conn = sqlite3.connect('Chinook_Sqlite.db') # Подключение к базе данных

cursor = conn.cursor()  #Создание объекта курсор

#********** ЧТЕНИЕ ИЗ БАЗЫ **********
# Делаем SELECT запрос к базе данных, используя обычный SQL-синтаксис
cursor.execute("SELECT Name FROM Artist ORDER BY Name LIMIT 3")

results = cursor.fetchall()
results1 = cursor.fetchall()

print(results)
print(results1)

#***********************************
#********** ЗАПИСЬ В БАЗУ **********
# Делаем INSERT запрос к базе данных, используя обычный SQL-синтаксис
cursor.execute("insert into Artist values (Null,'Aagrh!')")
# Если мы не просто читаем, но и вносим изменения в базу данных - необходимо сохранить транзакцию
conn.commit()

#********* Проверка результатов *********
cursor.execute("SELECT Name FROM Artist ORDER BY Name LIMIT 3")

results = cursor.fetchall()
print(results)


conn.close()

