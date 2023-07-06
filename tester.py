import pytz
from colorama import init, Fore, Style
from datetime import datetime
tz_CN = pytz.timezone('Asia/Shanghai')
current_datetime = datetime.now(tz_CN)
print(Fore.RESET + "update time:" + Fore.YELLOW +  current_datetime.strftime("%H:%M:%S"))