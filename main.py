from PIL import Image

img = Image.open('kitty.png')
pixels = list(img.getdata())

# Пример: вывод первых 100 пикселей
for i in range(100):
    print(pixels[i])
