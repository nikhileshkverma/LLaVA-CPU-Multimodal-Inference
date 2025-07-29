# 🧠 LLaVA CPU Multimodal Inference (Text + Image) - Online & Offline

This project demonstrates how to run **LLaVA (Large Language and Vision Assistant)** models on **CPU** using [Ollama](https://ollama.com), both in **online** and **offline** environments.

Supports:

* ✅ Text-only queries
* 🖼️ Image + text (multimodal) queries
* 📴 Fully offline mode
* ⚙️ CPU inference (low-resource)

---

## 📦 Requirements

### 🔧 System Requirements (Minimum)

| Resource   | Requirement                       |
| ---------- | --------------------------------- |
| OS         | Ubuntu / macOS / WSL2             |
| CPU        | 4 cores minimum (8+ recommended)  |
| RAM        | 16 GB minimum (32 GB recommended) |
| Disk Space | 10–12 GB free space               |
| Python     | 3.10+                             |
| Internet   | Only required for model download  |

---

## 🗂️ Dependencies

Install these packages (Python + system tools):

```bash
# System dependencies (Debian-based)
sudo apt update && sudo apt install -y git curl python3-pip

# Python packages
pip install ollama pillow pydantic
```

---

## 🚀 Setup (Online Mode)

### 1. Install Ollama

Install Ollama (CPU mode is fine):

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Verify it's working:

```bash
ollama --version
```

---

### 2. Pull the LLaVA model

LLaVA is a multimodal model (image + text):

```bash
ollama pull llava
```

> This will download \~4–5 GB of model files.

---

### 3. Clone this repo

```bash
git clone https://github.com/yourusername/llava-cpu-demo.git
cd llava-cpu-demo
```

---

### 4. Run the script (online)

```bash
python3 offline_check_llama.py
```

Example output:

```bash
What would you like to do?
1. Text-only query
2. Image + text query
3. Exit
> 1
Enter your text question:
> What is the capital of India?

Response:
The capital of India is New Delhi.
```

---

## 📴 Offline Mode

Once the model is downloaded (`ollama pull llava`), you can **go offline** and continue using the script.

### Offline safety tip:

```bash
# Disconnect from internet
nmcli networking off  # or disable WiFi manually
```

Run:

```bash
python3 offline_check_llama.py
```

You will see a message:

> ⚠️ You are currently connected to the internet. This tool is designed to run completely offline.

Ignore it if you're intentionally offline.

---

## 📁 `offline_check_llama.py` – Main Script

Here's the **full script** for your project:

```python
import ollama
from PIL import Image
import base64
import sys
import os

def encode_image_to_base64(path):
    with open(path, 'rb') as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

def text_query():
    question = input("Enter your text question:\n> ")
    response = ollama.chat(model='llava', messages=[
        {"role": "user", "content": question}
    ])
    print("\nResponse:\n ", response['message']['content'])

def image_query():
    image_path = input("Enter the relative path to your image (e.g. ./image.jpg):\n> ")
    question = input("Enter your text question about the image:\n> ")
    
    try:
        image_base64 = encode_image_to_base64(image_path)
        response = ollama.chat(
            model='llava',
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "image", "image": image_base64},
                        {"type": "text", "text": question}
                    ]
                }
            ]
        )
        print("\nResponse:\n ", response['message']['content'])
    except Exception as e:
        print(f"\n❌ Error: {e}")

def main():
    print("⚠️  Warning: You are currently connected to the internet.")
    print("This tool is designed to run completely offline.")
    print("You may disconnect your internet for full privacy.\n")

    while True:
        print("\nWhat would you like to do?")
        print("1. Text-only query")
        print("2. Image + text query")
        print("3. Exit")
        choice = input("> ")
        
        if choice == '1':
            text_query()
        elif choice == '2':
            image_query()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
```

---

## 🧪 Example Usage

### 📸 Image + Text Query

1. Save an image named `bee.jpg` in your project folder.
2. Run the script and choose **Option 2**
3. Ask a question like:

```text
> Describe the image
```

---

## 🧵 Model Details

| Name  | Model      | Size        | Tasks                     |
| ----- | ---------- | ----------- | ------------------------- |
| LLaVA | `llava:7b` | \~4 GB (Q4) | Multimodal (image + text) |

Model page: [https://ollama.com/library/llava](https://ollama.com/library/llava)
GGUF support via `llama.cpp`.

---

## ❓ FAQ

### Can this run without internet?

✅ Yes, after model is downloaded via `ollama pull`.

### Does it need a GPU?

❌ No. This is optimized for **CPU-only inference** via Ollama.

### How long does it take?

* Text-only: \~3–4 sec
* Image + text: \~8–15 sec

---

## 🔧 Troubleshooting

### 🔹 `model not found` error?

```bash
ollama pull llava
```

### 🔹 Pydantic validation error?

Ensure `messages` list is properly formatted as:

```python
{
  "role": "user",
  "content": [
    {"type": "image", "image": "<base64>"},
    {"type": "text", "text": "Your question"}
  ]
}
```

### 🔹 Wrong Python version?

Check with:

```bash
python3 --version  # should be 3.10+
```

---

## 📜 License

This project is open-source under the **MIT License**.

---
## 📚 References

Improved Baselines with Visual Instruction Tuning
https://arxiv.org/pdf/2310.03744

Visual Instruction Tuning
https://arxiv.org/pdf/2304.08485

llama.cpp – A port of Facebook’s LLaMA model in C/C++
https://github.com/ggml‑org/llama.cpp



