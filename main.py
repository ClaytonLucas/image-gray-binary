from PIL import Image
import os

INPUT_DIR = "image"
OUTPUT_DIR = "saida"

def in_file(filename):
    return os.path.join(INPUT_DIR, filename)

def out_file(filename):
    return os.path.join(OUTPUT_DIR, filename)


def grayscale(colored):
    w, h = colored.size
    img = Image.new("L", (w, h))

    for x in range(w):
        for y in range(h):
            pixel = colored.getpixel((x,y))
            lum = int(0.3*pixel[0] + 0.59*pixel[1] + 0.11*pixel[2])
            img.putpixel((x,y), lum)
    return img

def peb_image(gray, limiar=127):
    w, h = gray.size
    img = Image.new("1", (w, h))

    for x in range(w):
        for y in range(h):
            pixel = gray.getpixel((x,y))
            binary_val = 1 if pixel > limiar else 0
            img.putpixel((x,y), binary_val)
    return img
    

if __name__ == "__main__":
    img = Image.open(in_file("praia.jpg"))
    grayscale_img = grayscale(img)
    grayscale_img.save(out_file("praia_cinza.jpg"))
    binary_img = peb_image(grayscale_img)
    binary_img.save(out_file("praia_peb.jpg"))