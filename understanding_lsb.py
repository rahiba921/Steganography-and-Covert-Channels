#!/usr/bin/env python3

def demonstrate_lsb():
    """Demonstrate LSB modification concept"""
    
    # Original pixel value
    original_pixel = 170  # Binary: 10101010
    print(f"Original pixel: {original_pixel} = {format(original_pixel, '08b')}")
    
    # Message bit to hide
    message_bit = 1
    print(f"Message bit to hide: {message_bit}")
    
    # Modify LSB: Clear LSB and set to message bit
    modified_pixel = (original_pixel & 0xFE) | message_bit
    print(f"Modified pixel: {modified_pixel} = {format(modified_pixel, '08b')}")
    print(f"Difference: {abs(original_pixel - modified_pixel)} (imperceptible!)")
    
    # Extract the hidden bit
    extracted_bit = modified_pixel & 1
    print(f"Extracted bit: {extracted_bit}")
    print(f"Match: {extracted_bit == message_bit}")

if __name__ == "__main__":
    demonstrate_lsb()
