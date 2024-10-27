import os
import glob

def get_latest_screenshot_path2():
  # 假设屏幕截图文件夹路径为用户的图片文件夹下的"Screenshots"
  screenshot_folder = os.path.join(os.path.expanduser("~"), "Pictures", "Screenshots")
  # 获取所有截图文件
  screenshots = glob.glob(os.path.join(screenshot_folder, "*.png"))  # 假设截图为PNG格式
  if not screenshots:
      print("没有找到截图文件。")
  # 获取最新的截图文件
  latest_screenshot = max(screenshots, key=os.path.getctime)
  print("最新的截图文件路径:", latest_screenshot)
  return latest_screenshot

def get_latest_screenshot_path(screenshot_folder):
    # Use glob to find all png and jpg files in the folder
    screenshots = glob.glob(os.path.join(screenshot_folder, '*.png')) + glob.glob(os.path.join(screenshot_folder, '*.jpg'))
    if not screenshots:
        return get_latest_screenshot_path2()
    # Get the latest file based on modification time
    latest_screenshot = max(screenshots, key=os.path.getmtime)
    return latest_screenshot

# Example usage
screenshot_folder = 'C:/Users/gl/OneDrive/图片/Screenshots'  # Replace with your actual folder path
latest_image_path = get_latest_screenshot_path(screenshot_folder)
print(latest_image_path)

model = "google/gemini-flash-1.5-8b"
base_url = "https://openrouter.ai/api/v1"
api_key = "sk-or-v1-7f34389befc90c10fe888a8"
api_key += "c787a981f0710a913e45e59e11632793531358ff5"

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
          "text": "提取这个浏览器截图的网页地址,然后只输出网址",
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
