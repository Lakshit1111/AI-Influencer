import os
from ImageGenerator import ImageGenerator
import logging
from dotenv import load_dotenv

# Carga las variables de entorno desde el archivo .env
load_dotenv()

def main():
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting main function.")

    # Obtiene la URL de la API y la clave API de las variables de entorno
    api_url = os.getenv("API_URL")
    api_key = os.getenv("API_KEY")

    if not api_url or not api_key:
        logging.error("API URL or API Key not found in environment variables.")
        return

    generator = ImageGenerator(api_url, api_key)

    prompt = "The image captures a woman exuding a sultry confidence with an alluring smile that plays at the corners of her mouth. She appears to be in her 30s, with a form that marries elegance and sensuality, standing tall with a posture that is both inviting and assertive.Hair:Her hair is a striking shade of red, cascading down in long, straight locks that frame her face and spill over her shoulders, creating a bold curtain of color. The texture is glossy, suggesting the touch would be as luxurious as the visual appeal, each strand catching and reflecting the light to enhance her fiery aura.Face and Makeup:Her complexion is porcelain, a fair canvas graced by the delicate dusting of freckles that speak to a playful youthfulness. Her makeup is dramatic yet tastefully applied, with emerald eyeshadow providing a stark, mesmerizing contrast to her vibrant tresses, and a sharp black liner that outlines her piercing gaze. Her lashes arch long and full, flirtatiously framing her eyes, while her lips are painted in a soft pink, glossy and full, hinting at an untold promise.Attire:She is adorned in a cream-white suit jacket that artfully toes the line between professional and provocative. The jacket is tailored to perfection, skimming her form in a way that suggests rather than reveals. Adorned with beaded details that catch the light, the garment adds a layer of sophistication to her daring ensemble.Accessories:Dangling from her ears are earrings that could be diamonds or crystals, their sparkle matched only by the twinkle in her eye, adding an understated yet unmistakable opulence to her look.Lighting and Background:The ambiance is set by lighting that seems to halo her, soft and golden, suggesting an outdoor setting where the sun plays favorably on her features. Behind her is a stark white wall, devoid of distraction, ensuring that she remains the undisputed focal point. The overall image is one of refined allure, where each element from her vibrant hair to her impeccably chosen attire is a testament to a woman who owns her sexuality with grace and poise. The artist tasked with recreating this vision must balance the vibrancy of her hair with the subtlety of her makeup and the precise fit of her suit to capture the magnetic charm she embodies."
    logging.info(f"Using prompt: {prompt}")

    image = generator.generate_image(prompt)

    image.show()
    logging.info("Image displayed.")

if __name__ == "__main__":
    main()
