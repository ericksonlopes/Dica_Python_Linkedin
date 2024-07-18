# pip install boto3 requests pillow

from io import BytesIO

import boto3
import requests
from PIL import Image


def download_and_convert_to_png(url_image):
    response = requests.get(url_image)

    if response.status_code != 200:
        raise Exception(f"Failed to download image from {url_image}: {response.status_code}")

    imagem = Image.open(BytesIO(response.content))
    imagem_png_bytes = BytesIO()
    imagem.save(imagem_png_bytes, "PNG")

    return imagem_png_bytes.getvalue()


def upload_image_to_bucket(bucket_name, key, image_bytes):
    s3 = boto3.client("s3")
    s3.put_object(Bucket=bucket_name, Key=key, Body=image_bytes)


url_image = "https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png"
bucket_name = "my_bucket"
key = "sua_key"

image_bytes = download_and_convert_to_png(url_image)
upload_image_to_bucket(bucket_name, key, image_bytes)
