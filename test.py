from PIL import Image, ImageDraw, ImageFont
import cv2
import numpy as np

# Создание изображения
text = input()

font = ImageFont.truetype('arial.ttf', size=90)
text_width, text_height = font.getsize(text)
img_width = text_width
img_height = 100

img = Image.new('RGB', (img_width, img_height), color='white')
draw = ImageDraw.Draw(img)
draw.text((0, 0), text, fill='black', font=font)


# Создание видео
image = np.array(img)

output_video = cv2.VideoWriter('output.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 24, (100, 100))

window_width = 100
FPS = 24
duration_seconds = 3
total_frames = FPS * duration_seconds

for i in range(total_frames):
    x = (img_width - window_width + 1) * i // total_frames

    window = image[:, x:x+window_width]
    resized_window = cv2.resize(window, (100, 100))
    output_video.write(cv2.cvtColor(resized_window, cv2.COLOR_BGR2RGB))


output_video.release()