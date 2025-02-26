import requests

# Define the server's API URL for completions
API_URL = "http://localhost:1234/v1/chat/completions"

def read_file_content(file_path):
    try:
        with open(file_path, "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

# Function to create a chat completion with user input and system message
def create_chat_completion(user_input):
    headers = {"Content-Type": "application/json"}
    data = {
        "model": "local-model",  # Model name (change this if needed)
        "messages": [
            {"role": "system", "content": read_file_content("kusta.txt")},
            {"role": "user", "content": user_input}
        ],
        "temperature": 1,
    }
    
    # Send a POST request to the server
    response = requests.post(API_URL, json=data, headers=headers)
    
    if response.status_code == 200:
        # Assuming the content is in the 'choices' array in the response
        return response.json()["choices"][0]["message"]["content"]
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

# Main function to run the interactive assistant
def main():
    while True:
        user_input = input("You: ")
        completion = create_chat_completion(user_input)
        if completion:
            print("Kusta Pistachio: " + completion)

if __name__ == "__main__":
    main()
