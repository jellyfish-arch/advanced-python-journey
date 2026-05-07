from PIL import Image, ImageFilter
import os

def process_image():
    """
    Demonstrates basic image manipulation with Pillow.
    Creates a dummy image if none exists.
    """
    filename = "dummy_image.png"
    
    # Create a small dummy image if it doesn't exist
    if not os.path.exists(filename):
        img = Image.new('RGB', (200, 200), color='cyan')
        img.save(filename)
        print(f"Created {filename}")
    
    # Open and process
    with Image.open(filename) as img:
        print(f"Format: {img.format}, Size: {img.size}, Mode: {img.mode}")
        
        # 1. Resize
        resized = img.resize((100, 100))
        
        # 2. Filter (Blur)
        blurred = img.filter(ImageFilter.BLUR)
        
        # 3. Rotate
        rotated = img.rotate(45)
        
        # Save results
        rotated.save("processed_image.png")
        print("Processed and saved to processed_image.png")

if __name__ == "__main__":
    process_image()
