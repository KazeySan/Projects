#Ensure that pip is installed and available
#Ensure that pandas is installed and available through command line: pip install pandas in command prompt
import os
import pandas as pd
import requests

file = "your_file_name.xlsx" # Replace with your actual file name

Example = pd.read_excel(file, sheet_name="Sheet1") # Replace with your actual sheet name
sample = Example.head(50) #Number of rows to send to the LLM

#Write the prompt for the LLM
prompt = """Your_prompt

1. Step 1
2. Step 2

Use this format:
This is correct because: [your format]
"""

for _, row in sample.iterrows():
    prompt += f"\nID: {row['Column1.id']}\nStudent belief: {row['Column1.studentBelief']}\n"

API_KEY = "Your_API_Key_Here"  # Replace with your actual API key
BASE_URL = "Your_BASE_URL_Here" # Replace with the actual base URL of the API

def make_basic_call(prompt_text):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "X-Title": "Your Title Here",  # Replace with your actual title
        "Content-Type": "application/json"
    }

    payload = {
        "model": "insert-model-name-here",  # Replace with the actual LLM model name
        "messages": [
            {
                "role": "user",
                "content": prompt_text
            }
        ],
        "temperature": 0.7,
        "max_tokens": 20000 #Can change this value based on your needs
    }

    print("\nSending all rows to the LLM... Please wait.")

    response = requests.post(
        f"{BASE_URL}/chat/completions",
        headers=headers,
        json=payload
    )

    print("API responded!")

    if response.status_code == 200:
        result = response.json()

        print("\n=== RESPONSE FROM LLM ===")
        print(result["choices"][0]["message"]["content"])
        print("==========================\n")

    else:
        print(f"\nServer Error Code: {response.status_code}")
        print(f"Server Message: {response.text}")

make_basic_call(prompt)

input("\nPress Enter to close...")