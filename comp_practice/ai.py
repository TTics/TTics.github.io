from openai import OpenAI

client = OpenAI(
  api_key="2dffd8c0-d924-48f3-bd83-3d67520a2f40"
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "write a haiku about ai"},
  ]
)

print(completion.choices[0].message);
