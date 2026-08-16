import os

# ====== CHECK DEPENDENCIES ======
try:
    import requests
except ImportError:
    os.system("pip install requests")
    import requests

def key(k):
    global API_KEY
    API_KEY = k

messages = []

def answer(text, memory=False):
    global API_KEY
    BASE_URL = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    try:
        if memory:
            messages.append({"role": "user", "content": text})
            data = {
                "model": "openai/gpt-3.5-turbo",
                "messages": messages
            }
        else:
            data = {
                "model": "openai/gpt-3.5-turbo",
                "messages": [{"role": "user", "content": text}]  # ✅
            }

        response = requests.post(BASE_URL, headers=headers, json=data)
        result = response.json()

        reply = result['choices'][0]['message']['content']
        messages.append({"role": "assistant", "content": reply})
        return reply

    except KeyError:
        print("❌ Unexpected API response:", result)
        return "Error: invalid response from API"

    except Exception as e:
        print("❌ Request failed:", e)
        return "Error: check your internet or API key"

