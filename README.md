# PRODIGY_CS_02: Image Encryption Tool

![Language](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Library](https://img.shields.io/badge/Pillow-9.0+-red.svg)
![Task](https://img.shields.io/badge/Task-Cyber%20Security%20Internship-green.svg)

A professional-grade image encryption tool developed as part of the Prodigy InfoTech Cyber Security Internship. This tool allows users to encrypt and decrypt images using a secret numeric key, leveraging key-based pixel manipulation.

---

## 📋 Project Overview

This project fulfills Task 2 of the Prodigy InfoTech Cyber Security Internship. It moves beyond basic XOR encryption by implementing a **Keyed Stream Cipher** approach. The tool modifies pixel values using modular arithmetic, where the transformation is unique for every pixel based on its coordinates and a secret key.

## ✨ Features

- **Key-Based Encryption**: Uses a numeric integer as a secret key.
- **Keyed Stream Cipher**: Generates a pseudo-random stream based on `(x, y, key)`, making the encryption resistant to simple frequency analysis.
- **Pixel Manipulation**: Modifies RGB values using modular arithmetic to preserve image integrity.
- **Quality Preservation**: Decrypted images are bit-for-bit identical to the original (lossless).
- **Robust Error Handling**: Catches invalid files, unsupported formats, and non-numeric keys.
- **Menu-Driven Interface**: User-friendly CLI interface for easy operation.

---

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- Pip (Python package manager)

### Steps
1. **Clone the repository:**
   ```bash
   git clone https://github.com/sroyayan/PRODIGY_CS_02.git
   cd PRODIGY_CS_02
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🛠️ Usage

1. **Run the tool:**
   ```bash
   python image_encryptor.py
   ```

2. **Follow the menu:**
   - Select `1` to Encrypt an image.
   - Select `2` to Decrypt an image.
   - Select `3` to Exit.

3. **Input:**
   - Provide the path to the image (e.g., `input_images/sample.jpg`).
   - Enter your secret numeric key when prompted.

### Example Session
```text
==================================================
   PRODIGY_CS_02: IMAGE ENCRYPTION TOOL
==================================================

--- MENU ---
1. Encrypt Image
2. Decrypt Image
3. Exit
Select an option (1-3): 1

Enter image path (e.g., input_images/image.jpg): input_images/photo.jpg
Enter secret numeric key (integer): 12345
[*] Processing 1920x1080 image...
[+] Success! Image saved to 'output_images/encrypted_photo.jpg'
```

---

## 🔒 Encryption Algorithm Explained

### How it Works
The tool uses **Modular Arithmetic** combined with a **Pseudo-Random Number Generator (PRNG)** seeded by coordinates and the key.

1. **Key Stream Generation**:
   For a pixel at `(x, y)` and key `K`, a stream byte `S` is generated:
   `S = PRNG(x, y, K)`

2. **Encryption**:
   Each RGB channel `C` is transformed:
   `C_encrypted = (C + S) mod 256`

3. **Decryption**:
   To reverse the process:
   `C_original = (C_encrypted - S + 256) mod 256`

### Why Decryption Restores the Original
Because we are working in modulo 256 (the range of a byte), adding a value and then subtracting it returns the original value.
`(C + S) mod 256 = C_encrypted`
`(C_encrypted - S) mod 256 = C`
The `+ 256` in decryption ensures that even if `C_encrypted < S`, the result is positive before the modulo operation, preventing Python's negative modulo behavior from corrupting the data.

---



## 📚 Learning Outcomes

- Understanding of **Image Processing** and pixel-level manipulation.
- Application of **Modular Arithmetic** in cryptography.
- Implementation of **Stream Ciphers** using coordinate-based seeding.
- Writing clean, modular, and documented Python code.
- Handling file I/O and error states in a CLI environment.

---

## 📜 License

This project is part of the Prodigy InfoTech Internship Program.
