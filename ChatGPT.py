import openai

openai.api_key = "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"


MODEL = "gpt-3.5-turbo"
requests = [{"role": "system", "content": "You are a helpful assistant who provides answers within 50 words"}]

def get_response(request):
    global MODEL
    global requests
    requests.append({"role": "user", "content": request})
    chat = openai.ChatCompletion.create(
        model = MODEL,
        messages = requests
    )
    reply = chat.choices[0].message.content
    return reply
