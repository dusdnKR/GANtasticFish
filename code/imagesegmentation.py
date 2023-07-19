import os
from rembg import remove
from PIL import Image

# Create a directory to save the processed images
if not os.path.exists("removed"):
    os.makedirs("removed")

# Loop through all the image files in the current directory
for filename in os.listdir():
    if filename.endswith(".png"):
        # Load the image
        img = Image.open(filename)

        # Remove the background
        out = remove(img)

        # Save the processed image in the "removed" directory
        out_path = os.path.join("removed", f"{filename[:-4]}_removed.png")
        out.save(out_path)

print("Background removal completed!")