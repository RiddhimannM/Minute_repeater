import time
import datetime
import pygame

# Initialize pygame mixer
pygame.mixer.init()

def play_sound(file, count):
    sound = pygame.mixer.Sound(file)
    for _ in range(count):
        sound.play()
        time.sleep(sound.get_length())  # Wait for the sound to finish before playing the next

def minute_repeater():
    # now = datetime.datetime.now()
    now = datetime.datetime(2024, 1, 1, 8, 53 , 45)
    
    hours = now.hour % 12  # Get hour in 12-hour format
    quarters = now.minute // 15
    minutes = now.minute % 15
    
    print(f"Current Time: {now.strftime('%I:%M %p')}")
    
    # Chime hours
    if hours == 0:
        hours = 12  # Handle midnight and noon
    print("total number of hours: "+str(hours))
    play_sound("hour.mp3", hours)
    
    # Chime quarters
    print("total number of quarters: "+str(quarters)+" which is equivalent to "+str(quarters*15)+" minutes.")
    play_sound("quarter.mp3", quarters)
    
    # Chime minutes
    print("total number of minutes: "+str(minutes))
    play_sound("minute.mp3", minutes)
    
if __name__ == "__main__":
    minute_repeater()