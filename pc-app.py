import streamlit as st
import psycopg2

st.title("Predicción de progresión de Diabetes")

conn = psycopg2.connect(
    user=st.secrets["postgres"]["USER"],
    password=st.secrets["postgres"]["PASSWORD"],
    host=st.secrets["postgres"]["HOST"],
    port=st.secrets["postgres"]["PORT"],
    dbname=st.secrets["postgres"]["DBNAME"]
)

age = st.number_input("Edad", value=0.0)
bmi = st.number_input("BMI", value=0.0)
bp = st.number_input("Presión", value=0.0)

if st.button("Guardar"):
    prediction = age + bmi + bp
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO pc_ml_diabetes (age,bmi,bp,prediction) VALUES (%s,%s,%s,%s)",
        (age,bmi,bp,prediction)
    )
    conn.commit()
    st.success(f"Guardado. Predicción: {prediction}")
