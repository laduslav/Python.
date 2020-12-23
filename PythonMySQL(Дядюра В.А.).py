import mysql.connector as sql

mydb = sql.connect(
    host = '192.168.137.131',
    user = 'root',
    passwd = 'Dkflbckfd2312',
    database = 'mydb'
)
mycursor = mydb.cursor()

print('Программа была создана Владиславом Дядюрой.')
print ('Вот ваша база данных:')
mycursor.execute('SELECT * FROM students')
myresult = mycursor.fetchall()
for row in myresult:
    print (row)
print('Для изменения базы данных напишите "Change"')
print('Для добавления нового студента в базу данных напишите "New"')

a = input()

if a == 'Change':
    print('Введите номер студента в списке:')
    number = input()
    print('Если вы хотите изменить его логин, введите "Логин"')
    print('Если вы хотите изменить его пароль, введите "Пароль"')
    change = input()
    if change == 'Логин':
        print('Введите новый логин студента:')
        changeLogin = input()
        mycursor.execute("UPDATE `mydb`.`students` SET `Login` = '" + changeLogin + "' WHERE (`Students` = '" + number + "')")
    if change == 'Пароль':
        print('Введите новый предмет студента:')
        changePassword = input()
        mycursor.execute("UPDATE `mydb`.`students` SET `Password` = '" + changePassword + "' WHERE (`Students` = '" + number + "')")
    mydb.commit()
    print('Теперь база данных имеет следующий вид:')
    mycursor.execute('SELECT * FROM students')
    myresult = mycursor.fetchall()
    for row in myresult:
        print (row)
if a == 'New':
    sqlFormula = 'INSERT INTO students (Number, Login, Password) VALUES (%s, %s, %s)'

    print('Введите номер студента в списке')
    Number = input()
    print('Введите его логин')
    Login = input()
    print('Введите его пароль')
    Password = input()

    insertsql = (Number, Login, Password)

    mycursor.execute(sqlFormula, insertsql)
    mydb.commit()

    print('Теперь база данных имеет следующий вид:')
    mycursor.execute('SELECT * FROM students')
    myresult = mycursor.fetchall()
    for row in myresult:
        print (row) 
