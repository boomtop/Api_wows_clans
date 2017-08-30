import requests
import datetime
import csv
output_file = open("Server.csv", "w")
#wrtr = csv.writer(output_file)
a = datetime.datetime.today()
print(a)
clan_id, clan_id0 = 413651, 415822
list_id = requests.get('https://api.worldofwarships.ru/wows/clans/info/?application_id=8c4db613cbca0ad5c601afcd44024acb&clan_id=413651%2C+415822')
#user_id = list_id.json()['data']
user_id = list_id.json()['data']['413651']['members_ids'] + list_id.json()['data']['415822']['members_ids']
#print(user_id)
api_info = 'https://api.worldofwarships.ru/wows/account/info/?application_id=8c4db613cbca0ad5c601afcd44024acb&account_id='

for user_id in user_id:
    r = requests.get(
        api_info + str(user_id))
    inkey = r.json()
    if inkey['data'][str(user_id)]['hidden_profile'] == False:


        nickname = inkey['data'][str(user_id)]['nickname']
        battles = inkey['data'][str(user_id)]['statistics']['battles']
        captured_points = inkey['data'][str(user_id)]['statistics']['pvp']['control_captured_points']
        dropped_points = inkey['data'][str(user_id)]['statistics']['pvp']['dropped_capture_points']
        damage_dealt = inkey['data'][str(user_id)]['statistics']['pvp']['damage_dealt']
        damage_scouting = inkey['data'][str(user_id)]['statistics']['pvp']['damage_scouting']
        planes_killed = inkey['data'][str(user_id)]['statistics']['pvp']['planes_killed']
        ships_spotted = inkey['data'][str(user_id)]['statistics']['pvp']['ships_spotted']
        aircraft_frags = inkey['data'][str(user_id)]['statistics']['pvp']['aircraft']['frags']
        main_battery_frags = inkey['data'][str(user_id)]['statistics']['pvp']['main_battery']['frags']
        ramming_frags = inkey['data'][str(user_id)]['statistics']['pvp']['ramming']['frags']
        second_battery_frags = inkey['data'][str(user_id)]['statistics']['pvp']['second_battery']['frags']
        torpedoes_frags = inkey['data'][str(user_id)]['statistics']['pvp']['torpedoes']['frags']

        stats_updated_at = inkey['data'][str(user_id)]['stats_updated_at']
        stats_updated_MSK = datetime.datetime.fromtimestamp(
                int(stats_updated_at)
            ).strftime('%Y-%m-%d %H:%M:%S')

#        output_file.write(nickname +';'+battles)

        print('Ник: ', nickname)
        print('Проведено боёв: ', battles)
        print('Очки захвата базы: ', captured_points)
        print('Очки защиты базы: ', dropped_points)
        print('Количество нанесённых повреждений: ', damage_dealt)
        print('Урон, нанесённый союзниками: ', damage_scouting)
        print('Уничтожено самолётов противника: ', planes_killed)
        print('Корабли, впервые обнаруженные игроком: ', ships_spotted)
        print('Потоплено кораблей АВ: ', aircraft_frags)
        print('Потоплено кораблей ГК: ', main_battery_frags)
        print('Потоплено кораблей Таран: ', ramming_frags)
        print('Потоплено кораблей ПМК: ', second_battery_frags)
        print('Потоплено кораблей ТА: ', torpedoes_frags)
        print('Время обновления статистики: ', stats_updated_MSK)


output_file.close()
