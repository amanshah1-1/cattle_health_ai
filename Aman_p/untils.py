# utils.py
import csv
from datetime import datetime

LOG_FILE = "query_logs.csv"

def log_query(agent: str, question: str, answer: str):
    with open(LOG_FILE, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), agent, question, answer])