import os
import re

HTML_URL = os.path.join(os.path.dirname(__name__), '..', 'tmp', 'redux.html')
time_regex = re.compile(r'\d+:\d{2}')


def main():
    time_list = get_time_from_markup()
    total_min, total_sec = calculate_time(time_list)
    result = total_time(total_min, total_sec)
    print(f'The course takes {result:.2f} hours to complete')


def get_time_from_markup(url=HTML_URL):
    with open(url) as f:
        times = [time_regex.search(line).group()
                 for line in f if time_regex.search(line)]

    return times


def calculate_time(durations):
    sum_minutes = 0
    sum_seconds = 0
    for i in range(len(durations)):
        minutes, seconds = durations[i].split(':')
        sum_minutes = sum_minutes + int(minutes)
        sum_seconds = sum_seconds + int(seconds)

    return sum_minutes, sum_seconds


def total_time(total_min, total_sec):
    return float(total_min / 60 + total_sec / 3600)


if __name__ == "__main__":
    main()
