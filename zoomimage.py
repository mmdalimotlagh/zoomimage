import cv2
from PIL import Image

def zoom_image(image_path, zoom_factor):
   
    image = Image.open(image_path)

    
    width, height = image.size
    new_width = int(width * zoom_factor)
    new_height = int(height * zoom_factor)

   
    zoomed_image = image.resize((new_width, new_height), Image.LANCZOS)

  
    zoomed_image.show()

def main():
    
    image_path = input("لطفاً مسیر عکس را وارد کنید: ")
    zoom_factor = float(input("کنيد لطفاً مقدار زوم را وارد ): "))

    zoom_image(image_path, zoom_factor)

if __name__ == "__main__":
    main()
