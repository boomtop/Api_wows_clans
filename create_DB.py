# -*- coding: utf-8 -*-
import sqlite3
#Подключение к базе
conn = sqlite3.connect('clan.db')
#Создание курсора
c = conn.cursor()
c.execute('''CREATE TABLE clan_users (Ник varchar,Проведено_боёв varchar,Очки_захвата_базы varchar,
                  Очки_защиты_базы varchar,Количество_нанесённых_повреждений varchar,Урон_нанесённый_союзниками varchar,
                  Уничтожено_самолётов_противника varchar,Корабли_впервые_обнаруженные_игроком varchar,
                  Потоплено_кораблей_АВ varchar,Потоплено_кораблей_ГК varchar,Потоплено_кораблей_Таран varchar,Потоплено_кораблей_ПМК varchar,
                  Потоплено_кораблей_ТА varchar, Время_обновления_статистики varchar)''')