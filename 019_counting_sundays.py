'''How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?'''

from datetime import datetime

sundays = sum(1 for y in range(1901,2001) for m in range(1,13) if datetime.strptime(f'{y}{m}1', r'%Y%m%d').weekday()==6)
print(sundays)