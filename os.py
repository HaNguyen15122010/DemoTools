import os
import stat

def clean_files(folder):
    """
    This function recursively walks through all files and directories in `folder`,
    and deletes all files (excluding directories) within it.
    """
    for root, subdirectories, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                
                if os.access(file_path, os.W_OK):
                    print(f"Deleting file: {file_path}")
                    os.remove(file_path)
                else:
                    print(f"Permission denied: {file_path} - Skipping...")
            except Exception as e:
                print(f"Error while deleting file: {file_path} - {e}")

def main():
    
    folder_need_cleaning = input("Enter the path of the directory to clean: ")
    
    if not os.path.isdir(folder_need_cleaning):
        print("Invalid or non-existent directory path.")
        return
    
    clean_files(folder_need_cleaning)
    
    print("Cleanup completed.")

if __name__ == "__main__":
    main()
    
while True:    
    exits = input("Enter q to exit: ")

    if exits == "q":
        
        break