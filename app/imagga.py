import requests
import os

def get_image_tags(image_file):
    # Endpoint de Imagga para etiquetar imágenes
    url = 'https://api.imagga.com/v2/tags'

    # Enviar la imagen a la API de Imagga
    response = requests.post(
        url,
        auth=(os.getenv('acc_0c2aa3a2bad0abd'), os.getenv('d6038f2ccf5b1a2db5df45f55fbbf1e8')),
        files={'image': image_file}
    )

    # Verificar si la respuesta es exitosa
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.text}
