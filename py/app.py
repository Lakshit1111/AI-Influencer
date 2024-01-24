import streamlit as st
from ImageGenerator import ImageGenerator
import os
from dotenv import load_dotenv

# Carga las variables de entorno desde el archivo .env
load_dotenv()

# Obtiene la URL de la API y la clave API de las variables de entorno
api_url = os.getenv("API_URL")
api_key = os.getenv("API_KEY")

# Configura la página
st.set_page_config(page_title="AI Image Generator", page_icon=":camera:")

# Verifica que las variables de entorno existan
if not api_url or not api_key:
    st.error("API URL or API Key not found. Please check your .env file.")
    st.stop()

# Crear una instancia de ImageGenerator
generator = ImageGenerator(api_url, api_key)

# Título de la aplicación
st.title("AI Image Generator")

# Campo para que el usuario ingrese el prompt
prompt = st.text_area("Enter a description of the image you want to generate:", "")

# Botón para generar la imagen
if st.button("Generate Image"):
    if prompt:  # Asegúrate de que el prompt no esté vacío
        # Guardar el prompt para su uso futuro
        with open('prompts_history.txt', 'a') as file:
            file.write(prompt + "\n")

        # Generar la imagen
        with st.spinner("Generating..."):
            image = generator.generate_image(prompt)
            st.image(image, caption="Generated Image", use_column_width=True)
            st.success("Here is your image!")
    else:
        st.error("Please enter a prompt.")