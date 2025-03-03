import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

def decode_image(image_path, key):
    image = Image.open(image_path)
    pixels = image.load()

    width, height = image.size
    binary_message = ''
    end_marker = '1111111111111110'
    
    for y in range(height):
        for x in range(width):
            for color in range(3):
                pixel_value = pixels[x, y][color]
                binary_message += str(pixel_value & 1)

                if len(binary_message) >= len(end_marker) and binary_message[-len(end_marker):] == end_marker:
                    break
            if len(binary_message) >= len(end_marker) and binary_message[-len(end_marker):] == end_marker:
                break
        if len(binary_message) >= len(end_marker) and binary_message[-len(end_marker):] == end_marker:
            break

    binary_message = binary_message[:-len(end_marker)]

    encoded_message = ''
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        if len(byte) == 8:
            encoded_message += chr(int(byte, 2))

    decoded_message = ''.join(chr(ord(char) ^ key) for char in encoded_message)
    return decoded_message

def select_image():
    file_path = filedialog.askopenfilename(title="Select Encoded Image", filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    if file_path:
        encoded_image_path.set(file_path)

def decode():
    try:
        decoded_message = decode_image(encoded_image_path.get(), int(key.get()))
        decoded_message_output.set(decoded_message)
        messagebox.showinfo("Success", "Message decoded successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI Setup
root = tk.Tk()
root.title("Image Steganography - Decoding")

# Variables
encoded_image_path = tk.StringVar()
key = tk.StringVar()
decoded_message_output = tk.StringVar()

# Widgets
tk.Label(root, text="Select Encoded Image:").grid(row=0, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=encoded_image_path, width=40).grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=select_image).grid(row=0, column=2, padx=10, pady=10)

tk.Label(root, text="Key:").grid(row=1, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=key, width=40).grid(row=1, column=1, padx=10, pady=10)

tk.Button(root, text="Decode", command=decode).grid(row=2, column=0, columnspan=3, padx=10, pady=20)

tk.Label(root, text="Decoded Message:").grid(row=3, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=decoded_message_output, width=40, state='readonly').grid(row=3, column=1, padx=10, pady=10)

root.mainloop()
