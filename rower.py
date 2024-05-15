import os
import random
import keyboard
import pygame

def play_random_sound(folder_path):
    sound_files = [file for file in os.listdir(folder_path) if file.endswith(('.mp3', '.wav', '.ogg'))]
    random_sound = os.path.join(folder_path, random.choice(sound_files))
    pygame.mixer.init()
    pygame.mixer.music.load(random_sound)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue

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
