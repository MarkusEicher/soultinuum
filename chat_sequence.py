# chat_image_sequence.py

from google import genai
from google.genai import types
from PIL import Image
import os

MODEL_ID = "gemini-2.5-flash-image-preview"
API_KEY = os.environ.get("GEMINI_API_KEY")  # Stelle sicher, dass deine API-Variable gesetzt ist

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

def run_chat_sequence(messages, base_filename="fox_scene"):
    client = genai.Client(api_key=API_KEY)
    chat = client.chats.create(model=MODEL_ID)

    for i, message in enumerate(messages):
        print(f"\n💬 Sende Nachricht {i+1}: {message}")
        try:
            response = chat.send_message(message)
            display_response(response)
            filename = f"{base_filename}_{i+1}.png"
            save_image(response, filename)
        except Exception as e:
            print(f"⚠️ Fehler bei Nachricht {i+1}: {e}")

if __name__ == "__main__":
    messages = [
        "Create an image of a plastic toy fox figurine with a blue planet on its helmet in a kid's bedroom. It can have accessories but no weapon.",
        "Move that figurine to a beach.",
        "Now it should be base-jumping from a spaceship with a wingsuit."
    ]
    run_chat_sequence(messages, base_filename="toy_fox_adventure")
