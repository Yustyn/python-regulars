# # Розробіть програму, яка приймає різні формати дат, та повертає кортеж (year, month, day).


# рррр. ММ. дд	2006. 05. 04	Угорщина
# рррр-ММ-дд	2006-05-04	Польща, Швеція, Литва, Канада
# рррр/ММ/дд	2006/05/04	Іран, Японія
# рррр-М-д	2006-5-4	КНР
# рррр/М/д	2006/5/4	Гонконг, Тайвань
# д.М.рррр	4.5.2006	Фінляндія, Чехія
# д-М-рррр	4-5-2006	Нідерланди
# д/М/рррр	4/5/2006	Бразилія, Греція, Таїланд
# дд.мм.рррр	04.05.2006	Болгарія, Німеччина, Норвегія, Румунія, Росія, Туреччина, Україна
# дд-ММ-рррр	04-05-2006	Данія, Португалія
# дд/ММ/рррр	04/05/2006	Велика Британія, В'єтнам, Ізраїль, Індонезія, Іспанія, Італія, Франція
# М/д/рррр	5/4/2006	США
import re


def date_getter(date):
    pattern_1 = re.compile(r"(\d{4})[-/. ]*(\d{1,2})[-/. ]*(\d{1,2})")
    pattern_2 = re.compile(r"(\d{1,2})[-/. ]*(\d{1,2})[-/. ]*(\d{4})")

    if pattern_1.match(date):
        match = pattern_1.split(date)[1:-1]
    if pattern_2.match(date):
        match = pattern_2.split(date)[1:-1]
    # print(len(match[0]))
    if len(match[0]) == 4:
        return (match[0], match[1], match[2])
    else:
        if int(match[1]) > 12:
            return (match[2], match[0], match[1])
        return (match[2], match[1], match[0])


print(date_getter("2006. 05. 04"))
print(date_getter("2006-05-04"))
print(date_getter("2006/05/04"))
print(date_getter("2006-5-4"))
print(date_getter("2006/5/4"))
print(date_getter("4.5.2006"))
print(date_getter("4-5-2006"))
print(date_getter("4/5/2006"))
print(date_getter("04.05.2006"))
print(date_getter("04-05-2006"))
print(date_getter("04/05/2006"))
print(date_getter("5/13/2006"))
