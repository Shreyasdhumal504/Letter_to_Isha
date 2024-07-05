from PIL import Image, ImageDraw, ImageFont

# Create an image for the letter
letter_image = Image.new('RGB', (600, 400), color='white')
draw = ImageDraw.Draw(letter_image)
font = ImageFont.truetype("arial.ttf", 15)
message = "Dear Mayalu,\n\nThis is it, Ishaaaa! The moment you've been preparing for..."
draw.text((10, 10), message, fill="black", font=font)
letter_image.save('letter.png')

# Create heart images
heart_image = Image.new('RGB', (50, 50), color='red')
draw = ImageDraw.Draw(heart_image)
draw.polygon([(25, 0), (50, 25), (25, 50), (0, 25)], fill='red')
heart_image.save('heart.png')
