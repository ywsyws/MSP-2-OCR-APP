# image_path = "C:\Users\MPNH3677\workspace\MSP-2-OCR-APP\images\WMM+LOGO.jpg"
# print(image_path)
import os

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))