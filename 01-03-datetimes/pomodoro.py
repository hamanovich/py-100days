from datetime import timedelta
import time

mins = 5
duration = mins * 60

while True:
    print(timedelta(seconds=duration))
    duration -= 1
    if duration < 0:
        break
    time.sleep(1)

print('Time\'s Up')
