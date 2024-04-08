from django.shortcuts import render, HttpResponse
import sqlite3
from django.db import connections
from django.db.models import QuerySet
# Create your views here.
def first_page(request):
    return render(request,'1.html')
def orders_page(request):
    # Подключаемся к базе данных
    conn = sqlite3.connect('identifier.sqlite')
    cursor = conn.cursor()

    # Выполняем SQL запрос
    query = """SELECT наименование_должности FROM Должность;"""
    cursor.execute(query)

    # Получаем результаты
    rows = cursor.fetchall()

    # Закрываем соединение с базой данных
    conn.close()

    # Преобразуем результаты в список строк
    positions = [row[0] for row in rows]
    table = '<table><tr><th>Наименование должности</th></tr>'
    for row in rows:
        table += '<tr><td>{}</td></tr>'.format(row[0])
    table += '</table>'

    return render(request, 'orders.html', {'table': table})


