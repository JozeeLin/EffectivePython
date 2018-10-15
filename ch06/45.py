#!/usr/bin/env python
# coding=utf-8

from time import localtime, strftime
from time import mktime, strptime
from datetime import datetime, timezone
import pytz


now = 1407694710

local_tuple = localtime(now)
time_format = '%Y-%m-%d %H:%M:%S'
time_str = strftime(time_format, local_tuple)
# 1======================
#print(time_str)


time_tuple = strptime(time_str, time_format)
utc_now = mktime(time_tuple)
# 2=======================
#print(utc_now)


# 3=======================
now = datetime(2014,8,10,18,18,30)
now_utc = now.replace(tzinfo=timezone.utc)
now_local = now_utc.astimezone()
#print(now_local)

# 4=======================
time_str = '2014-08-10 11:18:30'
now = datetime.strptime(time_str, time_format)
time_tuple = now.timetuple()
utc_now = mktime(time_tuple)
#print(utc_now)


# 5=======================
arrival_nyc = '2014-05-01 23:33:24'
nyc_dt_naive = datetime.strptime(arrival_nyc, time_format)
eastern = pytz.timezone('US/Eastern')
nyc_dt = eastern.localize(nyc_dt_naive)
utc_dt = pytz.utc.normalize(nyc_dt.astimezone(pytz.utc))
print(utc_dt)

pacific = pytz.timezone('US/Pacific')
sf_dt = pacific.normalize(utc_dt.astimezone(pacific))
print(sf_dt)

nepal = pytz.timezone('Asia/Katmandu')
nepal_dt = nepal.normalize(utc_dt.astimezone(nepal))
print(nepal_dt)

