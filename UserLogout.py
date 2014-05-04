import requests
import datetime

s = requests.Session()

while True:
    nickname = input()
    r = s.get("https://api.worldoftanks.ru/wot/account/list/", params={'application_id': '01832d316a2655bc17523d78862950fc', 'search': nickname}).json()    
    if r['status'] == 'ok':
        break

if r['count'] != 0:
    account_id = [r_data['account_id'] for r_data in r['data'] if r_data['nickname'] == nickname][0]


    r = s.get('https://api.worldoftanks.ru/wot/account/info/', params={'application_id': '01832d316a2655bc17523d78862950fc', 'account_id': account_id}).json()

    timestamp = r['data'][str(account_id)]['logout_at']  # not converted

    if timestamp:
        time_utc = datetime.datetime.utcfromtimestamp(timestamp)
        print(time_utc)
    else:
        print('Пользователь не логинился в клиент.')
else:
    print('Нет такого игрока.')