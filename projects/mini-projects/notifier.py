from plyer import notification
import time

def send_notification(title, message, timeout=10):
    try:
        notification.notify(
            title=title,
            message=message,
            app_name="Python Notifier",
            timeout=timeout
        )
        print(f"Notification sent: {title}")
    except Exception as e:
        print(f"Error: {e}")
        print("Make sure 'plyer' is installed: pip install plyer")

def main():
    print("--- Desktop Notifier ---")
    title = input("Enter notification title: ")
    msg = input("Enter notification message: ")
    delay = int(input("Enter delay in seconds (0 for immediate): "))
    
    if delay > 0:
        print(f"Waiting {delay} seconds...")
        time.sleep(delay)
        
    send_notification(title, msg)

if __name__ == "__main__":
    main()
