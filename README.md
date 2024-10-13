# Экзопланеты-рекордсмены

Удобное, интуитивно понятное представление данных с сайта "NASA Exoplanet Archive".

## Идея

Поиск экзопланет-рекордсменов по отобранным показателям.

## Задачи

1. Выбрать наиболее удобные для представления показатели.
2. Выбрать нужные колонки данных. 
3. Скачать датасет по выбранным показателям.
4. Сформировать из полученных сырых данных приемлемые для работы табличные файлы.
5. Составление таблиц по отдельным показателям (под это требуется код).
6. Написать программу для определения экзопланет-рекордсменов по выбранным показателям.
7. Проверить код на предмет недочётов и нарушений стилистики.
8. Приведение README и директории на GitHub в презентабельный вид.

## Ход работы 

В качестве предоставляемых показателей были выбраны эксцентирисет, масса, удаленность от Земли и орбитальный период.
С сайта "NASA Exoplanet Archive" были скачаны таблицы в формате xlsx с выбранными показателями. Затем эти таблицы были переформатированы в формат csv и выгружены на GitHub.

## Итоги работы

Создан код, с помощью которого пользователь может найти любое количество планет-рекордсменов (по убыванию важности) по одному из четырех показателей. 
Пользователь вводит номер интересующего показателя и затем количество планет с наибольшими результатами. Показатели распределены следующим образом:
1) планеты с наибольшим орбитальным периодом (в днях)
2) планеты с наибольшей массой (в массах Земли)
3) планеты с наибольшим эксцентриситетом
4) планеты, расположенные дальше всего от Земли (в парсеках)

Как результат работы можно также представить отобранные с помощью кода планеты-рекордсмены.
| Показатель       | Название планеты    | Значение               |
|:-----------------|:--------------------|:-----------------------|
|Орбитальный период|COCONUTS-2 b         |872000000.0 days        |
|Масса             |OGLE-2014-BLG-0221L b|30721.29382 Earth masses|
|Эксцентриситет    |GJ 317 c             |1.013                   |
|Удаленность       |MOA-2011-BLG-291L b  |10300.0 parsecs         |

## Список авторов

### Цифрами выделены выполненные человеком задачи (зоны ответственности)
- Дубинина Василиса - 2, 3, 4, 7
- Сахтарьек Зачерий - 1, 5, 6, 8

