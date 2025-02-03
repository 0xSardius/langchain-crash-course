# Chat Model Documents: https://python.langchain.com/v0.2/docs/integrations/chat/
# OpenAI Chat Model Documents: https://python.langchain.com/v0.2/docs/integrations/chat/openai/

from dotenv import load_dotenv
import os
from langchain_anthropic import ChatAnthropic

# Load environment variables from .env
load_dotenv(override=True)
# Create a ChatOpenAI model
model = ChatAnthropic(model="claude-3-5-sonnet-20240620")


# Invoke the model with a message
result = model.invoke("What are the 64 hexagrams of the I Ching?")
print("Full result:")
print(result)
print("Content only:")
print(result.content)
