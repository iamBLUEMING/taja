import openai
import time
import mysql.connector
from colorama import init, Fore, Style
import sys
from datetime import datetime
import pytz
init()
while True:
    response = input("시작하시기 전에 먼저 SOCKS5/HTTP/HTTPS프록시 설정을 완료해주세요 - 서버IP : somestupidproxy.thisisnotrealdomain.cc | 포트 : 12345 / 또는 VPN을 활성화 해주세요 (yes or no) :")
    if response.lower() == 'yes':
        break
    elif response.lower() == 'no':
        print(" ")
        print(Fore.RED + "Accept request 'no', exiting the program" + Fore.RESET )
        exit()
    else:
        print(Fore.RED + 'Error! Please type "yes" or "no"!' + Fore.RESET)

time.sleep(int(3))

print("DB서버와 OpenAI사의 ChatGPT API에 연결을 시도 중입니다. 만약 에러가 나타나면 이 문제를 리포트 해주세요 : david@surv.ltd ")

db = mysql.connector.connect(
    host="YOURSERVERIP",
    user="david",
    password="weakpassword",
    database="dumbdb"
)
cursor = db.cursor()
openai.api_key = "sk-youneedtogetanapikeyfrom_www.openai.com___registeranaccountandgetoneforfree"

def generate_sentences():
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt="Generate a random sentence within 50 to 60 words. Don't say other things except for the sentence like dont say sure! and other stuffs only sentence.",
            max_tokens=60,
            n=1,
            stop=None,
            temperature=1.0,
            frequency_penalty=0.1,
            presence_penalty=0.0
        )
        return response.choices[0].text.strip()

string = generate_sentences()



word_count = len(string.split())
ascii_art = r'''
________________.___.__________.___ _______    ________                   
\__    ___/\__  |   |\______   \   |\      \  /  _____/                   
  |    |    /   |   | |     ___/   |/   |   \/   \  ___                   
  |    |    \____   | |    |   |   /    |    \    \_\  \                  
  |____|    / ______| |____|   |___\____|__  /\______  /                  
            \/                             \/        \/                   
____________________ ________    __________________    _____      _____   
\______   \______   \\_____  \  /  _____/\______   \  /  _  \    /     \  
 |     ___/|       _/ /   |   \/   \  ___ |       _/ /  /_\  \  /  \ /  \ 
 |    |    |    |   \/    |    \    \_\  \|    |   \/    |    \/    Y    \
 |____|    |____|_  /\_______  /\______  /|____|_  /\____|__  /\____|__  /
                  \/         \/        \/        \/         \/         \/ 
__________       .__                                 ____    _______      
\______   \ ____ |  |   ____ _____    ______ ____   /_   |   \   _  \     
 |       _// __ \|  | _/ __ \\__  \  /  ___// __ \   |   |   /  /_\  \    
 |    |   \  ___/|  |_\  ___/ / __ \_\___ \\  ___/   |   |   \  \_/   \   
 |____|_  /\___  >____/\___  >____  /____  >\___  >  |___| /\ \_____  /   
        \/     \/          \/     \/     \/     \/         \/       \/          
                                                                                  
'''
print(ascii_art)

print(Fore.LIGHTWHITE_EX + "프로그래밍동아리 타자 프로그램 정식 릴리스 v1.0 (Dev1.2) by V2 김성현 , C1 이우재, 이의찬, 김대현, 박지운, 문준서, 권오준 , G3 정필준, M1 심재연")

while True:
    response = input(Fore.GREEN + '"yes"를 입력해 타자를 시작하세요, 포기하실려면 "no"를 입력해주세요: ')
    if response.lower() == 'yes':
        break
    elif response.lower() == 'no':
        print(" ")
        print("당신은 실패작이야")
        exit()
    elif response.lower() == 'info':
        print('프로그래밍 동아리 "타자 프로그램" , under GNU General Public License v3.0')
        print('Credit : 심재연M1, Server & APIs by Survivilians® , Proxy by 蓝明网络云服务器技术和科技摔瓶子有限公司 KoreaNET')
        break
    else:
        print(' "yes" "no" 둘중에 하나만 하라고')

nickname = input(Fore.LIGHTYELLOW_EX + "닉네임을 입력하세요: ")
timewait = input('타자를 시작하기전 대기시간을 정해주세요(초) default=5 : ')
if not timewait:
    timewait = 5
print(Fore.BLUE + string)
print(Fore.LIGHTCYAN_EX + str(timewait) + '초 뒤에 위에 표시되는 문장을 타자해주세요')
time.sleep(int(timewait))

t0 = time.time()
print(Fore.LIGHTBLACK_EX + '이제 속도 계산기가 시작되었습니다. 타자를 시작해주세요')
inputText = input(Fore.LIGHTBLACK_EX + 'TYPE HERE!: ')
t1 = time.time()

input_words = inputText.split()
reference_words = string.split()
correct_word_count = 0

for input_word, reference_word in zip(input_words, reference_words):
    if input_word == reference_word:
        correct_word_count += 1

accuracy = (correct_word_count / word_count) * 100

time_taken = t1 - t0
word_per_minute = (word_count / time_taken) * 60

print(Fore.MAGENTA + " ")
print(Fore.MAGENTA + "타자 속도(WPM):", word_per_minute)
print(Fore.MAGENTA + "정확도:", accuracy, "%")
print(Fore.RESET)

if word_per_minute > 100:
    print("당신의 타자 속도가 매우 빠릅니다!")
elif word_per_minute < 10:
    print("타자 속도가 낮습니다. 조금 더 노력해보세요!")
elif word_per_minute > 60:
    print("타자 속도가 준수합니다.")
elif word_per_minute > 1000:
    print("핵쓰시네여")
else:
    print("타자 속도가 평균 입니다.")
current_date = datetime.now().date()
current_time = datetime.now().strftime('%H:%M:%S')
query = "INSERT INTO typing_results (nickname, word_per_minute, accuracy, `date`, `time`) VALUES (%s, %s, %s, %s, %s)"
values = (nickname, word_per_minute, accuracy, current_date, current_time)
cursor.execute(query, values)
db.commit()
#-----------------------------
ret1 = "Select AVG(word_per_minute) AS average from typing_results;"
cursor.execute(ret1)
rows = cursor.fetchall()
for a in rows:
    print(Fore.RESET + "현재 전학년 평균 WPM : " + Fore.CYAN + str(a[0]))
#-------------
ret2 = "Select AVG(accuracy) AS average from typing_results;"
cursor.execute(ret2)
rows = cursor.fetchall()
for b in rows:
    print(Fore.RESET + "현재 전학년 평균 정확도 : " + Fore.LIGHTCYAN_EX + str(b[0]))

#TIME!
tz_CN = pytz.timezone('Asia/Shanghai')
current_datetime = datetime.now(tz_CN)
print(Fore.RESET + "'현재' 가 뜻하는 시간 : "+ Fore.YELLOW +  current_datetime.strftime("%H:%M:%S"))



while True:
    response = input(Fore.RESET + '결과가 DB에 성공적으로 업로드 되었습니다. 아무 키를 눌러 종료하세요')
    if response.lower() != 'no':
        break

print("    ")
print(Fore.LIGHTGREEN_EX + "ByeBye")
db.commit()
db.close()
sys.exit()
