import json
import requests as request
# criar um pequeno crud que me permita ver a temperatura do dia 
# menu

def menu():
    while True:
        print("Bem-vindo ao sistema de previsão do tempo!")
        print("1. Ver temperatura do dia")
        print("2. Sair")
        escolha = input("Escolha uma opção: ")
        
        if escolha.strip() == '':
            print('Escolha uma opção valida')
        else:
            if escolha == '1':
                cidade = input("Digite o nome da cidade: ")
            # consumir uma api de previsão do tempo
            API_KEY = 'YOUR_KEY'
            url = f'https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={cidade}&aqi=yes'
            get = request.get(url)
            if get.status_code == 200:
                data = json.loads(get.text)
                temperatura = data['current']['temp_c']
                print(f'A temperatura atual em {cidade} é de {temperatura}°C')
            if get.status_code == 400:
                print('Cidade não encontrada')
        if escolha == '2':
            print('Saindo do sistema...')
            break
if __name__ == '__main__':
    print(menu())