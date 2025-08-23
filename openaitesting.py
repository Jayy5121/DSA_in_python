from openai import OpenAI
client = OpenAI(id)

response = client.responses.create(
  prompt={
    "id": "pmpt_68754d63d9b88197a46bc128235c7d6b05a0727711eef7c2",
    "version": "1"
  }
)