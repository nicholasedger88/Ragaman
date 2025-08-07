from PIL import Image

# Load the original image
img = Image.open("fav.webp")

# Resize (optional, common sizes: 16x16, 32x32, 48x48)
img = img.resize((32, 32))

# Save as .ico
img.save("favicon.ico", format="ICO")
