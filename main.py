import os
import cv2
from PIL import Image 

os.chdir("/Users/jinheppell/Desktop/collage/photos")
path = "/Users/jinheppell/Desktop/collage/photos"

mean_height = 0
mean_width = 0

valid_images = []
for file in os.listdir('.'):
    if file.lower().endswith(('.jpg' ,'.jpeg' ,'.png')):
        valid_images.append(file)
        
num_of_images = len(valid_images)        
for file in valid_images:
    img = Image.open(os.path.join(path, file))
    width, height = img.size
    mean_width = mean_width + width
    mean_height = mean_height + height

mean_width = mean_width // num_of_images
mean_height = mean_height // num_of_images

print(mean_width)
print(mean_height)

for file in valid_images:
    if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):
        img = Image.open(os.path.join(path,file))
        width,height = img.size
        imgResized = img.resize((mean_width, mean_height),Image.Resampling.LANCZOS)
        imgResized.save(file, 'JPEG', quality = 95)
        print(img.filename.split('\\')[-1], " is resized")

def videoGenerator():
    video_name = "MyfirstVideo.avi"

    os.chdir("/Users/jinheppell/Desktop/collage/photos")

    images = []
    for img in valid_images:
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