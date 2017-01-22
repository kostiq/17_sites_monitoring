# 17_sites_monitoring

Скрипт возвращает информацию о состоянии сайтов.
Для загрузки списка файлов, запускаем скрип с параметром -p или --path.

Для рабоыт скрипта устанавливаем зависимости из requirements.txt:

    pip3 install -r requirements.txt

Пример:  

    python3 check_sites_health.py --path sites.txt 

При нахождении неработоспособного сайта скрипт завершает свою работу.
Результат работы скрипта:

    https://pythonworld.ru/moduli/modul-datetime.html works and domain is paid!

    Care! https://docs.python.org/3/library/os.html


