#!/usr/bin/env python3

from PIL import Image
import numpy as np
import sys

class ImageSteganography:
    def __init__(self):
        self.delimiter = "###END###"
    
    def text_to_binary(self, text):
        """
        Convert text string to binary representation.
        
        Args:
            text: String to convert
        
        Returns:
            Binary string representation
        """
        # TODO: Convert each character to 8-bit binary
        # Hint: Use ord() and format()
        pass

    def compare_images(self, original_path, modified_path):
    """
    Compare original and steganographic images.
    
    Args:
        original_path: Path to original image
        modified_path: Path to modified image
    """
    # TODO: Load both images
    # TODO: Convert to numpy arrays
    # TODO: Calculate pixel differences
    # TODO: Compute statistics (max diff, average diff, count)
    # TODO: Display comparison results
    pass

    def binary_to_text(self, binary_data):
        """
        Convert binary string back to text.
        
        Args:
            binary_data: Binary string
        
        Returns:
            Decoded text string
        """
        # TODO: Process binary data in 8-bit chunks
        # TODO: Convert each byte to character using chr()
        pass
    
    def hide_message(self, image_path, message, output_path):
        """
        Hide a text message in an image using LSB steganography.
        
        Args:
            image_path: Path to cover image
            message: Text message to hide
            output_path: Path for output image
        
        Returns:
            True if successful, False otherwise
        """
        try:
            # TODO: Open image and convert to RGB
            # TODO: Convert image to numpy array
            # TODO: Prepare message with delimiter
            # TODO: Convert message to binary
            # TODO: Check if image can hold the message
            # TODO: Flatten image array
            # TODO: Modify LSB of each pixel with message bits
            # TODO: Reshape and save modified image
            
            print(f"Message successfully hidden in {output_path}")
            return True
            
        except Exception as e:
            print(f"Error: {str(e)}")
            return False
    
    def extract_message(self, image_path):
        """
        Extract hidden message from steganographic image.
        
        Args:
            image_path: Path to steganographic image
        
        Returns:
            Extracted message or None
        """
        try:
            # TODO: Open image and convert to RGB
            # TODO: Convert to numpy array and flatten
            # TODO: Extract LSB from each pixel value
            # TODO: Convert binary data to text
            # TODO: Find delimiter and extract message
            
            return None
            
        except Exception as e:
            print(f"Error: {str(e)}")
            return None

def main():
    stego = ImageSteganography()
    
    if len(sys.argv) < 2:
        print("Usage:")
        print("  Hide: python3 steganography_tool.py hide <image> <message> <output>")
        print("  Extract: python3 steganography_tool.py extract <image>")
        return
    
    command = sys.argv[1].lower()
    
    if command == "hide" and len(sys.argv) == 5:
        stego.hide_message(sys.argv[2], sys.argv[3], sys.argv[4])
    elif command == "extract" and len(sys.argv) == 3:
        stego.extract_message(sys.argv[2])
    else:
        print("Invalid command or arguments!")

if __name__ == "__main__":
    main()

import hashlib
import base64

def encrypt_message(self, message, password):
    """
    Encrypt message using XOR cipher with password.

    Args:
        message: Plain text message
        password: Encryption password

    Returns:
        Encrypted message (base64 encoded)
    """
    # TODO: Generate key from password using MD5 hash
    # TODO: XOR each character with key
    # TODO: Encode result in base64
    pass

def decrypt_message(self, encrypted_message, password):
    """
    Decrypt XOR encrypted message.

    Args:
        encrypted_message: Encrypted message (base64)
        password: Decryption password

    Returns:
        Decrypted plain text
    """
    # TODO: Decode base64
    # TODO: Generate same key from password
    # TODO: XOR to decrypt
    pass
