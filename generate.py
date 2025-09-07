# generate_image.py

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

def save_image(response, path="output.png"):
    for part in response.parts:
        if hasattr(part, "as_image") and (image := part.as_image()):
            image.save(path)
            print(f"Image saved to {path}")

def generate_image(prompt, output_path="generated.png"):
    client = genai.Client(api_key=API_KEY)

    print("Generating image...")

    response = client.models.generate_content(
        model=MODEL_ID,
        contents=prompt,
        config=types.GenerateContentConfig(response_modalities=["text", "image"])
    )

    image_parts = [
        part.inline_data.data
        for part in response.candidates[0].content.parts
        if part.inline_data
    ]

    if image_parts:
        image = Image.open(BytesIO(image_parts[0]))
        image.save(output_path)
        image.show()
        print(f"Image saved to {output_path}")
    else:
        print("No image data received.")

    display_response(response)

if __name__ == "__main__":
    prompt = "Erstelle ein Bild gemäss folgender Anweisung: Ein Astronaut betritt ein Cafe in Zürich. Zeige die Reaktion der Menschen und ihren Hunden."
    generate_image(prompt, output_path="astronaut_zh.png")
