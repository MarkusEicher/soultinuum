# edit_image.py

from google import genai
from google.genai import types
from PIL import Image
import os

MODEL_ID = "gemini-2.5-flash-image-preview"
API_KEY = os.environ.get("GEMINI_API_KEY")  # Setze deine API-Umgebungsvariable

def edit_image_with_prompt(image_path, prompt, output_path="edited.png"):
    client = genai.Client(api_key=API_KEY)

    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Fehler beim Laden des Bildes: {e}")
        return

    print("Sende Bild und Prompt an das Modell...")

    response = client.models.generate_content(
        model=MODEL_ID,
        contents=[prompt, image],
        config=types.GenerateContentConfig(response_modalities=["image"])
    )

    for part in response.parts:
        if hasattr(part, "as_image") and (edited := part.as_image()):
            edited.show()
            edited.save(output_path)
            print(f"Bild gespeichert unter: {output_path}")
            return

    print("Keine Bildantwort erhalten.")

if __name__ == "__main__":
    image_path = "astronaut_zh.png"  # Bild, das du zuvor generiert hast
    prompt = "Erstelle eine Seitenansicht des Astronauten, wie er mit einem Nano-Banane-Papagei spricht, unter Sternenhimmel."
    edit_image_with_prompt(image_path, prompt, output_path="astronaut_edited.png")
