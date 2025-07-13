import ollama
import os

def text_only():
    query = input("Enter your text question:\n> ")
    response = ollama.chat(
        model="llama3.2-vision",
        messages=[{"role": "user", "content": query}]
    )
    print("\nResponse:")
    print(response["message"]["content"])

def image_and_text():
    image_path = input("Enter the relative path to your image (e.g. ./bee.jpg):\n> ")
    if not os.path.isfile(image_path):
        print(f"Error: File '{image_path}' does not exist.")
        return
    query = input("Enter your text question about the image:\n> ")
    response = ollama.chat(
        model="llama3.2-vision",
        messages=[{"role": "user", "content": query, "images": [image_path]}]
    )
    print("\nResponse:")
    print(response["message"]["content"])

def main():
    while True:
        print("\nWhat would you like to do?")
        print("1. Text-only query")
        print("2. Image + text query")
        print("3. Exit")
        choice = input("> ").strip()

        if choice == "1":
            text_only()
        elif choice == "2":
            image_and_text()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
