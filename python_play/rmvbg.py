# Remove image background

# pip install rembg
from rembg import remove
from PIL import Image
input_img = "D:/Liz/liz.png"
print("Removing....")
output_img = "bgremoved_img.png"
input = Image.open(input_img)
output = remove(input)
output.save(output_img)