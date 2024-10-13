# This code help you to send message at the time when u run the code it means time is fixed, here doesn't need to define date and time 
# One thing you have to remember that the format of the time must be in 24 hours.

import pywhatkit as kit
import pyautogui
from datetime import datetime
import time

# Send WhatsApp message and click send automatically
def send_whatsapp_message_now(phone_number, message):
    try:
        # Get the current time
        now = datetime.now()
        current_hour = now.hour
        current_minute = now.minute + 1  # Schedule for the next minute
        
        print(f"Scheduling message at {current_hour}:{current_minute}.")
        
        # Schedule the message using pywhatkit
        kit.sendwhatmsg(phone_number, message, current_hour, current_minute)
        
        # Wait for WhatsApp Web to load (pywhatkit adds a delay for about 15-20 seconds)
        time.sleep(20)  # You may need to adjust this depending on how fast WhatsApp loads

        # Automatically press the 'Enter' key to send the message
        pyautogui.press('enter')
        
        print("Message sent successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
phone_number = "+917428******"  #WhatsApp number where you want to sent the message
message = "Lets Check"

# Call the function to send the message
send_whatsapp_message_now(phone_number, message)

