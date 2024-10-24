import os

# Define the path
main_path = r"E:\AMINE2\COURS FAC\LEARNING\Python\games\flappy\AI FLAPPY BIRD"
imgs_path = os.path.join(main_path, "imgs")

# Check if the main directory exists
if os.path.exists(main_path):
    print(f"Main directory '{main_path}' exists.")
    # List contents of the main directory
    print(f"Contents of '{main_path}':")
    for item in os.listdir(main_path):
        print(item)
else:
    print(f"Main directory '{main_path}' does not exist.")

# Check if the 'imgs' folder exists
if os.path.exists(imgs_path):
    print(f"Imgs directory '{imgs_path}' exists.")
    # List contents of the 'imgs' folder
    print(f"Contents of '{imgs_path}':")
    for item in os.listdir(imgs_path):
        print(item)
else:
    print(f"Imgs directory '{imgs_path}' does not exist.")
