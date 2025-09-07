# mix_images.py

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

def save_image(response, filename="mixed_output.png"):
    for part in response.parts:
        if hasattr(part, "as_image") and (image := part.as_image()):
            image.save(filename)
            print(f"Bild gespeichert unter: {filename}")
            return
    print("⚠️ Kein Bild erhalten.")

def mix_images_with_prompt(prompt, image_paths, output_path="mixed_output.png"):
    client = genai.Client(api_key=API_KEY)

    # Nur bis zu 3 Bilder zulassen
    if len(image_paths) > 3:
        print("⚠️ Maximal 3 Bilder erlaubt. Es werden nur die ersten 3 verwendet.")
        image_paths = image_paths[:3]

    # Bilder laden
    images = []
    for path in image_paths:
        try:
            img = Image.open(path)
            images.append(img)
        except Exception as e:
            print(f"⚠️ Fehler beim Laden von {path}: {e}")

    if not images:
        print("❌ Keine gültigen Bilder geladen. Abbruch.")
        return

    print("🔄 Sende Prompt und Bilder an das Modell...")

    try:
        response = client.models.generate_content(
            model=MODEL_ID,
            contents=[prompt] + images,
            config=types.GenerateContentConfig(response_modalities=["image"])
        )
        display_response(response)
        save_image(response, filename=output_path)
    except Exception as e:
        print(f"❌ Fehler bei der Anfrage: {e}")

if __name__ == "__main__":
    # Beispielprompt
    prompt = "Create a picture that combines the three main characters of the pictures sitting at a table in a diner like in the 1960ies."

    # Beispielbilder – passe die Pfade an deine Dateien an
    image_paths = ["cat.png", "frog.png", "astro.png"]  # Optional: füge ein drittes Bild hinzu

    mix_images_with_prompt(prompt, image_paths, output_path="fantasy_mix.png")
