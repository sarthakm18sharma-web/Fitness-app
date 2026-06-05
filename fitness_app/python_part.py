import mysql.connector as mysql
db=mysql.connect(host="localhost",user="root",password="1234",database="fitness_app")
cursor = db.cursor()
ch=int(input("Enter the number of times you want to add details: "))
for i in range(ch):
    name=input("Enter the name of the person:")
    email=input("Enter the email address of the peroson:")
    phone_number=input("enter the phone number of the person")
    age=int(input("Enter the age of the person"))
    gender=input("Enter the gender of the person")
#details are taken so far
    query = """
    INSERT INTO personal_details
    (name, email, phone_number, age, gender)
    VALUES (%s, %s, %s, %s, %s)
    """
    values = (name, email, phone_number, age, gender)

    cursor.execute(query, values)
db.commit()
db.close()
#hello