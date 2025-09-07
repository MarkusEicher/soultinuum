from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import os

MODEL_ID = "gemini-2.5-flash-image-preview"

API_KEY = os.environ.get("GEMINI_API_KEY")  # sicherer als direkt im Code

def display_response(response):
    for part in response.parts:
        if hasattr(part, "text") and part.text:
            print("\n--- Text Output ---\n")
            print(part.text)
        elif hasattr(part, "as_image") and (image := part.as_image()):
            print("\n--- Image Output ---\n")
            image.show()  # Öffnet mit Standard-Viewer

def save_image(response, path="output.png"):
    for part in response.parts:
        if hasattr(part, "as_image") and (image := part.as_image()):
            image.save(path)
            print(f"Image saved to {path}")

def edit_image_with_prompt(client, model_id, image_path, prompt, output_path="edited.png"):
    # Bild laden
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Fehler beim Laden des Bildes: {e}")
        return

    print("Sende Bild und Prompt an das Modell...")

    # Anfrage an das Modell
    response = client.models.generate_content(
        model=model_id,
        contents=[prompt, image],
        config=types.GenerateContentConfig(response_modalities=["image"])
    )

    # Bild anzeigen und speichern
    for part in response.parts:
        if hasattr(part, "as_image") and (edited := part.as_image()):
            edited.show()
            edited.save(output_path)
            print(f"Bild gespeichert unter: {output_path}")
            return

    print("Keine Bildantwort erhalten.")

client = genai.Client(api_key=API_KEY)

prompt = "Ein Astronaut betritt einen Gerichtssaal im Regenwald. Zeige die Reaktion der Tiere und die Jury aus Papageien."
# prompt = "Draw a red apple on a white table."


print("Generating image...")

response = client.models.generate_content(
    model=MODEL_ID,
    contents=prompt,
    config=types.GenerateContentConfig(
        response_modalities=['Text', 'Image']
    )
)

image_parts = [
    part.inline_data.data
    for part in response.candidates[0].content.parts
    if part.inline_data
]

if image_parts:
    image = Image.open(BytesIO(image_parts[0]))
    image.save("cat.png")
    image.show()

display_response(response)
save_image(response, "astronaut.png")

# edit_image_with_prompt(
#     client=client,
#     model_id=MODEL_ID,
#     image_path="cat.png",
#     prompt="Create a side view picture of that cat, in a tropical forest, eating a nano-banana, under the stars",
#     output_path="cat_tropical.png"
# )