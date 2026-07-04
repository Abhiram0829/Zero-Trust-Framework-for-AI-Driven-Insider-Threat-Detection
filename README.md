# Zero-Trust-Framework-for-AI-Driven-Insider-Threat-Detection
The Zero Trust Framework for AI-Driven Insider Threat Detection uses AI and UEBA to monitor user activities, analyze behavior patterns, and detect anomalies in real time. Following the “Never Trust, Always Verify” principle, it helps prevent insider threats, unauthorized access, and data breaches.!!
## Features
- Zero Trust access model (Never Trust, Always Verify)
- Machine Learning based anomaly detection (Isolation Forest)
- Insider threat detection using user behavior logs
- Web-based security monitoring dashboard (Flask)
- Comparison with traditional perimeter-based security

## Tech Stack
- Python
- Pandas, Scikit-learn
- Flask (Web Dashboard)
- Machine Learning (Isolation Forest)

## Objective
To analyze user behavior data, detect insider anomalies, reduce data leakage risks, 
and improve enterprise security monitoring through intelligent analytics.

## How to Run
1. Install dependencies:
   pip install pandas scikit-learn flask
2. Run anomaly detection:
   python anomaly_detection.py
3. Launch dashboard:
   python app.py
4. Open browser: http://127.0.0.1:5000

## Sample dataset
<img width="675" height="267" alt="image" src="https://github.com/user-attachments/assets/0b6759c6-8660-4989-8b93-d8b70a27e81f" />

## Output
<img width="1914" height="530" alt="Screenshot 2026-01-26 165622" src="https://github.com/user-attachments/assets/cff04527-9ccd-41ff-8329-8880c53a35ae" />

## Output Analysis

### 1. User U06 – Clearly Suspicious (True Insider Pattern)

| Feature | Value | Why Risky |
|--------|-------|-----------|
| Login hour | 1 AM | Odd working hour |
| Location | Remote | Outside secure office network |
| Device | Unknown | Untrusted device |
| Files accessed | 210 | Very high |
| Data downloaded | 4200 MB | Possible data exfiltration |

This behavior strongly indicates a potential **insider data theft scenario**.  
Hence, the Zero Trust model correctly flags **U06 as Suspicious**.

---

### 2. User U07 – Statistical Anomaly (Rare Pattern)

| Feature | Value |
|--------|-------|
| Role | Admin |
| Login hour | 16 |
| Device | Desktop |
| Location | Office |

User U07 does not show clear malicious behavior, but its combination of features is rare compared to other users.  
The Isolation Forest algorithm marks such rare patterns as **outliers**, which are treated as anomalies.  
This represents a **false positive**, a common challenge in real-world security analytics.


## Research Domain
Cybersecurity, Zero Trust Architecture, UEBA, Insider Threat Detection
