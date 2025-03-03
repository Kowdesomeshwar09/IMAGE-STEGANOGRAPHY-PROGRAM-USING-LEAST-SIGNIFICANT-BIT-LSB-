import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

def encode_image(input_image_path, secret_message, output_image_path, key):
    image = Image.open(input_image_path)
    pixels = image.load()

    width, height = image.size
    max_message_length = width * height * 3 // 8
    if len(secret_message) > max_message_length:
        raise ValueError("Message is too long to fit in the image")

    encoded_message = ''.join(chr(ord(char) ^ key) for char in secret_message)
    binary_message = ''.join(format(ord(char), '08b') for char in encoded_message) + '1111111111111110'
    binary_index = 0

    for y in range(height):
        for x in range(width):
            if binary_index >= len(binary_message):
                image.save(output_image_path)
                return

            pixel = list(pixels[x, y])
            for color in range(3):
                if binary_index >= len(binary_message):
                    break
                pixel_value = pixel[color]
                bit_to_encode = binary_message[binary_index]
                new_pixel_value = (pixel_value & ~1) | int(bit_to_encode)
                pixel[color] = new_pixel_value
                binary_index += 1
            pixels[x, y] = tuple(pixel)

    image.save(output_image_path)

def select_image():
    file_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    if file_path:
        input_image_path.set(file_path)

def encode():
    try:
        encode_image(input_image_path.get(), secret_message.get(), output_image_path.get(), int(key.get()))
        messagebox.showinfo("Success", "Message encoded successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI Setup
root = tk.Tk()
root.title("Image Steganography - Encoding")

# Variables
input_image_path = tk.StringVar()
output_image_path = tk.StringVar()
secret_message = tk.StringVar()
key = tk.StringVar()

# Widgets
tk.Label(root, text="Select Image:").grid(row=0, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=input_image_path, width=40).grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=select_image).grid(row=0, column=2, padx=10, pady=10)

tk.Label(root, text="Secret Message:").grid(row=1, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=secret_message, width=40).grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Output Image Path:").grid(row=2, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=output_image_path, width=40).grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="Key:").grid(row=3, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=key, width=40).grid(row=3, column=1, padx=10, pady=10)

tk.Button(root, text="Encode", command=encode).grid(row=4, column=0, columnspan=3, padx=10, pady=20)

root.mainloop()
