from datetime import datetime

def log_alert(message):

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_message = f"[{current_time}] {message}"

    print(log_message)

    with open("alerts.txt", "a") as file:
        file.write(log_message + "\n") 