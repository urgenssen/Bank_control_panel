# Bank_control_panel
There is a remote database (Django ORM) with access data of bank personal (visits, passcards, dates etc.).

The programm helps security staff to trailing users activity on access to bank storage:

- quantity and list of all passcards;
- quantity of active passcards;
- output information by some passcard (owner's name, passcode, date of creation, status);
- list of all visits;
- list of visits without exit and information by each such visit (when entered, duration of staying);
- output information about people staying in storage at the moment (names);
- list of visits of significant passcard;
- checking the duraton of visits of significant person (more than 10 minutes, more than 1000 minutes);
- suspicious check for each visit.

There are two versions of same project.

__First version contains in folder Django-ORM-standalone.__

Here you can only launch ```main.py``` and get the result in command line. 




The script makes short links using API of [bit.ly](https://bit.ly) and writes it in terminal by user's query or counts total clicks on short links by user's query.

# How to start

Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:

```bash
pip install -r requirements.txt
```
Before running a programm you need to make a .env file in the same directory with your script.

It's recommended to use virtual environment to isolate projects files, libraries and modules.

In this file you need to put your access token (variable `BITLY_TOKEN`) for API of [bit.ly](https://bit.ly) (first - you will make an account on [bit.ly](https://bit.ly), second - you will generate an access token on [app.bitly.com/settings/api/](https://app.bitly.com/settings/api/)). 

### Run

usage: main.py [-h] url

positional arguments:
  url         Your URL or bitlink

optional arguments:
  -h, --help  show this help message and exit
  
Launch on Linux or Windows as simple

```bash
$ python main.py https://sports.ru

# You will see

$ python main.py https://sports.ru
Битлинк: https://bit.ly/3B39pze
$ python main.py https://bit.ly/3B39pze
По вашей ссылке прошли: 1 раз(а)

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
