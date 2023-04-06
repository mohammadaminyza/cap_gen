import glob
import random
import string
import os  # Import the os module to create folder
from PIL import Image, ImageDraw, ImageFont

for i in range(1000000):

    # Captcha configuration
    captcha_width = 250
    captcha_height = 50
    captcha_text_length = random.randint(5, 7)
    captcha_noise_level = 90
    captcha_text_color = random.choice(["black", "white", "gray", "blue", "wheat", "orange"])
    captcha_bg_color = random.choice(["black", "white", "gray", "wheat", "orange"])
    captcha_shadow_color = random.choice(["black", "white", "gray", "blue", "green", "wheat", "orange"])

    if captcha_bg_color == captcha_text_color:
        choices = ["black", "white", "gray", "wheat", "orange"]
        choices.remove(captcha_text_color)
        captcha_bg_color = random.choice(choices)

    size = random.randint(33, 39)
    rotation_angle = random.randint(-5, 5)  # Random rotation angle

    # Generate random text for captcha
    # captcha_text = ''.join(random.choices(string.ascii_letters + string.digits, k=captcha_text_length))
    captcha_text = ''.join(random.choices(string.digits, k=captcha_text_length))

    # Create blank image
    captcha_image = Image.new('RGB', (captcha_width, captcha_height), color=captcha_bg_color)
    draw = ImageDraw.Draw(captcha_image)

    # Add text to the image with shadow and rotation
    # Drawing text and lines
    font_path = r"C:\Windows\Fonts"
    fonts = glob.glob(font_path + '\\ari*.ttf')
    font = ImageFont.truetype(random.choice(fonts), size)  # Increased text size
    text_width, text_height = draw.textsize(captcha_text, font=font)
    text_x = max((captcha_width - text_width) // 2, 0)  # Ensure text does not go out of image boundary
    text_y = max((captcha_height - text_height) // 2, 0)  # Ensure text does not go out of image boundary

    # Add random rotation to the character
    rotated_text = Image.new('RGBA', (text_width, text_height), (0, 0, 0, 0))
    rotated_text_draw = ImageDraw.Draw(rotated_text)
    rotated_text_draw.text((0, 0), captcha_text, fill=captcha_text_color, font=font)
    rotated_text = rotated_text.rotate(rotation_angle, expand=1)

    # Add padding around the character
    padding = 1

    # Add shadow to the character
    shadow = Image.new('RGBA', (text_width, text_height), (0, 0, 0, 0))
    shadow_draw = ImageDraw.Draw(shadow)
    shadow_draw.text((padding, padding), captcha_text, fill=captcha_shadow_color, font=font)
    shadow = shadow.rotate(rotation_angle, expand=1)

    # Paste the shadow on the captcha image
    shadow_x = max(text_x - 5, 0)  # Move shadow text 5 pixels to the left
    shadow_y = max(int((captcha_height / 4)) + random.randint(1, 3), 0)  # Move shadow text higher
    captcha_image.paste(shadow, (shadow_x, shadow_y), shadow)  # Adjusted shadow position

    # Paste the rotated text on the captcha image
    captcha_image.paste(rotated_text, (text_x, text_y), rotated_text)

    # Add noise to the image
    for _ in range(captcha_noise_level):
        x = random.randint(0, captcha_width)
        y = random.randint(0, captcha_height)
        draw.point((x, y), fill="black")

    # Save the captcha image
    if not os.path.exists("captcha_images_v2"):  # Check if folder exists, if not, create it
        os.makedirs("captcha_images_v2")
    captcha_image.save(f"captcha_images_v2/{captcha_text}.png")

    print(f"{i} captcha image saved! {1000000 - i} left!")
