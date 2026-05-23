import os
import csv
from datetime import datetime

def save_cover_letter_file(job_title, agency, content):
    folder = os.path.join(os.path.dirname(__file__), '..', 'data', 'cover_letters')
    os.makedirs(folder, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{job_title.replace(' ', '_')}_{timestamp}.txt"
    filepath = os.path.join(folder, filename)
    with open(filepath, 'w') as f:
        f.write(content)
    print(f"✅ Cover letter saved: {filename}")
    return filepath

def log_application(job_title, agency, resume_summary):
    log_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'applications_log.csv')
    file_exists = os.path.isfile(log_path)
    with open(log_path, 'a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Timestamp", "Job Title", "Agency", "Resume Summary"])
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), job_title, agency, resume_summary])
    print(f"✅ Application logged: {job_title} at {agency}")
