from PIL import Image
import io
import pymongo 
with open("documents/batista.jpeg", "rb") as image_file:
    image_data = image_file.read()

image = Image.open(io.BytesIO(image_data))
print(image)
img=image.show()
img

