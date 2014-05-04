import requests
import datetime

s = requests.Session()

application_id = '01832d316a2655bc17523d78862950fc'

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

if r['count'] != 0:
    account_id = [r_data['account_id'] for r_data in r['data'] if r_data['nickname'] == nickname][0]


    r = s.get('https://api.worldoftanks.ru/wot/account/info/', params={'application_id': application_id, 'account_id': account_id}).json()

    timestamp = [r['data'][str(account_id)]['logout_at'], r['data'][str(account_id)]['last_battle_time']]  # not converted

    if timestamp:
        time_utc = list(map(datetime.datetime.utcfromtimestamp, timestamp))
        print('last_battle_time: ', time_utc[1])
        print('logout_at: ', time_utc[0])
    else:
        print('Пользователь не логинился в клиент.')
else:
    print('Нет такого игрока.')