# importing the Image and ImageDraw classes from PIL library
from PIL import Image, ImageDraw, ImageFont

def watermark_image(input_image_path, output_image_path, watermark_text):
    """
    This function adds a text watermark to an image.
    :param input_image_path: Path to the input image.
    :param output_image_path: Path where the watermarked image will be saved.
    :param watermark_text: Text to be used as the watermark.
    """
    # Open the input image
    original_image = Image.open(input_image_path).convert('RGBA')
    
    # Make the image editable
    txt = Image.new('RGBA', original_image.size, (255,255,255,0))

    # Choose a font and size for the watermark
    # font = ImageFont.load_default()
    font = ImageFont.truetype("arial.ttf", 40)
    
    # Initialize ImageDraw
    d = ImageDraw.Draw(txt)

    # Apply the watermark text
    # d.text((10,10), watermark_text, fill=(255,255,255,128), font=font)
    # fill = (255,255,255,128)  # Semi-transparent white
    # x, y = 10, 10  # Adjust as needed
    # for offset in range(10):  # Adjust the range for bolder text
    #     d.text((x+offset, y+offset), watermark_text, font=font, fill=fill)

    fill = (255,255,255,128)  # Semi-transparent white
    width, height = original_image.size
    textwidth, textheight = d.textsize(watermark_text, font=font)
    x, y = (width - textwidth) / 2, (height - textheight) / 2  # Center the text

    # Draw the text onto the overlay image
    d.text((x, y), watermark_text, font=font, fill=fill)

    # Combine the image with the watermark
    watermarked = Image.alpha_composite(original_image, txt)

    # Convert the result to 'RGB' to save as JPEG or other formats not supporting transparency
    watermarked_rgb = watermarked.convert('RGB')
    
    # Save the watermarked image
    watermarked_rgb.save(output_image_path)
# Example usage:
watermark_image('image.png', 'watermarked_image.jpg', 'Jerry')
