import psycopg2
import random
import toml
from datetime import datetime

config = toml.load("secrets.toml")

conn = psycopg2.connect(
    user=config["postgres"]["USER"],
    password=config["postgres"]["PASSWORD"],
    host=config["postgres"]["HOST"],
    port=config["postgres"]["PORT"],
    dbname=config["postgres"]["DBNAME"]
)

cur = conn.cursor()

age = random.uniform(0,1)
bmi = random.uniform(0,1)
bp = random.uniform(0,1)
prediction = age + bmi + bp

cur.execute(
    """
    INSERT INTO pc_ml_diabetes (age,bmi,bp,prediction,created_at)
    VALUES (%s,%s,%s,%s,%s)
    """,
    (age,bmi,bp,prediction,datetime.now())
)

conn.commit()
print("Registro insertado")
