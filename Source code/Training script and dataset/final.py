import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# -----------------------------
# 1. LOAD DATA
# -----------------------------
df = pd.read_csv("solar_training_fixed_clean.csv")

# Split features and target
X = df[["temperature", "humidity", "wind_speed", "pressure"]].values
y = df["solar_irradiance"].values

# -----------------------------
# 2. NORMALIZE FEATURES
# -----------------------------
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# -----------------------------
# 3. TRAIN–TEST SPLIT
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# -----------------------------
# 4. BUILD MODEL
# -----------------------------
model = Sequential([
    Dense(32, activation='relu', input_shape=(X_train.shape[1],)),
    Dense(16, activation='relu'),
    Dense(1)
])

model.compile(optimizer='adam', loss='mse')

# -----------------------------
# 5. TRAIN MODEL
# -----------------------------
history = model.fit(
    X_train, y_train,
    validation_data=(X_test, y_test),
    epochs=30,
    batch_size=16,
    verbose=1
)

# -----------------------------
# 6. SAVE TFLITE MODEL
# -----------------------------
model.save("solar_model.h5")

converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

with open("solar_model.tflite", "wb") as f:
    f.write(tflite_model)

print("\n🎉 Model training complete!")
print("➡ Saved: solar_model.h5")
print("➡ Saved: solar_model.tflite (Use this for Edge Impulse BYOM)")
