# This code will help you to send message with images.
# One thing you have to remember that the format of the time must be in 24 hours.

import pywhatkit as kit
import pyautogui
from datetime import datetime
import time
import os

# Function to send WhatsApp message at a specific date and time
def schedule_whatsapp_message(phone_number, message, image_path, scheduled_datetime):
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
    
    # Schedule the WhatsApp message using pywhatkit (to open WhatsApp Web)
    kit.sendwhatmsg(phone_number, "", scheduled_hour, scheduled_minute)
    
    # time.sleep(15)  # Wait for WhatsApp Web to open and load (adjust if needed)
    
    # Check if the image exists
    if os.path.exists(image_path):
        # Send the image with the caption using pywhatkit
        kit.sendwhats_image(phone_number, image_path, message)
        
        time.sleep(5)  # Wait for the image to load before pressing enter
        pyautogui.press('enter')
        
        print("Image with message sent successfully!")
    else:
        print(f"Image not found at {image_path}")

# Example usage:
phone_number = "+91742******"  #WhatsApp number where you to sent the message.
image_path = ".jpeg" #path of the image
message = "Let's Check"

# Define the exact date and time when you want to send the message (YYYY, MM, DD, H, M)
scheduled_datetime = datetime(2024, 9, 23, 15, 54)

# Call the function to schedule the message
schedule_whatsapp_message(phone_number, message, image_path, scheduled_datetime)
