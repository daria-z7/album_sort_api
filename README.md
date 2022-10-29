##  Проект  album_sort_api

### Описание проекта:

На главной странице приложения выводится таблица с информацией об альбомах, исполнителях и треках. Реализована сортировка данных по кнопке для столбцов name и artist@name.

### Технологии:

При реализации проекта были использованы следующие основные технологии, фреймворки и библиотеки:
- Python 3.7
- Django 3.2
- Django Rest FrameWork 3.12.4

### Как запустить проект:
Клонируйте репозиторий и перейдите в него в командной строке:

```
git clone 'ссылка на репозиторий'
```

```
cd album_sort_api
```

Cоздайте и активируйте виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```
```
python -m pip install --upgrade pip
```

Установите зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполните миграции:

```
python manage.py migrate
```
Создайте суперпользователя:

```
python manage.py createsuperuser
```

Запустите проект:

```
python manage.py runserver
```

Перейдите по ссылке в админку и наполните таблицы данными:

```
http://127.0.0.1:8000/admin/
```

Перейдите по ссылке:

```
http://127.0.0.1:8000/api/albums/
```


### Автор проекта:
- Зайцева Дарья
