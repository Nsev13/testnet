## Тестовое задание:

С помощью языка Python 3 написать скрипт и проверить, что:

- Сайт sstmk.ru работает

- Узнать ip адрес хоста sstmk.ru

- С помощью GET запроса на главную страницу сайта узнать телефон компании

- Проверить номер телефона компании на допустимость по следующему стандарту: +A(BBB)CCC-CC-CC, где А – код страны, от одной до трех цифр (эта часть номера не обязательна); ВВВ – код города или зоны (число цифр может быть отлично от трех); CCC-CC-CC – номер телефона (число цифр может быть отлично от семи). Примеры допустимых номеров: +7(495)222-22-22, (495)222-22-22, (34111)2-22-22.

- Вывести в стандартный вывод номер телефона компании в соответствии с вышеуказанным стандартом

Код должен запускаться на персональном компьютере с операционной системой Ubuntu 22.04.1 LTS и работать под управлением стандартного интерпретатора Python 3. В случае использования дополнительных модулей необходимо обеспечить их работу и запуск из виртуальной среды

## Ход работ

Для выполнения задания была создана виртуальная машина под гипервизопом `VMware` с ОС `Ubuntu 22.04.1` и был использован `python` версии `3.10`, поставляемый с данной ОС.

![alt text](https://github.com/Nsev13/testnet/blob/master/Screenshots/%D0%92%D0%B5%D1%80%D1%81%D0%B8%D1%8F%20%D0%9E%D0%A1%20ubuntu.jpg)

Затем было создано виртуальное пространство `python` с помощью `venv` (пакет `python3.10-venv`), проверена корректная структура директории, содержащей в себе файлы виртуального пространста, и был создан файл `main.py`, который запускался для выполнения задания.

![alt text](https://github.com/Nsev13/testnet/blob/master/Screenshots/%D0%A1%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%20%D0%B2%D0%B8%D1%80%D1%82%D1%83%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D0%B3%D0%BE%20%D0%BF%D1%80%D0%BE%D1%81%D1%82%D1%80%D0%B0%D0%BD%D1%81%D1%82%D0%B2%D0%B0%20venv.jpg)

Вывод работы скрипта представлен ниже.

![alt text](https://github.com/Nsev13/testnet/blob/master/Screenshots/%D0%92%D1%8B%D0%B2%D0%BE%D0%B4%20%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D1%8B.jpg)

Каждая строчка вывода отвечает за соответсвующий вопрос из тестового задания.
Для каждого задания были написаны свои функции с приведенной типизацией.

![alt text](https://github.com/Nsev13/testnet/blob/master/Screenshots/%D0%9A%D0%BE%D0%B4%20%D1%81%D0%BA%D1%80%D0%B8%D0%BF%D1%82%D0%B0%20main.py.jpg)

Код можно посмотреть в репозитории по пути `./src/main.py`
