import psycopg2
import random
from datetime import datetime

conn = psycopg2.connect(
    user="TU_USER",
    password="TU_PASSWORD",
    host="TU_HOST",
    port="5432",
    dbname="postgres"
)

cur = conn.cursor()

age = random.uniform(0,1)
bmi = random.uniform(0,1)
bp = random.uniform(0,1)
prediction = age + bmi + bp

cur.execute(
    "INSERT INTO pc_ml_diabetes (age,bmi,bp,prediction,created_at) VALUES (%s,%s,%s,%s,%s)",
    (age,bmi,bp,prediction,datetime.now())
)

conn.commit()
print("Registro insertado")
