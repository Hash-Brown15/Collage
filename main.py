import os
import cv2
from PIL import Image 

os.chdir("/Users/jinheppell/Desktop/collage/photos")
path = ("/Users/jinheppell/Desktop/collage/photos")

mean_height = 0
mean_width = 0

num_of_images = len(os.listdir('.'))

for file in os.listdir('.'):
    img = Image.open(os.path.join(path, file))
    width, height = img.size
    mean_width = mean_width + width
    mean_height = mean_height + height

mean_width = mean_width // num_of_images
mean_height = mean_height // num_of_images

print(mean_width)
print(mean_height)

for file in os.listdir('.'):
    if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):
        imgResized = img.resize((mean_width, mean_height),Image.ANTIALIAS)
        imgResized.save(file, 'JPEG', quality = 95)
        print(img.filename.split('\\')[-1], " is resized")

def videoGenerator():
    video_name = "MyfirstVideo.avi"

    os.chdir("/Users/jinheppell/Desktop/collage/photos")

    images = []
    for img in os.listdir('.'):
        if img.endswith('.jpg') or img.endswith('.jpeg') or img.endswith('.png'):
            images.append(img)

    print(images)

    frame = cv2.imread(os.path.join(".", images[0]))

    height, width, layers = frame.shape
    video = cv2.VideoWriter(video_name, 0, 1, (width, height))

    for image in images:
        video.write(cv2.imread(os.path.join(".",image)))

    cv2.destroyAllWindows()
    video.release()

videoGenerator()