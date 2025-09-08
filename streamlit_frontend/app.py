# import streamlit as st
# from PIL import Image
# from gen_st_image import generate_image  # Stelle sicher, dass der Dateiname korrekt ist

# st.set_page_config(page_title="Tattoo Cover-Up Generator", layout="centered")

# st.title("🖋️ Tattoo Cover-Up Generator")
# st.markdown("Lade ein Bild deines Tattoos hoch und erhalte kreative Vorschläge zur Überarbeitung.")

# uploaded_file = st.file_uploader("📤 Bild hochladen", type=["png", "jpg", "jpeg"])

# style = st.selectbox("🎨 Gewünschter Stil", ["Blackwork", "Neo-Traditional", "Watercolor", "Realistic", "Trash Polka"])
# motif = st.text_input("🧠 Wunschmotiv (z. B. Drache, Rose, Mandala)")

# if uploaded_file:
#     image = Image.open(uploaded_file)
#     st.image(image, caption="Original Tattoo", use_container_width=True)

# if st.button("💡 Cover-Up generieren"):
#     if not motif:
#         st.warning("Bitte gib ein Wunschmotiv ein.")
#     else:
#         prompt = (
#             f"Design a {style} tattoo cover-up for an existing tattoo. "
#             f"The new design should feature a {motif}, suitable for placement on a shoulder. "
#             f"Use bold lines and shading typical of the {style} style."
#         )

#         with st.spinner("🧠 KI generiert dein Cover-Up..."):
#             result_image = generate_image(prompt)

#         if result_image:
#             st.image(result_image, caption="💡 Vorgeschlagene Cover-Up-Idee", use_container_width=True)
#         else:
#             st.error("❌ Es konnte kein Bild generiert werden. Bitte versuche es erneut.")

# import streamlit as st
# from PIL import Image
# from gen_st_image import generate_image

# st.set_page_config(page_title="Tattoo Cover-Up Generator", layout="centered")

# st.title("🖋️ Tattoo Cover-Up Generator")
# st.markdown("Lade ein Bild deines Tattoos hoch und teile uns mit, wie dein neues Design aussehen soll.")

# uploaded_file = st.file_uploader("📤 Bild hochladen", type=["png", "jpg", "jpeg"])

# if uploaded_file:
#     image = Image.open(uploaded_file)
#     st.image(image, caption="Original Tattoo", use_container_width=True)

#     st.subheader("🎯 Design-Präferenzen")

#     style = st.selectbox("Stilrichtung", ["Blackwork", "Neo-Traditional", "Watercolor", "Realistic", "Trash Polka"])
#     motif = st.text_input("Wunschmotiv (z. B. Drache, Rose, Mandala)")

#     cover_strategy = st.radio("Umgang mit bestehendem Tattoo", [
#         "Vollständiges Cover-Up", "Teilweise Integration", "Nur Ergänzung"
#     ])

#     emotion_tags = st.multiselect("Bedeutung des neuen Tattoos", [
#         "Schutz", "Freiheit", "Erinnerung", "Spiritualität", "Kampf", "Verwandlung", "Neuanfang"
#     ])

#     body_area = st.selectbox("Körperstelle", ["Schulter", "Oberarm", "Unterarm", "Brust", "Rücken", "Bein"])

#     reference_images = st.file_uploader("📎 Inspirationsbilder (optional)", type=["png", "jpg", "jpeg"], accept_multiple_files=True)

#     if st.button("💡 Cover-Up generieren"):
#         if not motif:
#             st.warning("Bitte gib ein Wunschmotiv ein.")
#         else:
#             prompt = (
#                 f"Design a {style} tattoo in the style of a {cover_strategy.lower()} for an existing tattoo. "
#                 f"The new design should feature a {motif} and be placed on the {body_area}. "
#                 f"It should reflect the themes of {', '.join(emotion_tags)}. "
#                 f"Use bold lines and shading typical of the {style} style."
#             )

#             with st.spinner("🧠 KI generiert dein Cover-Up..."):
#                 result_image = generate_image(prompt)

#             if result_image:
#                 st.image(result_image, caption="💡 Vorgeschlagene Cover-Up-Idee", use_container_width=True)
#             else:
#                 st.error("❌ Es konnte kein Bild generiert werden. Bitte versuche es erneut.")

# import streamlit as st
# from PIL import Image
# from gen_st_image import generate_image  # Funktion nutzt Bild + Prompt

# st.set_page_config(page_title="Tattoo Cover-Up Generator", layout="centered")

# st.title("🖋️ Tattoo Cover-Up Generator")
# st.markdown("Lade dein aktuelles Tattoo hoch und erhalte einen KI-generierten Cover-Up-Vorschlag.")

# uploaded_file = st.file_uploader("📤 Bild deines Tattoos hochladen", type=["png", "jpg", "jpeg"])

# if uploaded_file:
#     original_image = Image.open(uploaded_file)
#     st.image(original_image, caption="📌 Hochgeladenes Tattoo", use_container_width=True)

#     st.subheader("🎨 Gestaltungswünsche")

#     style = st.selectbox("Stilrichtung", ["Blackwork", "Neo-Traditional", "Watercolor", "Realistic", "Trash Polka"])
#     motif = st.text_input("Wunschmotiv (z. B. Drache, Rose, Mandala)")
#     size = st.selectbox("Größe des neuen Tattoos", ["Klein", "Mittel", "Groß"])
#     strategy = st.radio("Cover-Up Strategie", ["Vollständiges Überdecken", "Teilweise Integration"])

#     if st.button("💡 Cover-Up generieren"):
#         if not motif:
#             st.warning("Bitte gib ein Wunschmotiv ein.")
#         else:
#             prompt = (
#                 f"Create a {style} tattoo design as a {strategy.lower()} of an existing tattoo. "
#                 f"The new design should feature a {motif} and be {size.lower()} in size. "
#                 f"Use the uploaded image as the base for the transformation."
#             )

#             with st.spinner("🧠 KI verarbeitet dein Bild..."):
#                 result_image = generate_image(prompt, original_image)

#             if result_image:
#                 st.image(result_image, caption="✨ KI-generierter Cover-Up-Vorschlag", use_container_width=True)
#             else:
#                 st.error("❌ Es konnte kein Bild generiert werden. Bitte versuche es erneut.")

# app.py

# import streamlit as st
# from PIL import Image
# from gen_st_image import generate_image

# st.set_page_config(page_title="Tattoo Cover-Up Generator", layout="centered")

# st.title("🖋️ Tattoo Cover-Up Generator")
# st.markdown("Lade dein aktuelles Tattoo hoch und erhalte zwei KI-generierte Vorschläge: "
#             "einen mit sichtbarer Engelstruktur zur Orientierung und einen finalen Entwurf ohne Rückstände.")

# uploaded_file = st.file_uploader("📤 Bild deines Tattoos hochladen", type=["png", "jpg", "jpeg"])

# if uploaded_file:
#     original_image = Image.open(uploaded_file)
#     st.image(original_image, caption="📌 Hochgeladenes Tattoo", use_container_width=True)

#     st.subheader("🎨 Gestaltungswünsche")

#     style = st.selectbox("Stilrichtung", ["Blackwork", "Neo-Traditional", "Watercolor", "Realistic", "Trash Polka"])
#     motif = st.text_input("Wunschmotiv (z. B. Drache, Rose, Mandala)")
#     size = st.selectbox("Größe des neuen Tattoos", ["Klein", "Mittel", "Groß"])
#     strategy = st.radio("Cover-Up Strategie", ["Vollständiges Überdecken", "Teilweise Integration"])

#     if st.button("💡 Cover-Up generieren"):
#         if not motif:
#             st.warning("Bitte gib ein Wunschmotiv ein.")
#         else:
#             prompt_with_overlay = (
#                 f"Create a {style} tattoo design of a {motif} that overlays and transforms the existing tattoo of an angel. "
#                 f"The new design should incorporate the angel's structure visibly within the {motif}, showing how the cover-up works. "
#                 f"Use the uploaded image as the base and preserve key visual elements of the angel temporarily. "
#                 f"The new tattoo should be {size.lower()} in size and follow the strategy: {strategy.lower()}."
#             )

#             prompt_clean = (
#                 f"Create a clean {style} tattoo design of a {motif} without any trace of the original angel tattoo. "
#                 f"This version should be ready for final application, with no visible remnants of the previous design. "
#                 f"The tattoo should be {size.lower()} in size."
#             )

#             with st.spinner("🧠 KI erstellt Cover-Up mit Engelstruktur..."):
#                 image_with_overlay = generate_image(prompt_with_overlay, original_image)

#             with st.spinner("🎨 KI erstellt finale Version ohne Engel..."):
#                 image_clean = generate_image(prompt_clean)

#             if image_with_overlay:
#                 st.image(image_with_overlay, caption="🧩 Cover-Up mit Engelstruktur", use_container_width=True)
#             else:
#                 st.error("❌ Cover-Up mit Engelstruktur konnte nicht erstellt werden.")

#             if image_clean:
#                 st.image(image_clean, caption="✅ Finale Version ohne Engel", use_container_width=True)
#             else:
#                 st.error("❌ Finale Version ohne Engel konnte nicht erstellt werden.")

# app.py

# import streamlit as st
# from PIL import Image
# from gen_st_image import generate_image

# st.set_page_config(page_title="Tattoo Cover-Up Generator", layout="centered")

# st.title("🖋️ Tattoo Cover-Up Generator")
# st.markdown("Lade dein aktuelles Tattoo hoch und erhalte zwei KI-generierte Vorschläge: "
#             "einen mit sichtbarer Engelstruktur zur Orientierung und einen finalen Entwurf ohne Rückstände.")

# uploaded_file = st.file_uploader("📤 Bild deines Tattoos hochladen", type=["png", "jpg", "jpeg"])

# if uploaded_file:
#     original_image = Image.open(uploaded_file)
#     st.image(original_image, caption="📌 Hochgeladenes Tattoo", use_container_width=True)

#     st.subheader("🎨 Gestaltungswünsche")

#     style = st.selectbox("Stilrichtung", ["Traditionell Japanisch", "Blackwork", "Neo-Traditional", "Watercolor", "Realistic"])
#     motif = st.text_input("Wunschmotiv (z. B. Drache, Rose, Mandala)")
#     size = st.selectbox("Größe des neuen Tattoos", ["Klein", "Mittel", "Groß"])
#     strategy = st.radio("Cover-Up Strategie", ["Vollständiges Überdecken", "Teilweise Integration"])

#     if st.button("💡 Cover-Up generieren"):
#         if not motif:
#             st.warning("Bitte gib ein Wunschmotiv ein.")
#         else:
#             # Prompt für Bild 1 – mit sichtbarer Engelstruktur
#             prompt_with_overlay = (
#                 f"Create a tattoo design that overlays and transforms the original angel tattoo into a {motif} motif. "
#                 f"The {motif} should fully cover or integrate the angel's structure, using the uploaded image as the base. "
#                 f"However, the angel's underlying form must remain subtly visible within the new design — for example, through transparency, outlines, or embedded shapes — "
#                 f"so that the cover-up process is clearly understandable to both the client and the tattoo artist. "
#                 f"The style should be {style.lower()}, and the tattoo should be {size.lower()} in size. "
#                 f"Follow the strategy: {strategy.lower()}. Maintain the original image’s proportions, placement, and lighting."
#             )

#             # Prompt für Bild 2 – finale Version ohne Engelstruktur
#             prompt_clean = (
#                 f"Create a final tattoo design of the same {motif} motif in {style.lower()} style, using the uploaded image as the base. "
#                 f"This version must be visually identical to the previous design in terms of composition, placement, size, and lighting — "
#                 f"except that all traces of the original angel tattoo must be completely removed. "
#                 f"The result should look like a clean, finished {motif} tattoo, ready for application, with no visible remnants of the previous design."
#             )

#             with st.spinner("🧠 KI erstellt Cover-Up mit Engelstruktur..."):
#                 image_with_overlay = generate_image(prompt_with_overlay, original_image)

#             with st.spinner("🎨 KI erstellt finale Version ohne Engel..."):
#                 image_clean = generate_image(prompt_clean, original_image)

#             if image_with_overlay:
#                 st.image(image_with_overlay, caption="🧩 Cover-Up mit sichtbarer Engelstruktur", use_container_width=True)
#             else:
#                 st.error("❌ Cover-Up mit Engelstruktur konnte nicht erstellt werden.")

#             if image_clean:
#                 st.image(image_clean, caption="✅ Finale Version ohne Engelstruktur", use_container_width=True)
#             else:
#                 st.error("❌ Finale Version ohne Engelstruktur konnte nicht erstellt werden.")

# app.py

# import streamlit as st
# from PIL import Image
# from gen_st_image import generate_image

# st.set_page_config(page_title="Tattoo Cover-Up Generator", layout="centered")

# st.title("🖋️ Tattoo Cover-Up Generator")
# st.markdown("Lade dein aktuelles Tattoo hoch und erhalte zwei KI-generierte Vorschläge: "
#             "einen mit sichtbarer Engelstruktur zur Orientierung und einen finalen Entwurf ohne Rückstände.")

# uploaded_file = st.file_uploader("📤 Bild deines Tattoos hochladen", type=["png", "jpg", "jpeg"])

# if uploaded_file:
#     original_image = Image.open(uploaded_file)
#     st.image(original_image, caption="📌 Hochgeladenes Tattoo", use_container_width=True)

#     st.subheader("🎨 Gestaltungswünsche")

#     style = st.selectbox("Stilrichtung", ["Traditionell Japanisch", "Blackwork", "Neo-Traditional", "Watercolor", "Realistic"])
#     motif = st.text_input("Wunschmotiv (z. B. Rose, Mandala, Drache)")
#     size = st.selectbox("Größe des neuen Tattoos", ["Klein", "Mittel", "Groß"])
#     strategy = st.radio("Cover-Up Strategie", ["Vollständiges Überdecken", "Teilweise Integration"])

#     if st.button("💡 Cover-Up generieren"):
#         if not motif:
#             st.warning("Bitte gib ein Wunschmotiv ein.")
#         else:
#             # Prompt für Bild 1 – Cover-Up mit sichtbarer Engelstruktur
#             prompt_with_overlay = (
#                 f"Design a {style.lower()} tattoo that overlays and transforms the original angel tattoo into a {motif}. "
#                 f"The {motif} must fully cover or integrate the angel, but the angel’s original structure should remain subtly visible — "
#                 f"as shadow, contour, or embedded form — so the cover-up process is clearly understandable. "
#                 f"The uploaded image must be used as the base. "
#                 f"The new tattoo should be {size.lower()} in size and follow the strategy: {strategy.lower()}. "
#                 f"Maintain the original image’s proportions, placement, and lighting."
#             )

#             # Prompt für Bild 2 – finale Version ohne Engelstruktur
#             prompt_clean = (
#                 f"Create a final version of the same {motif} tattoo in {style.lower()} style, using the uploaded image as the base. "
#                 f"This version must be visually identical to the previous design in terms of composition, placement, size, and lighting — "
#                 f"but all traces of the original angel tattoo must be completely removed. "
#                 f"The result should be a clean, finished {motif} tattoo, ready for application, with no visible remnants of the angel."
#             )

#             with st.spinner("🧠 KI erstellt Cover-Up mit Engelstruktur..."):
#                 image_with_overlay = generate_image(prompt_with_overlay, original_image)

#             with st.spinner("🎨 KI erstellt finale Version ohne Engel..."):
#                 image_clean = generate_image(prompt_clean, original_image)

#             if image_with_overlay:
#                 st.image(image_with_overlay, caption="🧩 Cover-Up mit sichtbarer Engelstruktur", use_container_width=True)
#             else:
#                 st.error("❌ Cover-Up mit Engelstruktur konnte nicht erstellt werden.")

#             if image_clean:
#                 st.image(image_clean, caption="✅ Finale Version ohne Engelstruktur", use_container_width=True)
#             else:
#                 st.error("❌ Finale Version ohne Engelstruktur konnte nicht erstellt werden.")

# app.py

# import streamlit as st
# from PIL import Image
# from gen_st_image import generate_image

# st.set_page_config(page_title="Tattoo Cover-Up Generator", layout="centered")

# st.title("🖋️ Tattoo Cover-Up Generator")
# st.markdown("Lade dein aktuelles Tattoo hoch und erhalte einen KI-generierten Cover-Up-Vorschlag, "
#             "der das ursprüngliche Motiv vollständig überdeckt oder integriert.")

# uploaded_file = st.file_uploader("📤 Bild deines Tattoos hochladen", type=["png", "jpg", "jpeg"])

# if uploaded_file:
#     original_image = Image.open(uploaded_file)
#     st.image(original_image, caption="📌 Ursprüngliches Tattoo", use_container_width=True)

#     st.subheader("🎨 Gestaltungswünsche")

#     style = st.selectbox("Stilrichtung", ["Traditionell Japanisch", "Blackwork", "Neo-Traditional", "Watercolor", "Realistic"])
#     motif = st.text_input("Wunschmotiv (z. B. Rose, Mandala, Drache)")
#     size = st.selectbox("Größe des neuen Tattoos", ["Klein", "Mittel", "Groß"])
#     strategy = st.radio("Cover-Up Strategie", ["Vollständiges Überdecken", "Teilweise Integration"])

#     if st.button("💡 Cover-Up generieren"):
#         if not motif:
#             st.warning("Bitte gib ein Wunschmotiv ein.")
#         else:
#             prompt = (
#                 f"Create a {style.lower()} tattoo design of a {motif} that fully covers or integrates the original tattoo shown in the uploaded image. "
#                 f"The new design must match the original tattoo’s size, placement, and lighting, so that the transformation is clearly recognizable. "
#                 f"The result should look like a finished {motif} tattoo that either hides or absorbs the previous structure, depending on the strategy: {strategy.lower()}."
#             )

#             with st.spinner("🎨 KI erstellt Cover-Up..."):
#                 cover_up_image = generate_image(prompt, original_image)

#             if cover_up_image:
#                 st.image(cover_up_image, caption="✅ Fertiges Cover-Up", use_container_width=True)
#             else:
#                 st.error("❌ Cover-Up konnte nicht erstellt werden.")

# app.py

# import streamlit as st
# from PIL import Image, ImageEnhance
# from gen_st_image import generate_image

# st.set_page_config(page_title="Tattoo Cover-Up Generator", layout="centered")

# st.title("🖋️ Tattoo Cover-Up Generator")
# st.markdown("Lade dein aktuelles Tattoo hoch und erhalte einen KI-generierten Cover-Up-Vorschlag, "
#             "der das ursprüngliche Motiv vollständig überdeckt oder integriert.")

# uploaded_file = st.file_uploader("📤 Bild deines Tattoos hochladen", type=["png", "jpg", "jpeg"])

# if uploaded_file:
#     original_image = Image.open(uploaded_file).convert("RGBA")
#     st.image(original_image, caption="📌 Ursprüngliches Tattoo", use_container_width=True)

#     st.subheader("🎨 Gestaltungswünsche")

#     style = st.selectbox("Stilrichtung", ["Traditionell Japanisch", "Blackwork", "Neo-Traditional", "Watercolor", "Realistic"])
#     motif = st.text_input("Wunschmotiv (z. B. Rose, Mandala, Drache)")
#     size = st.selectbox("Größe des neuen Tattoos", ["Klein", "Mittel", "Groß"])
#     strategy = st.radio("Cover-Up Strategie", ["Vollständiges Überdecken", "Teilweise Integration"])

#     if st.button("💡 Cover-Up generieren"):
#         if not motif:
#             st.warning("Bitte gib ein Wunschmotiv ein.")
#         else:
#             prompt = (
#                 f"Create a {style.lower()} tattoo design of a {motif} that fully covers or integrates the original tattoo shown in the uploaded image. "
#                 f"The new design must match the original tattoo’s size, placement, and lighting, so that the transformation is clearly recognizable. "
#                 f"The result should look like a finished {motif} tattoo that either hides or absorbs the previous structure, depending on the strategy: {strategy.lower()}."
#             )

#             with st.spinner("🎨 KI erstellt Cover-Up..."):
#                 cover_up_image = generate_image(prompt, original_image)

#             if cover_up_image:
#                 st.image(cover_up_image, caption="✅ Fertiges Cover-Up", use_container_width=True)

#                 # Overlay-Ansicht erzeugen
#                 st.subheader("🔍 Vergleichsansicht: Überlagerung")
#                 cover_up_rgba = cover_up_image.convert("RGBA")
#                 original_transparent = original_image.copy()
#                 alpha = original_transparent.split()[3]
#                 alpha = ImageEnhance.Brightness(alpha).enhance(0.5)
#                 original_transparent.putalpha(alpha)

#                 overlay = Image.alpha_composite(cover_up_rgba, original_transparent)
#                 st.image(overlay, caption="🧪 Überlagerung: Original mit 50 % Transparenz über Cover-Up", use_container_width=True)
#             else:
#                 st.error("❌ Cover-Up konnte nicht erstellt werden.")

# app.py

# import streamlit as st
# from PIL import Image, ImageEnhance
# from gen_st_image import generate_image

# st.set_page_config(page_title="Tattoo Cover-Up Generator", layout="centered")

# st.title("🖋️ Tattoo Cover-Up Generator")
# st.markdown("Lade dein aktuelles Tattoo hoch und erhalte einen KI-generierten Cover-Up-Vorschlag, "
#             "der das ursprüngliche Motiv vollständig überdeckt oder integriert.")

# uploaded_file = st.file_uploader("📤 Bild deines Tattoos hochladen", type=["png", "jpg", "jpeg"])

# if uploaded_file:
#     original_image = Image.open(uploaded_file).convert("RGBA")
#     st.image(original_image, caption="📌 Ursprüngliches Tattoo", use_container_width=True)

#     st.subheader("🎨 Gestaltungswünsche")

#     style = st.selectbox("Stilrichtung", ["Traditionell Japanisch", "Blackwork", "Neo-Traditional", "Watercolor", "Realistic"])
#     motif = st.text_input("Wunschmotiv (z. B. Rose, Mandala, Drache)")
#     size = st.selectbox("Größe des neuen Tattoos", ["Klein", "Mittel", "Groß"])
#     strategy = st.radio("Cover-Up Strategie", ["Vollständiges Überdecken", "Teilweise Integration"])

#     if st.button("💡 Cover-Up generieren"):
#         if not motif:
#             st.warning("Bitte gib ein Wunschmotiv ein.")
#         else:
#             prompt = (
#                 f"Create a {style.lower()} tattoo design of a {motif} that fully covers or integrates the original tattoo shown in the uploaded image. "
#                 f"The new design must match the original tattoo’s size, placement, and lighting, so that the transformation is clearly recognizable. "
#                 f"The result should look like a finished {motif} tattoo that either hides or absorbs the previous structure, depending on the strategy: {strategy.lower()}."
#             )

#             with st.spinner("🎨 KI erstellt Cover-Up..."):
#                 cover_up_image = generate_image(prompt, original_image)

#             if cover_up_image:
#                 # Skalieren auf Originalgröße
#                 cover_up_resized = cover_up_image.convert("RGBA").resize(original_image.size)

#                 st.image(cover_up_resized, caption="✅ Fertiges Cover-Up", use_container_width=True)

#                 # Überlagerung erzeugen
#                 st.subheader("🔍 Vergleichsansicht: Überlagerung")
#                 original_transparent = original_image.copy()
#                 alpha = original_transparent.split()[3]
#                 alpha = ImageEnhance.Brightness(alpha).enhance(0.5)
#                 original_transparent.putalpha(alpha)

#                 overlay = Image.alpha_composite(cover_up_resized, original_transparent)
#                 st.image(overlay, caption="🧪 Überlagerung: Original mit 50 % Transparenz über Cover-Up", use_container_width=True)
#             else:
#                 st.error("❌ Cover-Up konnte nicht erstellt werden.")

# app.py

import streamlit as st
from PIL import Image, ImageEnhance
from gen_st_image import generate_image

st.set_page_config(page_title="Tattoo Cover-Up Generator", layout="centered")

st.title("🖋️ Tattoo Cover-Up Generator")
st.markdown("Lade dein aktuelles Tattoo hoch und erhalte einen KI-generierten Cover-Up-Vorschlag, "
            "der das ursprüngliche Motiv vollständig überdeckt oder integriert.")

uploaded_file = st.file_uploader("📤 Bild deines Tattoos hochladen", type=["png", "jpg", "jpeg"])

if uploaded_file:
    original_image = Image.open(uploaded_file).convert("RGBA")
    st.image(original_image, caption="📌 Ursprüngliches Tattoo", use_container_width=True)

    st.subheader("🎨 Gestaltungswünsche")

    style = st.selectbox("Stilrichtung", ["Traditionell Japanisch", "Blackwork", "Neo-Traditional", "Watercolor", "Realistic"])
    motif = st.text_input("Wunschmotiv (z. B. Rose, Mandala, Drache)")
    size = st.selectbox("Größe des neuen Tattoos", ["Klein", "Mittel", "Groß"])
    strategy = st.radio("Cover-Up Strategie", ["Vollständiges Überdecken", "Teilweise Integration"])

    if st.button("💡 Cover-Up generieren"):
        if not motif:
            st.warning("Bitte gib ein Wunschmotiv ein.")
        else:
            prompt = (
                f"Create a {style.lower()} tattoo design of a {motif} that matches the size and placement of the uploaded tattoo image. "
                f"The design should be scaled to '{size.lower()}' size, meaning it should {'match' if size == 'Klein' else 'slightly exceed' if size == 'Mittel' else 'significantly exceed'} the original tattoo dimensions. "
                f"The new design must either fully cover or integrate the original structure, depending on the strategy: {strategy.lower()}."
            )

            with st.spinner("🎨 KI erstellt Cover-Up..."):
                cover_up_image = generate_image(prompt, original_image)

            if cover_up_image:
                # Skalierungsfaktor definieren
                scale_map = {"Klein": 1.0, "Mittel": 1.2, "Groß": 1.5}
                scale_factor = scale_map[size]

                # Neue Größe berechnen
                new_size = (
                    int(original_image.width * scale_factor),
                    int(original_image.height * scale_factor)
                )

                # Cover-Up skalieren
                cover_up_scaled = cover_up_image.convert("RGBA").resize(new_size)

                # Bei Vergrößerung: zentrieren und auf Originalgröße zuschneiden
                if scale_factor > 1.0:
                    left = (new_size[0] - original_image.width) // 2
                    top = (new_size[1] - original_image.height) // 2
                    cover_up_cropped = cover_up_scaled.crop((left, top, left + original_image.width, top + original_image.height))
                else:
                    cover_up_cropped = cover_up_scaled

                st.image(cover_up_cropped, caption="✅ Fertiges Cover-Up", use_container_width=True)

                # Überlagerung erzeugen
                st.subheader("🔍 Vergleichsansicht: Überlagerung")
                original_transparent = original_image.copy()
                alpha = original_transparent.split()[3]
                alpha = ImageEnhance.Brightness(alpha).enhance(0.5)
                original_transparent.putalpha(alpha)

                overlay = Image.alpha_composite(cover_up_cropped, original_transparent)
                st.image(overlay, caption="🧪 Überlagerung: Original mit 50 % Transparenz über Cover-Up", use_container_width=True)
            else:
                st.error("❌ Cover-Up konnte nicht erstellt werden.")
  
# stream