from PIL import Image

img = Image.open("fav.webp")  # or .png/.jpg
img = img.resize((180, 180))
img.save("apple-touch-icon.png", format="PNG")
