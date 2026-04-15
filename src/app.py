from pickle import load
import pandas as pd

with open("../models/modelo_LR_Ridge_alp1_fit-inter0_max-it100_solv-sag.sav", "rb") as f:
    model = load(f)

# Si se ha entrenado el modelo con el dataset ganador, por ejemplo el que se aplica el escalado min-max, se carga también
#...

X_train_CON_outliers = pd.read_excel("../data/processed/X_train_CON_outliers.xlsx")

# -----------------

import streamlit as st

st.title("Fatiga mental🧠")
st.header("Modelo que precide tu puntuación de fatiga mental")

Age = st.slider(label = "Edad", min_value = 18, max_value = 99, step = 1, value=30)
daily_screen_time_hours = st.slider(label = "Tiempo diario en pantalla (horas)", min_value = 0.0, max_value = 14.00, step = 0.01)
phone_usage_before_sleep_minutes = st.slider(label = "Tiempo de uso del teléfono antes de dormir (min)", min_value = 0, max_value = 120, step = 1)
sleep_duration_hours =  st.slider(label = "Duración del sueño (horas)", min_value = 0.0, max_value = 10.00, step = 0.01)
sleep_quality_score = st.slider(label = "Calidad del sueño", min_value = 1.00, max_value = 10.00, step = 0.01, value=5.00)
stress_level = st.slider(label = "Niveles de Estrés", min_value = 1.00, max_value = 10.00, step = 0.01)
caffeine_intake_cups = st.slider(label = "Vasos de café al día", min_value = 0, max_value = 5, step = 1)
physical_activity_minutes = st.slider(label = "Actividad física (min)", min_value = 0, max_value = 120, step = 1)


if st.button("Calcular fatiga mental"):

    if Age > X_train_CON_outliers["age"].max():
        Age = X_train_CON_outliers["age"].max()

    if daily_screen_time_hours > X_train_CON_outliers["daily_screen_time_hours"].max():
        daily_screen_time_hours = X_train_CON_outliers["daily_screen_time_hours"].max()

    if phone_usage_before_sleep_minutes > X_train_CON_outliers["phone_usage_before_sleep_minutes"].max():
        phone_usage_before_sleep_minutes = X_train_CON_outliers["phone_usage_before_sleep_minutes"].max()

    if sleep_duration_hours > X_train_CON_outliers["sleep_duration_hours"].max():
        sleep_duration_hours = X_train_CON_outliers["sleep_duration_hours"].max()

    if caffeine_intake_cups > X_train_CON_outliers["caffeine_intake_cups"].max():
        caffeine_intake_cups = X_train_CON_outliers["caffeine_intake_cups"].max()

    if physical_activity_minutes > X_train_CON_outliers["physical_activity_minutes"].max():
        physical_activity_minutes = X_train_CON_outliers["physical_activity_minutes"].max()

    predict_row = [[Age, daily_screen_time_hours, phone_usage_before_sleep_minutes, sleep_duration_hours, sleep_quality_score, stress_level, caffeine_intake_cups, physical_activity_minutes]]
    prediction = model.predict(predict_row)[0]
    st.write(f"Tus niveles de fatiga mental son: {round(prediction/10, 2)}")
