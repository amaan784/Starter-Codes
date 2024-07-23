import os
from dotenv import load_dotenv

def main():
    load_dotenv()  # Load environment variables from .env file
    file_path = os.environ.get("FILE_PATH")
    
    print(file_path)

if __name__ == '__main__':
    main()  # Call the main function
