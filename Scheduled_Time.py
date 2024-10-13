# This code help you to send message automatically at that time when you want,it need to define the date and time. HEre you need to define "Year", "Month", "Date", "Hours", "Minute"
# One thing you have to rememder that the time must be in the format of 24 hours.

import pywhatkit as kit
import pyautogui
from datetime import datetime, timedelta

# Function to send WhatsApp message at a specific date and time
def schedule_whatsapp_message(phone_number, message, scheduled_datetime):
    # Get current time
    now = datetime.now()
    
    # Extract the target hour and minute from the scheduled datetime
    scheduled_hour = scheduled_datetime.hour
    scheduled_minute = scheduled_datetime.minute
    
    # Check if the scheduled time is valid (future time)
    if scheduled_datetime <= now:
        print("Scheduled time must be in the future!")
        return

    print(f"Message will be sent on {scheduled_datetime.strftime('%Y-%m-%d %H:%M')}")
    
    # Schedule the WhatsApp message using pywhatkit
    kit.sendwhatmsg(phone_number, message, scheduled_hour, scheduled_minute)
    
    pyautogui.press('enter')

    print("Message scheduled successfully!")

# Example usage:
phone_number = "+917428******"  #WhatsApp number where you want to sent the message
message = "Let's check"

# Define the exact date and time when you want to send the message (YYYY, MM, DD, H, M)
# Example: Scheduled for September 30, 2024, at 10:30 AM
scheduled_datetime = datetime(2024, 9, 23, 13, 6)

# Call the function to schedule the message
schedule_whatsapp_message(phone_number, message, scheduled_datetime)
