'''Extract datetimes from log entries and calculate the time
   between the first and last shutdown events'''
from datetime import datetime
import os
import urllib.request

SHUTDOWN_EVENT = 'Shutdown initiated'

logfile = os.path.join(os.path.dirname(__file__), '..', 'tmp', 'log')

urllib.request.urlretrieve('http://bit.ly/2AKSIbf', logfile)


def main():
    print(convert_to_datetime(loglines[6]))
    print(convert_to_datetime(loglines[10]))
    print(time_between_shutdowns(loglines))


with open(logfile) as f:
    loglines = f.readlines()


def convert_to_datetime(line):
    '''TODO 1:
       Given a log line extract its timestamp and convert it to a datetime object. 
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)'''
    log_date = line.split()[1]
    date_format = '%Y-%m-%dT%H:%M:%S'
    return datetime.strptime(log_date, date_format)


def time_between_shutdowns(loglines):
    '''TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and calculate the 
       timedelta between the first and last one. 
       Return this datetime.timedelta object.'''
    shut_lines = [
        l.strip()
        for l in loglines
        if SHUTDOWN_EVENT in l
    ]
    shut_times = [
        convert_to_datetime(event)
        for event in shut_lines
    ]
    return max(shut_times) - min(shut_times)


if __name__ == "__main__":
    main()
