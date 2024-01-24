import requests
import io
from PIL import Image
import logging

class ImageGenerator:
    def __init__(self, api_url, api_key):
        self.api_url = api_url
        self.headers = {"Authorization": f"Bearer {api_key}"}
        logging.info("ImageGenerator initialized with API URL and key.")

    def query(self, payload):
        logging.info(f"Sending request to API with payload: {payload}")
        response = requests.post(self.api_url, headers=self.headers, json=payload)
        response.raise_for_status()
        logging.info("Response received successfully.")
        return response.content

    def generate_image(self, prompt):
        logging.info(f"Generating image for prompt: '{prompt}'")
        image_bytes = self.query({"inputs": prompt})
        image = Image.open(io.BytesIO(image_bytes))
        logging.info("Image generated successfully.")
        return image
