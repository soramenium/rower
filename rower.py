import os
import random
import time
import pygame
import RPi.GPIO as GPIO

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)
switch_pin = 17
GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def play_random_sound(folder_path):
    sound_files = [file for file in os.listdir(folder_path) if file.endswith(('.mp3', '.wav', '.ogg'))]
    random_sound = os.path.join(folder_path, random.choice(sound_files))
    pygame.mixer.init()
    pygame.mixer.music.load(random_sound)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue


try:
    while True:
        # Check if the switch is on
        if GPIO.input(switch_pin) == GPIO.LOW:
            # Execute your function
            play_random_sound("sounds/")
            # Add any additional delay to prevent rapid checking
            # This is optional and depends on your specific requirements
            time.sleep(0.1)
finally:
    # Clean up GPIO
    GPIO.cleanup()







def main():
    folder_path = "./sounds"  # Change this to your sound folder path
    # print("Press 'p' to play a random sound. Press 'q' to quit.")
    # while True:
    #     key_pressed = keyboard.read_event(suppress=True)
    #     if key_pressed.name == "p":
    #         play_random_sound(folder_path)
    #     elif key_pressed.name == "q":
    #         print("Exiting...")
    #         break
    for i in 10:
        play_random_sound(folder_path)

if __name__ == "__main__":
    main()
