#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import datetime
import time
import datetime

s = requests.Session()

application_id = '01832d316a2655bc17523d78862950fc'
last_battle_time = ''
logout_at = ''



while True:
    print('Введите ник для поиска:')
    nickname = input()
    r = s.get("https://api.worldoftanks.ru/wot/account/list/", params={'application_id': application_id, 'search': nickname}).json()    
    if r['status'] == 'ok'and r['count'] == 0:
        print('Не нашел такого игрока. :(')
    elif r['status'] == 'ok':
        break
    else:
        print('Поисковая строка не должна быть Null или меньше 3 символов.')

f_name = str(nickname) + '_session_log.txt'
print(f_name)
f = open(f_name, 'a')

if r['count'] != 0:
    
    account_id = [r_data['account_id'] for r_data in r['data'] if r_data['nickname'] == nickname][0]

    while True:
        r = s.get('https://api.worldoftanks.ru/wot/account/info/', params={'application_id': application_id, 'account_id': account_id}).json()

        timestamp = [r['data'][str(account_id)]['logout_at'], r['data'][str(account_id)]['last_battle_time']]  # not converted

        if timestamp:
            time_utc = list(map(datetime.datetime.utcfromtimestamp, timestamp))

            if last_battle_time != str(time_utc[1]):
                now_time = datetime.datetime.now()
                log_data = str(now_time) + ' last_battle_time: ' + str(time_utc[1])
                print(log_data)
                f.write(log_data + '\n')
            if logout_at != str(time_utc[0]):
                now_time = datetime.datetime.now()
                log_data = str(now_time) + ' logout_at: ' + str(time_utc[0])
                print(log_data)
                f.write(log_data + '\n')
            last_battle_time = str(time_utc[1])
            logout_at = str(time_utc[0])

        else:
            print('Пользователь не логинился в клиент.')
        time.sleep(15)

else:
    print('Нет такого игрока.')