import telegram
import asyncio
from openai import OpenAI

def ChatGPT():  
  client = OpenAI(
    api_key="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"
  )
  completion = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    messages=[
      {"role": "system", "content": "사람 이름을 말하면 그사람의 명언을 알려줘."},
      {"role": "user", "content": " 이순신 장군."}
    ],
  )
  print(completion.choices[0].message.content)
  return completion.choices[0].message.content

def TelegramSend(str):
  token = "6833983891:AAGQNZuPAmYgRU4beRzTq-mE2hoMKvG13io"
  public_chat_name = '@OpenSw_2_chatbot'
  chat_id = 6475305403
  bot = telegram.Bot(token = token)
  asyncio.run(bot.sendMessage(chat_id=public_chat_name, text=str))
  # asyncio.run(bot.sendMessage(chat_id=chat_id, text=completion.choices[0].message.content))

str = ChatGPT()
TelegramSend(str)