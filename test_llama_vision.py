import os
import glob

def get_latest_screenshot_path(screenshot_folder):
    # Use glob to find all png and jpg files in the folder
    screenshots = glob.glob(os.path.join(screenshot_folder, '*.png')) + glob.glob(os.path.join(screenshot_folder, '*.jpg'))
    if not screenshots:
        return None
    # Get the latest file based on modification time
    latest_screenshot = max(screenshots, key=os.path.getmtime)
    return latest_screenshot

# Example usage
screenshot_folder = 'C:/Users/gl/OneDrive/图片/Screenshots'  # Replace with your actual folder path
latest_image_path = get_latest_screenshot_path(screenshot_folder)
print(latest_image_path)

api_key = "hf_FZGHifwSLtbHMpb"
api_key += "zWmMktyjrBfXKMICbup"
base_url = "https://api-inference.huggingface.co/models/meta-llama/Llama-3.2-11B-Vision-Instruct/v1"
model = "meta-llama/Llama-3.2-11B-Vision-Instruct"

import base64
from openai import OpenAI

client = OpenAI(api_key=api_key,base_url=base_url)

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your image
image_path = latest_image_path

# Getting the base64 string
base64_image = encode_image(image_path)

response = client.chat.completions.create(
  model=model,
  messages=[
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "give me url",
        },
        {
          "type": "image_url",
          "image_url": {
            "url":  f"data:image/png;base64,{base64_image}"
          },
        },
      ],
    }
  ],
)

url = response.choices[0].message.content
print(url)

import webbrowser

# 使用默认浏览器打开URL
webbrowser.open(url)
