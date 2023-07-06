import mysql.connector

# MySQL 연결 설정
db = mysql.connector.connect(
    host="YOURSERVERIP",
    user="david",
    password="weakpassword",
    database="dumbdb"
)
cursor = db.cursor()

# 커서 생성
cursor = db.cursor()

# typing_results 테이블 생성 쿼리
create_table_query = """
CREATE TABLE typing_results (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nickname VARCHAR(255),
    word_per_minute FLOAT,
    accuracy FLOAT
)
"""

# typing_results 테이블 생성
cursor.execute(create_table_query)
print("typing_results 테이블이 성공적으로 생성되었습니다.")

# 삽입할 데이터
nickname = "John"
word_per_minute = 60.0
accuracy = 80.0

# INSERT 쿼리와 값 설정
insert_query = """
INSERT INTO typing_results (nickname, word_per_minute, accuracy)
VALUES (%s, %s, %s)
"""
values = (nickname, word_per_minute, accuracy)

# 데이터 삽입
cursor.execute(insert_query, values)
db.commit()
print("데이터가 성공적으로 삽입되었습니다.")

# 연결 종료
cursor.close()
db.close()
