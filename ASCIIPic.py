import PIL
from PIL import Image, ImageDraw, ImageFont

# ASCII characters used to build output text
ASCII_Chars = ["@","#","$","%","^","&","*","+",";",":",",","."]

# resizing image according to new width
def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width / 1.65  # Adjusted ratio for better aspect in ASCII
    new_height = int(ratio * new_width)
    resized_image = image.resize((new_width, new_height))
    return(resized_image)

# convert each pixel to grayscale
def grayify(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)

# convert pixels to a string of ASCII Characters 
def pixel_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_Chars[pixel//25] for pixel in pixels])
    return(characters)

def save_ascii_as_image(ascii_image, font_size=10, output_file="ascii_image.jpg"):
    lines = ascii_image.split("\n")
    width = max(len(line) for line in lines) * font_size // 2
    height = len(lines) * font_size

    # Create a white background
    img = Image.new("RGB", (width, height), color="white")
    draw = ImageDraw.Draw(img)

    # Use default font
    font = ImageFont.load_default()

    # Draw ASCII art line by line
    y = 0
    for line in lines:
        draw.text((0, y), line, fill="black", font=font)
        y += font_size

    img.save(output_file)
    print(f"✅ ASCII art saved as {output_file}")


def main(new_width=100):
    # attempt to open image from user-input

    path = input("Enter a valid pathname to an image:\n").strip()

    try:
        image = PIL.Image.open(path)
    except Exception as e:
        print(f"{path} is not a valid path. Error: {e}")
        return
    
    # convert image to ascii
    new_image_data = pixel_to_ascii(grayify(resize_image(image)))

    # format
    pixel_count = len(new_image_data)
    ascii_image = "\n".join(new_image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))

    # print result
    print(ascii_image)

    # saving..,
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)

    # save result to an image file (NEW FEATURE)
    save_ascii_as_image(ascii_image, font_size=10, output_file="ascii_image.jpg")


if __name__ == "__main__":
    main()