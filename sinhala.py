from gtts import gTTS
import pygame
from io import BytesIO

# Initialize Pygame mixer
pygame.mixer.init()

# Read Sinhala text from a file
with open('C:/Users/user/Downloads/VisionVoice-recognition/VisionVoice-recognition/src/sinhala_text.txt', 'r', encoding='utf-8') as file:
    sinhala_text = file.read()

# Specify the language code for Sinhala
sinhala_language = 'si'

# Create a gTTS object for Sinhala text
sinhala_audio = gTTS(text=sinhala_text, lang=sinhala_language, slow=False)

# Save the audio file to a BytesIO object
sinhala_audio_bytes = BytesIO()
sinhala_audio.write_to_fp(sinhala_audio_bytes)

# Load the audio file
sinhala_audio_bytes.seek(0)
sinhala_sound = pygame.mixer.Sound(sinhala_audio_bytes)

# Play the audio file
print("Playing Sinhala audio...")
sinhala_sound.play()
pygame.time.wait(int(sinhala_sound.get_length() * 1000))  # Wait for the audio to finish playing

# Quit Pygame mixer
pygame.mixer.quit()

print("Sinhala audio playback finished.")
