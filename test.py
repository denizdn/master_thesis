from openai import OpenAI
client = OpenAI()
completion = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages = [{"role": "system", "content": "you are a helpful asisstant"},
                {"role": "user", "content": "describe us history"}]
)