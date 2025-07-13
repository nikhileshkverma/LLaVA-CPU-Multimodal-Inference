import ollama

response = ollama.chat(
    model="llama3.2-vision",
    messages=[
        {
            "role": "user",
            "content": "Describe this image.",
            "images": ["./bee.jpg"]
        }
    ]
)

print(response['message']['content'])
