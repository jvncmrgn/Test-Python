from PIL import Image, ImageOps

def main():
    try:
        #Relative Path
        img = Image.open("gambar1.jpg") 
        print(img.mode)
          
        #converting image to bitmap
        print(img.tobitmap())
          
        print(type(img.tobitmap()))
    except IOError:
        pass
  
if __name__ == "__main__":
    main()