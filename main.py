from PIL import Image, ImageDraw, ImageFont

def apply_watermark(image_path, watermark_text, output_path):
    image = Image.open(image_path).convert("RGBA")
    txt = Image.new("RGBA", image.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(txt)
    font = ImageFont.truetype("arial.ttf", 50)
    bbox = draw.textbbox((0, 0), watermark_text, font=font)
    text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
    x = image.width - text_width - 10
    y = image.height - text_height - 10
    draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, 128))
    watermarked = Image.alpha_composite(image, txt)
    watermarked.save(output_path, "PNG")
    print("Watermark appliqué avec succès!")

image_path = "image.png"
watermark_text = "instagram.com/light2k4"
output_path = "output/image_w.png"

apply_watermark(image_path, watermark_text, output_path)