# import datetime
# import time
# import csv
# from django import get_or_create
#
# def concat_datetime(string_date, string_time):
#     date = datetime.datetime.strptime(string_date, "%Y-%m-%d")
#     time = datetime.datetime.strptime(string_time, "%H:%M").time()
#     dt = datetime.datetime.combine(date, time)
#     return dt
#
# def upload_microstation(path):
#     with open(path) as f:
#         reader = csv.reader(f)
#         for row in reader:
#             objs, created = get_or_create()
