from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_anthropic import ChatAnthropic

# Load environment variables from .env
load_dotenv(override=True)

# Create ChatAnthropic model
model = ChatAnthropic(model="claude-3-sonnet-20240229")

# Start conversation about astrology
messages = [
    SystemMessage(
        content="You are an expert astrologer teaching about houses and planetary rulers. "
        "Explain concepts clearly and provide specific examples when relevant."
    ),
    HumanMessage(
        content="What is the first house in astrology and what planet rules it?"
    ),
]

# Get first response
result = model.invoke(messages)
print("\nFirst Response:")
print(f"AI: {result.content}\n")

# Continue conversation
messages.extend([
    AIMessage(content=result.content),
    HumanMessage(
        content="How does Mars's influence manifest differently when ruling the first house versus the eighth house?"
    ),
])

# Get second response
result = model.invoke(messages)
print("\nSecond Response:")
print(f"AI: {result.content}\n")

# Add final question about house rulership
messages.extend([
    AIMessage(content=result.content),
    HumanMessage(
        content="Can you explain the concept of planetary dignity in house rulership?"
    ),
])

# Get final response
result = model.invoke(messages)
print("\nFinal Response:")
print(f"AI: {result.content}\n")
