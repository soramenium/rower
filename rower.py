import RPi.GPIO as GPIO
import pygame
import time
import os
import random
from collections import deque

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
SIGNAL_PIN = 17
GPIO.setup(SIGNAL_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Initialize Pygame mixer
pygame.mixer.init()

# Parameters
WINDOW_SIZE = 5  # seconds
FREQUENCY_THRESHOLD = 1  # Hz, frequency threshold to trigger sound
SOUNDS_FOLDER = 'sounds'  # Folder where sound files are located
DEBOUNCE_TIME = 200  # milliseconds

signal_times = deque(maxlen=1000)

def get_random_sound():
    """ Get a random sound file from the sounds folder """
    sound_files = [f for f in os.listdir(SOUNDS_FOLDER) if f.endswith('.wav')]
    if not sound_files:
        raise FileNotFoundError("No .wav files found in the sounds folder")
    return os.path.join(SOUNDS_FOLDER, random.choice(sound_files))

def play_sound():
    """ Play a random sound """
    sound_file = get_random_sound()
    sound = pygame.mixer.Sound(sound_file)
    sound.play()

def signal_received(channel):
    """ Callback function when signal is received """
    current_time = time.time()
    signal_times.append(current_time)

# Add event detection on the signal pin
    GPIO.add_event_detect(SIGNAL_PIN, GPIO.FALLING, callback=signal_received, bouncetime=DEBOUNCE_TIME)

try:
    while True:
        current_time = time.time()

        # Remove signals that are outside the window
        while signal_times and signal_times[0] < current_time - WINDOW_SIZE:
            signal_times.popleft()

        # Calculate frequency
        if len(signal_times) > 1:
            duration = signal_times[-1] - signal_times[0]
            frequency = len(signal_times) / duration if duration > 0 else 0
        else:
            frequency = 0

        # Play sound if frequency is above threshold
        if frequency >= FREQUENCY_THRESHOLD:
            play_sound()

        # Sleep a bit before next check
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Exiting program")

finally:
    GPIO.cleanup()
    pygame.quit()
