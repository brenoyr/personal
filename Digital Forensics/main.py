import csv
from datetime import datetime
import pytz

# pytz used to convert timestamp into aware datetime in python 2.7
# aware time is what allows format to be changed into a different time zone with pytz

names = []
passwords = []
times = []

forSkip = 0
with open('database_dump.csv', mode='r') as csvfile:
    entries = csv.reader(csvfile, delimiter=',')
    for row in entries:
        if forSkip == 0:
            forSkip += 1
            continue
        else:
            names.append(row[0])
            passwords.append(row[1])
            # times.append(row[2])
            # print row[2]

            dt = datetime.fromtimestamp(float(row[2]), pytz.utc)    # pytz.utc used to make time "aware"
            time = dt.astimezone(pytz.timezone('US/Mountain'))      # Mountain time zone used to account for DST on Central Time
            times.append(time)

with open('decrypted.csv', mode='w') as decrypted_file:
    entries = csv.writer(decrypted_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)

    for n in range(len(names)):
        entries.writerow(['John', '1234', times[n]])

        