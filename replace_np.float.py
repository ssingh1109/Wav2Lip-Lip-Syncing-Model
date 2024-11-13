import os

# Define the base path to your project
base_path = r"D:\wav2lip-HD-main\Wav2Lip-GFPGAN"

# Recursively search for .py files and replace deprecated float
for root, dirs, files in os.walk(base_path):
    for file in files:
        if file.endswith(".py"):
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as f:
                content = f.read()

            # Replace deprecated float with the appropriate dtype
            updated_content = content.replace('float', 'float')

            with open(file_path, 'w') as f:
                f.write(updated_content)

print("Replacement complete.")
