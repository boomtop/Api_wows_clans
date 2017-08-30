import requests
import datetime
import csv
import sqlite3

print('Start ', datetime.datetime.today())

conn = sqlite3.connect('clan.db')
c = conn.cursor()



out_file = 'Server.csv'
list_id = requests.get(
    'https://api.worldofwarships.ru/wows/clans/info/?application_id=8c4db613cbca0ad5c601afcd44024acb&clan_id=413651%2C+415822')
users_id = list_id.json()['data']['413651']['members_ids'] + list_id.json()['data']['415822']['members_ids']
str_users = '%2C+'.join(str(v) for v in users_id)
#print(str_users)
api_info_all = requests.get(
    'https://api.worldofwarships.ru/wows/account/info/?application_id=8c4db613cbca0ad5c601afcd44024acb&account_id=%s'
            %(str_users))
statistic_all = api_info_all.json()
print(statistic_all)
list_export_for_csv = []
for user_id in users_id:
    if not statistic_all['data'][str(user_id)]['hidden_profile']:
        nickname = statistic_all['data'][str(user_id)]['nickname']
        battles = statistic_all['data'][str(user_id)]['statistics']['battles']
        captured_points = statistic_all['data'][str(user_id)]['statistics']['pvp']['control_captured_points']
        dropped_points = statistic_all['data'][str(user_id)]['statistics']['pvp']['dropped_capture_points']
        damage_dealt = statistic_all['data'][str(user_id)]['statistics']['pvp']['damage_dealt']
        damage_scouting = statistic_all['data'][str(user_id)]['statistics']['pvp']['damage_scouting']
        planes_killed = statistic_all['data'][str(user_id)]['statistics']['pvp']['planes_killed']
        ships_spotted = statistic_all['data'][str(user_id)]['statistics']['pvp']['ships_spotted']
        aircraft_frags = statistic_all['data'][str(user_id)]['statistics']['pvp']['aircraft']['frags']
        main_battery_frags = statistic_all['data'][str(user_id)]['statistics']['pvp']['main_battery']['frags']
        ramming_frags = statistic_all['data'][str(user_id)]['statistics']['pvp']['ramming']['frags']
        second_battery_frags = statistic_all['data'][str(user_id)]['statistics']['pvp']['second_battery']['frags']
        torpedoes_frags = statistic_all['data'][str(user_id)]['statistics']['pvp']['torpedoes']['frags']
        stats_updated_at = statistic_all['data'][str(user_id)]['stats_updated_at']
        stats_updated_MSK = datetime.datetime.fromtimestamp(
            int(stats_updated_at)).strftime('%Y-%m-%d %H:%M:%S')
        list_export = [nickname, battles, captured_points, dropped_points,
                       damage_dealt, damage_scouting, planes_killed,
                       ships_spotted, aircraft_frags, main_battery_frags,
                       ramming_frags, second_battery_frags, torpedoes_frags,
                       stats_updated_at, stats_updated_MSK]
        list_export_for_csv.append(list_export)

        c.execute("INSERT INTO clan_users (Ник,Проведено_боёв,Очки_захвата_базы,"
                  "Очки_защиты_базы,Количество_нанесённых_повреждений,Урон_нанесённый_союзниками,"
                  "Уничтожено_самолётов_противника,Корабли_впервые_обнаруженные_игроком,"
                  "Потоплено_кораблей_АВ,Потоплено_кораблей_ГК,Потоплено_кораблей_Таран,Потоплено_кораблей_ПМК,"
                  "Потоплено_кораблей_ТА, Время_обновления_статистики) VALUES ('%s','%s','%s','%s','%s','%s','%s',"
                  "'%s','%s','%s','%s','%s','%s','%s')" % (nickname, battles, captured_points,
                                                                                    dropped_points, damage_dealt,
                                                                                    damage_scouting, planes_killed,
                                                                                    ships_spotted, aircraft_frags,
                                                                                    main_battery_frags, ramming_frags,
                                                                                    second_battery_frags, torpedoes_frags,
                                                                                    stats_updated_MSK
                                                                                    ))
        conn.commit()

        c.execute('SELECT * FROM clan_users')
        row = c.fetchone()

        while row is not None:
            print("id:" + str(row[0]) + " Логин: " + row[1] + " | Пароль: " + row[2])
            row = c.fetchone()

print(list_export_for_csv)
print('END ', datetime.datetime.today())

c.close()
conn.close()
