#! Ver 1.1 beta

import time
import mysql.connector
from colorama import init, Fore, Style
import sys
from datetime import datetime
init()

# MySQL 연결 설정
db = mysql.connector.connect(
    host="YOURSERVERIP",
    user="david",
    password="weakpassword",
    database="dumbdb"
)
cursor = db.cursor()
openai.api_key = "sk-youneedtogetanapikeyfrom_www.openai.com___registeranaccountandgetoneforfree"

string = "The quick brown fox jumps over the lazy dog and finds a hidden treasure beneath the tree"
string2 = "The quick brown fox jumps over the lazy dog and finds"
string3 = "a hidden treasure beneath the tree"
word_count = len(string.split())

ascii_art = r'''
 _________    ___    ___ ________  _______   ________     ___    ___              
|\___   ___\ |\  \  /  /|\   __  \|\  ___ \ |\   __  \   |\  \  /  /|             
\|___ \  \_| \ \  \/  / | \  \|\  \ \   __/|\ \  \|\  \  \ \  \/  / /             
     \ \  \   \ \    / / \ \   ____\ \  \_|/_\ \   _  _\  \ \    / /              
      \ \  \   \/  /  /   \ \  \___|\ \  \_|\ \ \  \\  \|  /     \/               
       \ \__\__/  / /      \ \__\    \ \_______\ \__\\ _\ /  /\   \               
        \|__|\___/ /        \|__|     \|_______|\|__|\|__/__/ /\ __\              
            \|___|/                                      |__|/ \|__|              
                                                                                  
                                                                                  
 ________  _______   ___      ___      _________  _______   ________  _________   
|\   ___ \|\  ___ \ |\  \    /  /|    |\___   ___\\  ___ \ |\   ____\|\___   ___\ 
\ \  \_|\ \ \   __/|\ \     \ \  \ 
   \ \_______\ \_______\ \__/ /              \ \__\ \ \_______\____\_\  \   \ \__\
    \|_______|\|_______|\|__|/                \|__|  \|_______|\_________\   \|__|
                                                              \|_________|        \  /  / /    \|___ \  \_\ \   __/|\ \  \___|\|___ \  \_| 
 \ \  \ \\ \ \  \_|/_\ \  \/  / /          \ \  \ \ \  \_|/_\ \_____  \   \ \  \  
  \ \  \_\\ \ \  \_|\ \ \    / /            \ \  \ \ \  \_|\ \|____|\  \
                                                                                  
'''

print(ascii_art)
print(Fore.LIGHTWHITE_EX + "코딩동아리 타자대회 내부 테스트 프로그램 버전 1.1 - 5월29일")


while True:
    response = input(Fore.GREEN + '"yes"를 입력해 타자를 시작하세요, 포기하실려면 "no"를 입력해주세요: ')
    if response.lower() == 'yes':
        break
    elif response.lower() == 'no':
        print("                       ")
        print("당신은 실패작이야")
        exit()
    elif response.lower() == 'info':
        print("under development tester typer")
        break
    else:
        print(' "yes" "no" 둘중에 하나만 하라고')

nickname = input(Fore.LIGHTYELLOW_EX + "닉네임을 입력하세요: ")  # 닉네임 입력

t0 = time.time()  # 타이머 시작
print(Fore.BLUE + string2)
print(Fore.BLUE + string3)
inputText = str(input(Fore.LIGHTBLACK_EX + '의에 표시되는 문장을 최대한 빠르게 입력해주세요: '))
t1 = time.time()  # 타이머 중지

input_words = inputText.split()
reference_words = string.split()
correct_word_count = 0

for input_word, reference_word in zip(input_words, reference_words):
    if input_word == reference_word:
        correct_word_count += 1

accuracy = (correct_word_count / word_count) * 100

time_taken = t1 - t0
word_per_minute = (word_count / time_taken) * 60

print(Fore.MAGENTA + "----------------------")
print(Fore.MAGENTA + "타자 속도(WPM):", word_per_minute)
print(Fore.MAGENTA + "정확도:", accuracy, "%")
print(Fore.RESET)

# 타자 수듄
if word_per_minute > 100:
    print("당신의 타자 속도가 매우 빠릅니다!")
elif word_per_minute < 10:
    print("타자 속도가 낮습니다. 조금 더 노력해보세요!")
elif word_per_minute > 60:
    print("타자 속도가 준수합니다.")
elif word_per_minute > 1000:
    print("핵쓰시네여")
else:
    print("타자 속도가 평균 수준입니다.")

# 결과를 데베에 저장

current_date = datetime.now().date()
current_time = datetime.now().strftime('%H:%M:%S')

query = "INSERT INTO typing_results (nickname, word_per_minute, accuracy, `date`, `time`) VALUES (%s, %s, %s, %s, %s)"
values = (nickname, word_per_minute, accuracy, current_date, current_time)
cursor.execute(query, values)
db.commit()

while True:
    response = input(Fore.WHITE + '결과가 Survivilians의 DB에 성공적으로 업로드 되었습니다. 아무 키를 눌러 종료하세요')
    if response.lower() != 'no':
        break

print("    ")
print(Fore.LIGHTGREEN_EX + "We'll see you next time")
db.close()
sys.exit()
