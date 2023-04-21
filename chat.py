import openai

openai.api_key = "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"


completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "user", "content": "When was the last football worldcup held?"},
        # {"role": "user", "content": "What is the national sport of England?"},
        # {"role": "user", "content": "What is CHATGPT?"},

    ]
)


# print(completion)

response = completion["choices"][0]["message"]['content']

print(response)

