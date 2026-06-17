from datetime import datetime

def log_step(message: str) -> None:
    timestamp = datetime.utcnow().isoformat()
    print(f"[{timestamp}] {message}")
