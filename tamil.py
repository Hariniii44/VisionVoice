from gtts import gTTS
import pygame
from io import BytesIO

# Initialize Pygame mixer
pygame.mixer.init()

# Read Tamil text from a file
with open('tamil_text.txt', 'r', encoding='utf-8') as file:
    tamil_text = file.read()

# Specify the language code for Tamil
tamil_language = 'ta'

# Create a gTTS object for Tamil text
tamil_audio = gTTS(text=tamil_text, lang=tamil_language, slow=False)

# Save the audio file to a BytesIO object
tamil_audio_bytes = BytesIO()
tamil_audio.write_to_fp(tamil_audio_bytes)

# Load the audio file
tamil_audio_bytes.seek(0)
tamil_sound = pygame.mixer.Sound(tamil_audio_bytes)

# Play the audio file
print("Playing Tamil audio...")
tamil_sound.play()
pygame.time.wait(int(tamil_sound.get_length() * 1000))  # Wait for the audio to finish playing

# Quit Pygame mixer
pygame.mixer.quit()

print("Tamil audio playback finished.")


##pip install pygame
##pip install gtts
