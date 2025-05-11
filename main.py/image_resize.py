from PIL import Image
import os

def resize_with_background(input_path, output_path, target_size=(1274, 956)):
    image = Image.open(input_path)
    image_ratio = image.width / image.height
    target_ratio = target_size[0] / target_size[1]

    # Вычисляем новый размер, сохраняя пропорции
    if image_ratio > target_ratio:
        new_width = target_size[0]
        new_height = int(target_size[0] / image_ratio)
    else:
        new_height = target_size[1]
        new_width = int(target_size[1] * image_ratio)

    image = image.resize((new_width, new_height), Image.LANCZOS)

    # Создаём фон на основе угла изображения
    corner_color = image.getpixel((0, 0))
    background = Image.new("RGB", target_size, color=corner_color)

    # Вставляем изображение по центру
    offset = ((target_size[0] - new_width) // 2, (target_size[1] - new_height) // 2)
    background.paste(image, offset)
    background.save(output_path)

# Пример использования
if __name__ == "__main__":
    input_file = "input.jpg"
    output_file = "output.jpg"
    resize_with_background(input_file, output_file)