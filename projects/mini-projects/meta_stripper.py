from PIL import Image
import os
import sys

def strip_metadata(image_path):
    try:
        img = Image.open(image_path)
        data = list(img.getdata())
        image_without_exif = Image.new(img.mode, img.size)
        image_without_exif.putdata(data)
        
        output_path = "stripped_" + os.path.basename(image_path)
        image_without_exif.save(output_path)
        print(f"Metadata stripped. Saved as: {output_path}")
    except Exception as e:
        print(f"Error processing {image_path}: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for path in sys.argv[1:]:
            strip_metadata(path)
    else:
        print("Usage: python meta_stripper.py <image1.jpg> <image2.png> ...")
        print("Note: Requires Pillow (pip install Pillow)")
