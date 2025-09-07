# generate_story_loop.py

from google import genai
from google.genai import types
from PIL import Image
import os
import time

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

def generate_story_images(base_prompt, num_images=8, base_filename="blue_duo_1960s"):
    client = genai.Client(api_key=API_KEY)

    for i in range(num_images):
        scene_prompt = f"{base_prompt} This is scene {i+1} of 8."
        print(f"\n🖼️ Generiere Szene {i+1}...")

        try:
            response = client.models.generate_content(
                model=MODEL_ID,
                contents=scene_prompt,
                config=types.GenerateContentConfig(response_modalities=["image"])
            )
            filename = f"{base_filename}_scene_{i+1}.png"
            display_response(response)
            save_image(response, filename)

        except Exception as e:
            print(f"⚠️ Fehler bei Szene {i+1}: {e}")
            time.sleep(2)  # kurze Pause vor nächstem Versuch

if __name__ == "__main__":
    base_prompt = (
        "Create a beautifully entertaining story image with two blue characters and their adventures "
        "in the 1960s music scene. The story is thrilling throughout with emotional highs and lows and ends "
        "on a great twist and high note. Do not include any words or text on the image but tell the story purely through the imagery itself."
    )
    generate_story_images(base_prompt, num_images=4, base_filename="blue_duo_1960s")
