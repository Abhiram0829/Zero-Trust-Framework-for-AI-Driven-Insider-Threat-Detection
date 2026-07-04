import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import LabelEncoder

# Load data
data = pd.read_csv("data.csv")

# Encode categorical columns
encoder = LabelEncoder()
data['role_enc'] = encoder.fit_transform(data['role'])
data['location_enc'] = encoder.fit_transform(data['location'])
data['device_enc'] = encoder.fit_transform(data['device'])

features = data[['login_hour', 'files_accessed', 'data_mb', 'role_enc', 'location_enc', 'device_enc']]

# Train Isolation Forest
model = IsolationForest(contamination=0.25, random_state=42)
data['anomaly'] = model.fit_predict(features)

# Convert results
data['status'] = data['anomaly'].apply(lambda x: "Suspicious" if x == -1 else "Normal")

print("\nZero Trust Insider Detection Result:\n")
print(data[['user_id', 'role', 'login_hour', 'files_accessed', 'data_mb', 'status']])
