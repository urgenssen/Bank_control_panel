# Bank control panel
There is a remote database (Django ORM) with access data of bank personal (visits, passcards, dates and etc.).

The program helps security staff to trailing users activity on access to bank storage:

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

<ins>*First version* contains in folder __Django-ORM-standalone.__</ins>

This version allows you to get access to remote database (see ```settings.py``` for data connection) and displays mentioned above data in terminal.

<ins>*Second version* contains in folder __Django-orm-watching-storage.__</ins>

This version allows you to get access to remote database (see ```settings.py``` for data connection) and displays mentioned above data on local web-site directly in your browser that makes perception more clear, understandable and allows to choose information by each user only by hand (while in first version you have to change the script if you want to obtain information of another user).


# How to start

First, you have to download this repository.

Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:

```bash
pip install -r requirements.txt
```

It's recommended to use virtual environment to isolate projects files, libraries and modules.


### Run

For __Django-ORM-standalone:__

usage: main.py
  
Launch on Linux or Windows as simple

```bash
$ python main.py

# You will see

$ Task #1:
Количество пропусков: 100

Task #2:
<QuerySet [<Passcard: Jennifer Martin>, <Passcard: Breanna Campbell>, <Passcard: Susan Long>, <Passcard: Derrick Watts>, <Passcard: Katherine Johnson>, <Passcard: Bobby Stafford>, <Passcard: Barbara Beck>, <Passcard: Renee Sexton>, <Passcard: Glenda Mitchell>, <Passcard: Rebecca Hill>, <Passcard: David Wilson>, <Passcard: Samantha Smith>, <Passcard: John Zhang>, <Passcard: Micheal Melton>, <Passcard: Tricia Parker>, <Passcard: Gabrielle Davis>, <Passcard: Phillip Harrison>, <Passcard: Ashley Bartlett>, <Passcard: Gregory Thompson>, <Passcard: Andre Adams>, '...(remaining elements truncated)...']>

Task #3:
owner_name: Jennifer Martin
passcode: ceb148a6-fb27-4106-890c-89dc8cedfe83
created_at: 2018-01-11 12:28:39+00:00
is_active: True

...
```

For __Django-orm-watching-storage:__

usage: main.py
  
Launch on Linux or Windows as simple

```bash
$ python main.py

# You will see

Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
January 21, 2023 - 14:19:33
Django version 3.2, using settings 'project.settings'
Starting development server at http://0.0.0.0:8000/
Quit the server with CTRL-BREAK.

```
It will launch your local web-server.

And you need to go at http://127.0.0.1:8000/ at your web-browser where you will operate with database's interface:


![web_1](https://user-images.githubusercontent.com/45304364/213862720-04289a6e-0281-43e1-9838-0914fd9dc920.png)


![web_2](https://user-images.githubusercontent.com/45304364/213862724-c6a955ce-ba23-4c0f-abb1-334917478ed0.png)


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
