import requests
from PIL import Image
from io import BytesIO

# ⚡ FREE FAST API (no download models)
API_URL = "https://image.pollinations.ai/prompt/"

def generate_image(prompt):
    url = API_URL + prompt

    response = requests.get(url)

    image = Image.open(BytesIO(response.content))
    image.save("output.png")

    print("✅ Image created instantly: output.png")


# ================= MAIN =================
prompt = input("Enter prompt: ")
generate_image(prompt)