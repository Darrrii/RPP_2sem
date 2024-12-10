def send_message(method, to, content):
    print(f"Connecting to {method}...")
    print(f"Sending {method} to {to} with content '{content}'...")
    print(f"{method} sent.")

def send_email(to, subject, body):
    send_message("email", to, f"Subject: {subject}\nBody: {body}")

def send_sms(to, message):
    send_message("SMS", to, message)

if __name__ == "__main__":
    # Пример использования функций
    send_email("example@example.com", "Hello!", "This is a test email.")
    send_sms("1234567890", "This is a test SMS.")
