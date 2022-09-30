from datetime import datetime

if datetime.today().month >= 10:
    print(f'{datetime.today().year}-{datetime.today().month}-{datetime.today().day}')
else:
    print(f'{datetime.today().year}-0{datetime.today().month}-{datetime.today().day}')