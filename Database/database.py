import mysql.connector as mysql

db = mysql.connect(
    host="localhost",
    user="root",
    passwd="cuong12345",
    database="datacamp"
)
cursor = db.cursor()


def check_register(username):
    query = "SELECT * from tables where username=%s"
    cursor.execute(query, [username])
    result = cursor.fetchall()
    if result:
        print("user already exists")
    else:
        print("register")


def insert_new_account(username, password):
    query = "INSERT INTO tables(username, password) VALUES (%s,%s)"
    values = (username, password)
    cursor.execute(query, values)
    db.commit()


def check_login(username, password):
    query = "SELECT * FROM tables WHERE username = %s and password = %s"
    cursor.execute(query, [username, password])
    result = cursor.fetchall()
    if result:
        print("Logged in successfully")
    else:
        print("wrong password or username does not exist")


if __name__ == "__main__":
    check_login('123', 'hong')
    check_register('88')
# insert_new_account('hong, 'hong@0201')
