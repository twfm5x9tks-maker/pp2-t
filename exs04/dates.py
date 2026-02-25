from datetime import date, timedelta, datetime

#1
today= date.today()
past=today-timedelta(days=5)
print(past)


#2
yest=today-timedelta(days=1)
tomo=today+timedelta(days=1)
print(yest, today, tomo)


#3
now=datetime.now()
nowwm=now.replace(microsecond=0)
print(nowwm)

#4
date1=datetime(2026,4,7,7,23,58)
date2=datetime(2026,7,29,13,50,37)
diff=date2-date1
sec=diff.total_seconds()
print(sec)