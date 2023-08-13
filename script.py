import sounddevice as sd
import speech_recognition as sr
from encryption import decrypt
from gtts import gTTS
import tempfile
import os

# Set up API openAI
import openai

encrypted_api_key = b'z1DHJwKEsKq4PK7vNE/9RgGYiDK189yIR7xH3Ad0NpPRQmaAm2k0EZ7Hp8oDBgPppgkgke5KJQ0YFNppe+m7sA=='
decrypted_api_key = decrypt(encrypted_api_key)

# Set up API openai
openai.api_key = decrypted_api_key

# AI name
assistant_name = 'Jarvis'

# Speech recognition setup
r = sr.Recognizer()

# Start voice assistant
print(f'{assistant_name}: Hello! How can I assist you today?')

while True:
    # Get user input
    with sr.Microphone() as source:
        print('Listening...')
        audio = r.listen(source)

        # Convert speech to text
        user_input = r.recognize_google(audio)

        # Display user input
        print(f'User: {user_input}')

        # Processes user input with ChatGPT
    response = openai.Completion.acreate(
        engine='text-davinci-003',
        prompt=f'User: {user_input}\n{assistant_name}:',
        max_tokens=50
    )

    # Get assistant reply from response
    assistant_reply = response.choices[0].text.strip()

    # Output assistants reply
    print(f'{assistant_name}: {assistant_reply}')

    # Convert assistant reply to audio
    tts = gTTS(text=assistant_reply, lang='en')
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    tts.save(temp_file.name)
    temp_file.close()

    # Play reply
    sd.play(sd.read(temp_file.name).all())

    # Wait until the audio finishes playing
    sd.wait()

    # Delete temp audio file
    os.remove(temp_file.name)
