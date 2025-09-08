# generate_image.py

import os
from io import BytesIO
from PIL import Image
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

# Modell-ID und API-Key
MODEL_ID = "gemini-2.5-flash-image-preview"
API_KEY = os.environ.get("GEMINI_API_KEY")  # Stelle sicher, dass dieser gesetzt ist

# def generate_image(prompt):
#     """
#     Generiert ein Bild basierend auf dem gegebenen Prompt mithilfe von Gemini 2.5 Flash.
#     Gibt ein PIL.Image-Objekt zurück oder None, falls keine Bilddaten empfangen wurden.
#     """
#     client = genai.Client(api_key=API_KEY)

#     response = client.models.generate_content(
#         model=MODEL_ID,
#         contents=prompt,
#         config=types.GenerateContentConfig(response_modalities=["image"])
#     )

#     image_parts = [
#         part.inline_data.data
#         for part in response.candidates[0].content.parts
#         if part.inline_data
#     ]

#     if image_parts:
#         image = Image.open(BytesIO(image_parts[0]))
#         return image
#     else:
#         return None

# def generate_image(prompt, input_image):
#     client = genai.Client(api_key=API_KEY)

#     image_bytes = BytesIO()
#     input_image.save(image_bytes, format="PNG")
#     image_bytes.seek(0)

#     response = client.models.generate_content(
#         model=MODEL_ID,
#         contents=[
#             types.Content(
#                 parts=[
#                     types.Part(text=prompt),
#                     types.Part(inline_data=types.Blob(mime_type="image/png", data=image_bytes.read()))
#                 ]
#             )
#         ],
#         config=types.GenerateContentConfig(response_modalities=["image"])
#     )

#     image_parts = [
#         part.inline_data.data
#         for part in response.candidates[0].content.parts
#         if part.inline_data
#     ]

#     if image_parts:
#         return Image.open(BytesIO(image_parts[0]))
#     else:
#         return None

# def generate_image(prompt, input_image=None):
#     client = genai.Client(api_key=API_KEY)

#     parts = [types.Part(text=prompt)]
#     if input_image:
#         image_bytes = BytesIO()
#         input_image.save(image_bytes, format="PNG")
#         image_bytes.seek(0)
#         parts.append(types.Part(inline_data=types.Blob(mime_type="image/png", data=image_bytes.read())))

#     response = client.models.generate_content(
#         model=MODEL_ID,
#         contents=[types.Content(parts=parts)],
#         config=types.GenerateContentConfig(response_modalities=["image"])
#     )

#     image_parts = [
#         part.inline_data.data
#         for part in response.candidates[0].content.parts
#         if part.inline_data
#     ]

#     if image_parts:
#         return Image.open(BytesIO(image_parts[0]))
#     else:
#         return None

# def generate_image(prompt, input_image=None):
#     client = genai.Client(api_key=API_KEY)

#     parts = [types.Part(text=prompt)]
#     if input_image:
#         image_bytes = BytesIO()
#         input_image.save(image_bytes, format="PNG")
#         image_bytes.seek(0)
#         parts.append(types.Part(inline_data=types.Blob(mime_type="image/png", data=image_bytes.read())))

#     response = client.models.generate_content(
#         model=MODEL_ID,
#         contents=[types.Content(parts=parts)],
#         config=types.GenerateContentConfig(response_modalities=["image"])
#     )

#     image_parts = [
#         part.inline_data.data
#         for part in response.candidates[0].content.parts
#         if part.inline_data
#     ]

#     if image_parts:
#         return Image.open(BytesIO(image_parts[0]))
#     else:
#         return None

# def generate_image(prompt, input_image=None):
#     client = genai.Client(api_key=API_KEY)

#     parts = [types.Part(text=prompt)]
#     if input_image:
#         image_bytes = BytesIO()
#         input_image.save(image_bytes, format="PNG")
#         image_bytes.seek(0)
#         parts.append(types.Part(inline_data=types.Blob(mime_type="image/png", data=image_bytes.read())))

#     response = client.models.generate_content(
#         model=MODEL_ID,
#         contents=[types.Content(parts=parts)],
#         config=types.GenerateContentConfig(response_modalities=["image"])
#     )

#     image_parts = [
#         part.inline_data.data
#         for part in response.candidates[0].content.parts
#         if part.inline_data
#     ]

#     if image_parts:
#         return Image.open(BytesIO(image_parts[0]))
#     else:
#         return None

# def generate_image(prompt, input_image=None):
#     client = genai.Client(api_key=API_KEY)

#     parts = [types.Part(text=prompt)]
#     if input_image:
#         image_bytes = BytesIO()
#         input_image.save(image_bytes, format="PNG")
#         image_bytes.seek(0)
#         parts.append(types.Part(inline_data=types.Blob(mime_type="image/png", data=image_bytes.read())))

#     response = client.models.generate_content(
#         model=MODEL_ID,
#         contents=[types.Content(parts=parts)],
#         config=types.GenerateContentConfig(response_modalities=["image"])
#     )

#     image_parts = [
#         part.inline_data.data
#         for part in response.candidates[0].content.parts
#         if part.inline_data
#     ]

#     if image_parts:
#         return Image.open(BytesIO(image_parts[0]))
#     else:
#         return None

def generate_image(prompt, input_image=None):
    client = genai.Client(api_key=API_KEY)

    parts = [types.Part(text=prompt)]
    if input_image:
        image_bytes = BytesIO()
        input_image.save(image_bytes, format="PNG")
        image_bytes.seek(0)
        parts.append(types.Part(inline_data=types.Blob(mime_type="image/png", data=image_bytes.read())))

    response = client.models.generate_content(
        model=MODEL_ID,
        contents=[types.Content(parts=parts)],
        config=types.GenerateContentConfig(response_modalities=["image"])
    )

    image_parts = [
        part.inline_data.data
        for part in response.candidates[0].content.parts
        if part.inline_data
    ]

    if image_parts:
        return Image.open(BytesIO(image_parts[0]))
    else:
        return None