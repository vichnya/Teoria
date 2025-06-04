## pip

# Устанавка указанного пакета
# pip install tabulate

# Вывод всех установленных пакетов
# pip freeze

# Запись всех установленных пакетов в файл определения (requirements.txt)
# pip freeze > requirements.txt

# Установка всез зависимостей из файла определения
# pip install -r requirements.txt

# Удаление установленного пакета
# pip uninstall tabulate


## venv

# Создание виртуального окружения
# python -m venv venv


## virtualvenv

# Установка 
# pip install virtualenv

# Установка иного интерпритатора
# virtualenv -p /usr/bin/python3.9 venv


## pipenv

# Установка
# pip install pipenv

# Автоматическое создание виртуального окружения, установка пакета и запись в файл определения и файл блокировки
# pipenv install tabulate

# Установка пакета и дабавление dev зависимости
# pipenv install pytest --dev

# Обновление файла блокировки
# pipenv lock 

# Удаление виртуальной среды
# pipenv –rm 




