import os
from PIL import Image


def optimize_images():
    # Settings
    input_folder = "images"
    output_folder = "images/optimized"
    target_width = 800

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Created folder: {output_folder}")

    # Loop through all files in the images folder
    files = [f for f in os.listdir(
        input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    print(f"Found {len(files)} images to process...")

    for filename in files:
        file_path = os.path.join(input_folder, filename)

        with Image.open(file_path) as img:
            # 1. Calculate new height to maintain aspect ratio (No cropping)
            aspect_ratio = img.height / img.width
            new_height = int(target_width * aspect_ratio)

            # 2. Resize the image
            print(
                f"Resizing {filename} from {img.size} to ({target_width}, {new_height})...")
            img_resized = img.resize(
                (target_width, new_height), Image.Resampling.LANCZOS)

            # 3. Create new filename (change extension to .webp)
            name_only = os.path.splitext(filename)[0]
            new_filename = f"{name_only}.webp"
            save_path = os.path.join(output_folder, new_filename)

            # 4. Save as WebP (Quality 85 is the sweet spot for web)
            img_resized.save(save_path, 'WEBP', quality=80)

            # Calculate savings
            original_size = os.path.getsize(file_path) / 1024  # KB
            new_size = os.path.getsize(save_path) / 1024  # KB
            print(
                f"✅ Saved to {save_path} | Size: {new_size:.1f}KB (was {original_size:.1f}KB)")


if __name__ == "__main__":
    optimize_images()
