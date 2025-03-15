# Image Steganography Using Least Significant Bit (LSB)

## Overview
This project implements an **image steganography** program using the **Least Significant Bit (LSB)** technique. The program allows users to **encode** a secret message into an image and **decode** it later. By modifying the least significant bits of the pixel values, the message is embedded in a way that is **imperceptible** to the human eye.

## Features
- **Encode messages into images** using LSB steganography
- **Decode hidden messages** from steganographic images
- Supports **standard image formats** (PNG, JPEG, BMP, etc.)
- Simple command-line interface for ease of use
- Written in **Python** with the **Pillow** library for image processing
- Extendable for larger messages and alternative steganographic techniques

## Dependencies
Ensure you have the following dependencies installed:

pip install pillow numpy

### Required Libraries:
- **Python 3.x**
- **Pillow** (for image manipulation)
- **NumPy** (for array processing)

## Installation
1. Clone the repository:
   
   git clone https://github.com/yourusername/image-steganography.git
   cd image-steganography
   
2. Install dependencies:
   
   pip install -r requirements.txt
   
## Usage
### Encoding a Message into an Image

   python encode.py input_image.png "Your secret message" output_image.png
   
- `input_image.png` → The original image
- `"Your secret message"` → The message to hide
- `output_image.png` → The generated steganographic image

### Decoding a Message from an Image

   python decode.py output_image.png
   
This will extract and display the hidden message.

## Example
Encoding:

   python encode.py example.png "Hello, World!" encoded.png
   
Decoding:

   python decode.py encoded.png
   
Output:

   Decoded Message: Hello, World!
   
## Contributing
Contributions are welcome! Feel free to submit **issues** and **pull requests**.

## License
This project is licensed under the **MIT License**.

---
Developed by KOWDE SOMESHWAR 🚀

