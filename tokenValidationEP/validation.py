from datetime import datetime,timedelta

def validation(a,b,duration,created_at):
    now=datetime.now()
    time_limit=created_at+timedelta(minutes=duration)
    return (a==b and now<time_limit)