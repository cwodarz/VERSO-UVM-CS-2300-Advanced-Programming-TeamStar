# this file takes a date in string form and formats it to be printed
from datetime import datetime

date_str = "2022-03-17 10:45:30"
date_obj = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
formatted_date = date_obj.strftime('%m/%d/%Y %H:%M:%S')

# changed print statement
print(formatted)
