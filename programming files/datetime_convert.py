# bugs introduced by cam
# this file takes a date in string form and formats it to be printed
from datetime import datetime

date_str = "2022-03-17 10:45:30"
date_obj = datetime.strptime(date_str, '%Y-m-%d %H:%M:%S') # removed the % before the m 
formattted_date = date_obj.strftime('%m/%d/%Y %H:%M:%S')  # added an extra t in formatted

print(formatted_date)
