# generate_story.py

from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import os

MODEL_ID = "gemini-2.5-flash-image-preview"
API_KEY = os.environ.get("GEMINI_API_KEY")  # Setze deine API-Umgebungsvariable

def display_response(response):
    for part in response.parts:
        if hasattr(part, "text") and part.text:
            print("\n--- Text Output ---\n")
            print(part.text)
        elif hasattr(part, "as_image") and (image := part.as_image()):
            print("\n--- Image Output ---\n")
            image.show()

def save_images(response, base_filename="story_image"):
    count = 0
    for part in response.parts:
        if hasattr(part, "as_image") and (image := part.as_image()):
            filename = f"{base_filename}_{count+1}.png"
            image.save(filename)
            print(f"Bild {count+1} gespeichert unter: {filename}")
            count += 1
    if count == 0:
        print("Keine Bilder erhalten.")

def generate_story(prompt, base_filename="story_image"):
    client = genai.Client(api_key=API_KEY)

    print("Generiere Story-Bilder...")

    response = client.models.generate_content(
        model=MODEL_ID,
        contents=prompt,
        config=types.GenerateContentConfig(response_modalities=["image"])
    )

    display_response(response)
    save_images(response, base_filename=base_filename)

if __name__ == "__main__":
    prompt = (
        "Create a beautifully entertaining 8 part story with 8 images with two blue characters and their adventures "
        "in the 1960s music scene. The story is thrilling throughout with emotional highs and lows and ending on a great "
        "twist and high note. Do not include any words or text on the images but tell the story purely through the imagery itself."
    )
    generate_story(prompt, base_filename="blue_duo_1960s")
