# chat_image_interactive.py

from google import genai
from google.genai import types
from PIL import Image
import os

MODEL_ID = "gemini-2.5-flash-image-preview"
API_KEY = os.environ.get("GEMINI_API_KEY")

def display_response(response):
    for part in response.parts:
        if hasattr(part, "as_image") and (image := part.as_image()):
            image.show()

def save_image(response, filename):
    for part in response.parts:
        if hasattr(part, "as_image") and (image := part.as_image()):
            image.save(filename)
            print(f"Bild gespeichert unter: {filename}")
            return
    print("Kein Bild erhalten.")

def run_interactive_chat():
    client = genai.Client(api_key=API_KEY)
    chat = client.chats.create(model=MODEL_ID)

    count = 1
    print("🔵 Starte Bild-Chat. Gib deinen Prompt ein (oder 'exit' zum Beenden):")

    while True:
        user_input = input(f"\nPrompt {count}: ")
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Chat beendet.")
            break

        try:
            response = chat.send_message(user_input)
            display_response(response)
            filename = f"interactive_image_{count}.png"
            save_image(response, filename)
            count += 1
        except Exception as e:
            print(f"⚠️ Fehler: {e}")

if __name__ == "__main__":
    run_interactive_chat()
