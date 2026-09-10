"""
PRODIGY_CS_02 - Image Encryption Tool
Author: Ayan Sarkar
Task: Develop a simple image encryption tool using pixel manipulation.
"""

import os
import sys
from PIL import Image
import random

def get_user_input():
    """Get image path and secret key from user."""
    while True:
        path = input("\nEnter image path (e.g., input_images/image.jpg): ").strip()
        if not path:
            print("[!] Path cannot be empty.")
            continue
        if not os.path.exists(path):
            print(f"[!] Error: File not found at '{path}'")
            continue

        # Check if file is an image
        if not path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')):
            print("[!] Error: Unsupported file format. Please use PNG, JPG, JPEG, BMP, GIF, or TIFF.")
            continue

        while True:
            try:
                key = int(input("Enter secret numeric key (integer): ").strip())
                return path, key
            except ValueError:
                print("[!] Invalid input. Key must be an integer.")


    """
    Generates a pseudo-random byte stream based on pixel coordinates and the secret key.
    This ensures the encryption is not uniform across the image, making it more robust.
    """
    # Using a simple PRNG seeded by coordinates and key
def key_stream(x, y, key):
    random.seed(f"{x}_{y}_{key}")
    return random.randint(0, 255)

def encrypt_pixel(r, g, b, x, y, key):
    """
    Encrypts a single pixel's RGB values using modular arithmetic.
    Encryption formula: (Value + Stream) % 256
    """
    stream = key_stream(x, y, key)
    # Apply modular addition to ensure the value stays within 0-255
    encrypted_r = (r + stream) % 256
    encrypted_g = (g + stream) % 256
    encrypted_b = (b + stream) % 256
    return encrypted_r, encrypted_g, encrypted_b

def decrypt_pixel(r, g, b, x, y, key):
    """
    Decrypts a single pixel's RGB values.
    Decryption formula: (Value - Stream + 256) % 256
    Because (r + stream) % 256 is encrypted_r,
    (encrypted_r - stream + 256) % 256 will restore r.
    """
    stream = key_stream(x, y, key)
    # Subtract the stream and add 256 before modulo to handle negative results in Python
    decrypted_r = (r - stream + 256) % 256
    decrypted_g = (g - stream + 256) % 256
    decrypted_b = (b - stream + 256) % 256
    return decrypted_r, decrypted_g, decrypted_b

def process_image(input_path, output_path, key, mode):
    """
    Main function to process the image.
    mode: 'encrypt' or 'decrypt'
    """
    try:
        # Open the image and convert to RGB to ensure 3 channels
        img = Image.open(input_path).convert('RGB')
        width, height = img.size
        pixels = img.load()

        print(f"[*] Processing {width}x{height} image...")

        # Iterate through each pixel in the image
        for y in range(height):
            for x in range(width):
                r, g, b = pixels[x, y]

                if mode == 'encrypt':
                    new_r, new_g, new_b = encrypt_pixel(r, g, b, x, y, key)
                else:
                    new_r, new_g, new_b = decrypt_pixel(r, g, b, x, y, key)

                pixels[x, y] = (new_r, new_g, new_b)

        # Save the processed image
        img.save(output_path)
        print(f"[+] Success! Image saved to '{output_path}'")

    except Exception as e:
        print(f"[!] An error occurred during processing: {e}")

def main():
    """Main menu loop."""
    print("="*50)
    print("   PRODIGY_CS_02: IMAGE ENCRYPTION TOOL")
    print("="*50)

    while True:
        print("\n--- MENU ---")
        print("1. Encrypt Image")
        print("2. Decrypt Image")
        print("3. Exit")

        choice = input("Select an option (1-3): ").strip()

        if choice == '1':
            path, key = get_user_input()
            filename = os.path.basename(path)
            output_path = os.path.join("output_images", f"encrypted_{filename}")
            process_image(path, output_path, key, 'encrypt')

        elif choice == '2':
            path, key = get_user_input()
            filename = os.path.basename(path)
            output_path = os.path.join("output_images", f"decrypted_{filename}")
            process_image(path, output_path, key, 'decrypt')

        elif choice == '3':
            print("Exiting program. Goodbye!")
            sys.exit()

        else:
            print("[!] Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    # Ensure output directory exists
    if not os.path.exists("output_images"):
        os.makedirs("output_images")
    main()
