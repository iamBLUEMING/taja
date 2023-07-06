import time
import mysql.connector
from colorama import init, Fore, Style
init()

# MySQL 연결 설정
db = mysql.connector.connect(
    host="YOURSERVERIP",
    user="david",
    password="weakpassword",
    database="dumbdb"
)
cursor = db.cursor()

string = "The quick brown fox jumps over the lazy dog and finds a hidden treasure beneath the ancient tree"
string2 = "The quick brown fox jumps over the lazy dog and finds"
string3 = "a hidden treasure beneath the ancient tree"
word_count = len(string.split())

while True:
    response = input(Fore.GREEN + '"yes"를 입력해 타자를 시작하세요, 포기하실려면 "no"를 입력해주세요: ')
    if response.lower() == 'yes':
        break
    elif response.lower() == 'no':
        print("                       ")
        print("당신은 실패작이야")
        exit()
    elif response.lower() == 'info':
        print("under development tester typerx")
        break
    else:
        print(' "yes" "no" 둘중에 하나만 하라고')

nickname = input(Fore.LIGHTYELLOW_EX + "닉네임을 입력하세요: ")  # 닉네임 입력

t0 = time.time()  # 타이머 시작
print(Fore.BLUE + string2)
print(Fore.BLUE + string3)
inputText = str(input(Fore.LIGHTBLACK_EX + '의에 표시되는 문장을 최대한 빠르게 입력해주세요: '))
t1 = time.time()  # 타이머 중지

acc = len(set(inputText.split()) & set(string.split()))
accuracy = acc / word_count * 100
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
else:
    print("타자 속도가 평균 수준입니다.")

# 결과를 데베에 저장
query = "INSERT INTO typing_results (nickname, word_per_minute, accuracy) VALUES (%s, %s, %s)"
values = (nickname, word_per_minute, accuracy)
cursor.execute(query, values)
db.commit()

db.close()
exit()
