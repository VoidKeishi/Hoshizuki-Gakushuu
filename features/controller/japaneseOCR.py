from PIL import Image
import pytesseract
import os
def image_to_text(file):
    """
    This function will handle the core OCR processing of images. input must be a string indicating the path of the image file or a pillow image object
    """
    dirname = os.path.dirname(__file__)
    pytesseract.pytesseract.tesseract_cmd = os.path.join(dirname, "TesseractOCR", "tesseract.exe")  # This is the path where tesseract is installed on my windows machine
    # check if input is a string or a pillow image object
    if isinstance(file, str):
        image = Image.open(file)
    if isinstance(file, Image.Image):
        image = file
    else:
        raise TypeError("Input must be a string or a file object or a pillow image object")
    text = pytesseract.image_to_string(image, lang="Japanese")
    return text