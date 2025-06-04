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

# venv\Scripts\activate - для windows
# source venv/bin/activate - для macOS/Linux

# deactivate - для выхода из виртуального окружения


## virtualvenv

# Установка 
# pip install virtualenv

# Создание среды
# virtualenv venv

# Установка иного интерпритатора
# virtualenv -p "C:\Users\89128\AppData\Local\Programs\Python\Python311\python.exe" venv


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
# Проверка - pipenv --venv

# Установка среды строго по файлу блокировки
# pipenv install --ignore-pipfile 


## Poetry

# Установка Poetry
# curl -sSL https://install.python-poetry.org | python3 –

# Добавляет зависимости и обновляет pyproject.toml и poetry.lock
# poetry new my_project1966

# Добавляет зависимости и обновляет pyproject.toml и poetry.lock (dev)
# poetry add --dev pytest  

# Создаёт или обновляет файл poetry.lock, фиксируя все версии (включая транзитивные)
# poetry lock 

# Cоздаёт виртуальную среду и устанавливает зависимости строго по poetry.lock
# poetry install 

# Публикация пакета
# poetry build
# poetry publish 

# Удаление виртуальной среды
# poetry env remove python

## uv

# Установка
# для macOS/Linux: curl -Ls https://astral.sh/uv/install.sh | bash
# для Windows нужно скачать zip, распаковать его и указать к нему путь в переменных средах: https://github.com/Astral-sh/uv/releases

# Создание виртуальной среды:
# uv venv

# Создание виртуальной среды с другим интерпритатором 
# uv venv --python 3.11 

# Инициализация проекта
# uv init

# устанавливает зависимости, как pip, но быстрее и с кэшированием
# uv pip install tabulate

# Аналогично pip freeze, но поддерживает строгую фиксацию всех транзитивных зависимостей
# uv pip freeze > requirements.lock.txt 

# Удаляет все лишние пакеты и устанавливает только из файла определния
# uv pip sync requirements.txt 

# Сборка и публикация

# uv build
# uv publish 
