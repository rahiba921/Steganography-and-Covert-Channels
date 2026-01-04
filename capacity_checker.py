#!/usr/bin/env python3

from PIL import Image
import sys

def calculate_capacity(image_path):
    """
    Calculate maximum message capacity of an image.
    
    Args:
        image_path: Path to image file
    
    Returns:
        Maximum characters that can be hidden
    """
    # TODO: Open image and get dimensions
    # TODO: Calculate total bits available (width * height * 3)
    # TODO: Account for delimiter overhead
    # TODO: Convert bits to character capacity
    # TODO: Display results
    pass

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 capacity_checker.py <image_path>")
    else:
        calculate_capacity(sys.argv[1])
