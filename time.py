from datetime import datetime,timedelta

# presentDate and time

present =datetime.now()
print(present)

date=present.strftime('%d/%m/%y')
print(date)


def sleep():
    return None