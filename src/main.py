import urllib.request
import re
import socket

URL = 'sstmk.ru'

def check_avaliability(url: str) -> bool:
    try:
        urllib.request.urlopen('https://' + url).getcode()
        return True
    except urllib.error.URLError as e:
        return False

def get_ip_address(url: str) -> str:
    if check_avaliability(url):
        return socket.gethostbyname_ex(url)[2][0]
    return 'Host unreachable'

def aquire_phone_number(url: str) -> str:
    reg_phone = re.compile(r'\+?\d{0,3}\s?\([0-9]{1,5}\)\s?[0-9]{1,3}-[0-9]{1,2}-[0-9]{1,2}')
    webpage = urllib.request.urlopen('https://' + url).read()
    try:
        phone_number = re.findall(reg_phone, str(webpage))[0]
    except IndexError:
        print('No phone numbers found on this website')
    return phone_number

def is_valid_phone_number(num: str) -> bool:
    reg_phone = re.compile(r'\+?\d{0,3}\([0-9]{1,5}\)[0-9]{1,3}-[0-9]{1,2}-[0-9]{1,2}')
    try:
        phone_str = re.findall(reg_phone, num)[0]
    except IndexError:
        return False
    if phone_str == num:
        return True
    else:
        return False

def print_corrected_phone_number(pnum: str) -> None:
    if len(re.findall(r'\d', pnum)) not in (10,11):
        print('Invalid phone number')
        return None
    if is_valid_phone_number(aquire_phone_number(URL)) is True:
        pnum = re.sub(r'\s+', '', pnum)
        print(pnum)

if __name__ == '__main__':
    #проверить, что:
    #Сайт sstmk.ru работает
    print(check_avaliability(URL))
    #Узнать ip адрес хоста sstmk.ru
    print(get_ip_address(URL))
    #С помощью GET запроса на главную страницу сайта узнать телефон компании
    print(aquire_phone_number(URL))
    #Проверить номер телефона компании на допустимость
    print(is_valid_phone_number(aquire_phone_number(URL)))
    #Вывести в стандартный вывод номер телефона компании в соответствии с вышеуказанным стандартом
    print_corrected_phone_number(aquire_phone_number(URL))
