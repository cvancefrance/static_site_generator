import os
import shutil


def clean_directory(path):
# Check if "public" directory exists
    if os.path.exists(path):
    # Remove it and everything inside
        shutil.rmtree(path)

def copy_directory(source, destination):
    # List everything in the source directory
    files_and_dirs = os.listdir(source)
    for item in files_and_dirs:
        # Create the full paths for source and destination
        source_item = os.path.join(source, item)
        destination_item = os.path.join(destination, item)

        print(f"Copying {source_item} to {destination_item}")

        # Check if the item is a file
        if os.path.isfile(source_item):
            # Copy the file to the destination
            shutil.copy(source_item, destination_item)
        else:
            # If it's a directory, create it in destination and call recursively
            os.mkdir(destination_item)
            copy_directory(source_item, destination_item)



def main():
    clean_directory("public")
    if not os.path.exists("public"):
        os.mkdir("public")
    copy_directory("static", "public")

if __name__ == "__main__":
    main()
