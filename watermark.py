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
    font = ImageFont.truetype("/mnt/d/WATERMARK/Kode_Mono/static/KodeMono-Bold.ttf", 40)
    
    # Initialize ImageDraw
    d = ImageDraw.Draw(txt)

    # fill = (255,255,255,128)  # Semi-transparent white
    width, height = original_image.size

    # Function to calculate text size
    def get_text_size(text, font):
        im = Image.new('RGB', (1, 1))
        draw = ImageDraw.Draw(im)
        bbox = draw.textbbox((0, 0), text, font=font)
        width = bbox[2] - bbox[0]
        height = bbox[3] - bbox[1]
        return width, height

    # Use the function to get text width and height
    textwidth, textheight = get_text_size(watermark_text, font)

    # Calculate position for the text
    fill = (255,255,255,120)  # Semi-transparent white
    width, height = original_image.size
    x, y = (width - textwidth) / 5, (height - textheight) / 5  

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
