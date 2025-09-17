from fastapi import FastAPI
import pymysql

app = FastAPI()

# 데이터베이스 연결 함수
def get_connection():
    return pymysql.connect(
        host="localhost",     # MySQL 서버 주소
        user="root",          # 사용자
        password="",      # 비밀번호
        database="testdb",    # 사용할 DB 이름
        cursorclass=pymysql.cursors.DictCursor
    )

@app.get("/")
def read_root():
    return {"Hello": "MySQL"}

@app.get("/users")
def read_users():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, email FROM users;")
    rows = cursor.fetchall()
    conn.close()
    return rows
