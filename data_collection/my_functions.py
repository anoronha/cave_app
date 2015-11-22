import datetime
import time

def concat_datetime(string_date, string_time):
    date = datetime.datetime.strptime(string_date, "%Y-%m-%d")
    time = datetime.datetime.strptime(string_time, "%H:%M").time()
    dt = datetime.datetime.combine(date, time)
    return dt
