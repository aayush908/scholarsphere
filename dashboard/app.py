import requests

user_input = "what is python"
# Replace "YOUR_API_KEY" with your actual ChatGPT API key
api_key = "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"
api_url = "https://api.openai.com/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
}

data = {
    "model": "text-davinci-002",  # Replace with the desired language model
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_input},
    ]
}

response = requests.post(api_url, json=data, headers=headers)
print(response.status_code)
print(response.json())  # Print the full JSON response

if response.status_code == 200:
    chatgpt_response = response.json()["choices"][0]["message"]["content"]
else:
    chatgpt_response = "Error fetching response from ChatGPT API"

context = {"user_input": user_input, "chatgpt_response": chatgpt_response}
print(context)
