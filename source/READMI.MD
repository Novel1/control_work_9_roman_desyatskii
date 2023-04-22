## Инструкция по найстройке проекта

1) Создать или открыть папку куда будет копироваться проект 
2) Открыть папку и прописать команду git clone ```https://github.com/Novel1/control_work_9_roman_desyatskii.git```
3) Перейти в появившуюся папку и открыв терминал, создать виртуальное окружение командой virtualenv venv -p python
4) Активировать виртуальное окружение . venv/bin/activate
5) Установите зависимости командой pip install -r requirements.txt
6) Далее перейдите в папку source командой cd source
7) Загрузите фикстуры командой python3 manage.py loaddata fixtures/auth.json, python3 manage.py loaddata fixtires/dump.json 
8) Делаем миграцию командой ./manage.py migrate
9) И запустите приложение командой ./manage.py runserver