import aiocron

# Если удалить эту задачу и оставить файлик пустым, то будет ошибка: 
# DeprecationWarning: There is no current event 
# Это не повлияет на работу бота. Происходит это из за того что aiocron под капотом
# Создает свой Event Loop а мы в main.py файле к нему подключемся что бы наши задачи отрабатывали.

# Время указывать так: "{MIN} {HOURS} * * *"
@aiocron.crontab("0 0 * * *")
async def scare_task():
    print("БУ!")