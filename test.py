from rembg import remove
from PIL import Image

input_image = Image.open("input.jpg")

output_image = remove(input_image)

output_image.save("output.png")

print("Background removed successfully!")
