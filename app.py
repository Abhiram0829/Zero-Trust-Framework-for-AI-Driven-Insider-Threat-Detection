from flask import Flask, render_template
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

@app.route("/")
def dashboard():
    data = pd.read_csv("data.csv")

    # Encode categorical columns
    le = LabelEncoder()
    data['role_enc'] = le.fit_transform(data['role'])
    data['location_enc'] = le.fit_transform(data['location'])
    data['device_enc'] = le.fit_transform(data['device'])

    features = data[['login_hour','files_accessed','data_mb','role_enc','location_enc','device_enc']]

    model = IsolationForest(contamination=0.25, random_state=42)
    data['anomaly'] = model.fit_predict(features)

    data['status'] = data['anomaly'].apply(lambda x: "Suspicious" if x == -1 else "Normal")

    # Convert to clean HTML (no \n issue)
    table_html = data.to_html(index=False)

    return render_template("dashboard.html", tables=table_html)

if __name__ == "__main__":
    app.run(debug=True)
