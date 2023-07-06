import time
import mysql.connector
from colorama import init, Fore, Style
init()

string = "The quick brown fox jumps over the lazy dog and finds a hidden treasure beneath the ancient tree"
string2 = "The quick brown fox jumps over the lazy dog and finds"
string3 = "a hidden treasure beneath the ancient tree"
#여기서 정확도와 속도 계산은 string만 사용 하고 string2&3는 오직 긴 문장을 위해 표시 용도입니다
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
    elif response.lower() == '커스텀':
        print("메세지")
        break
#커스텀에다가 명령어를 넣고 메세지에 보내고 싶은 print를 넣어 이스터에그를 만드세요!
    else:
        print(' "yes" "no" 둘중에 하나만 하라고')


t0 = time.time()  # 타이머시작
print(Fore.BLUE + string2)
print(Fore.BLUE + string3)
inputText = str(input(Fore.LIGHTBLACK_EX + '의에 표시되는 문장을 최대한 빠르게 입력해용 : '))
t1 = time.time()  # 타이머중지

acc = len(set(inputText.split()) & set(string.split()))
accuracy = acc / word_count * 100 
time_taken = t1 - t0
word_per_minute = (word_count / time_taken) * 60

print(Fore.MAGENTA + "----------------------")

print(Fore.MAGENTA + "당신의 WPM :", word_per_minute)
print(Fore.MAGENTA + "정확도:", accuracy,"%")
print(Fore.RESET)

#타자레벨

if word_per_minute > 100:
    print("당신 타자속도가 존나 빠르군?")
elif word_per_minute < 10:
    print("님 사람임?")
elif word_per_minute > 60:
    print("타자속도가 준수합니다")
else:
    print("타자속도가 평균입니다")

exit()

