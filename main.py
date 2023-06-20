from PIL import Image, ImageDraw, ImageFont
import os
# Open the image
image_path = r'/home/aarika/Desktop/New_OCR/data/upload/abc.jpg'  # Replace with your image path
image = Image.open(image_path)

# Create a drawing object
draw = ImageDraw.Draw(image)
# font_path = '/path/to/arial.ttf'  # Replace with the absolute path to your font file
# font = ImageFont.truetype(font_path, 16)

# Define the label text and font
label_text = 'Label'
font = ImageFont.truetype('abc.jpg', 16)  # Replace with your desired font and size

# Define the label position (top-left coordinates)
label_position = (10, 10)  # Adjust as per your preference

# Define the label color
label_color = (255, 0, 0)  # Red color (RGB format)

# Add the label to the image
draw.text(label_position, label_text, font=font, fill=label_color)

# Save the image with the label
image_with_label_path = 'image_with_label.jpg'  # Replace with the desired output path
image.save(image_with_label_path)

# Display the image
image.show()
