import os
import argparse
import requests

def list_files(directory):
    """List all JSON files in the specified directory."""
    json_files = [file for file in os.listdir(directory) if file.endswith('.json')]
    return json_files

def select_file(files):
    """Display a menu-like system to select a file from the list."""
    print("Select a JSON file to send:")
    for idx, file in enumerate(files, start=1):
        print(f"{idx}. {file}")
    
    while True:
        choice = input("Enter the number of the file you want to send: ")
        if choice.isdigit() and 1 <= int(choice) <= len(files):
            selected_file = files[int(choice) - 1]
            return selected_file
        else:
            print("Invalid choice. Please enter a valid number.")

def send_data(file_path, url, method):
    """Send the JSON data in the selected file via a POST or GET request."""
    with open(file_path, 'r') as file:
        json_data = file.read()

    if method.upper() == 'POST':
        response = requests.post(url, json=json_data)
    elif method.upper() == 'GET':
        response = requests.get(url, json=json_data)
    else:
        print("Invalid HTTP method. Please specify 'GET' or 'POST'.")
        return

    print(f"Response from {method} request:")
    print(response.text)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send JSON data from a file via HTTP request.")
    # parser.add_argument("directory", help="Directory containing JSON files")
    parser.add_argument("url", help="URL of the API endpoint")
    parser.add_argument("method", help="HTTP method (GET or POST)")
    args = parser.parse_args()

    directory = './tests'
    # List JSON files in the specified directory
    json_files = list_files(directory)

    if not json_files:
        print("No JSON files found in the directory.")
    else:
        # Display menu-like system to select a file
        selected_file = select_file(json_files)
        
        # Send selected file data via HTTP request
        file_path = os.path.join(args.directory, selected_file)
        send_data(file_path, args.url, args.method)
