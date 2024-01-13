
import sys, os
dirname = os.path.dirname(__file__)
sys.path.append(os.path.join(dirname, "..", ".."))
from features.controller.japaneseOCR import image_to_text
from PIL import Image

image_path = os.path.join(dirname, "sample1.png")
image = Image.open(image_path)
print("processing image at: " + image_path + " ...")
text = image_to_text(image)
print("Text: " + text)
