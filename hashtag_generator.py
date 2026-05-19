from groq import Groq
import os
import time

# Create Groq client using API key from environment variable
client = Groq(api_key=os.environ["GROQ_API_KEY"])

# Take user input
topic = input("What is the image/post about? ").strip()

# Send request to AI model
r = client.chat.completions.create(
    model="llama-3.1-8b-instant",

    messages=[
        {
            "role": "system",
            "content": (
                """
                You need to write hashtags based on Input.
                Always include relevant hashtags at the end.
                Example:
                #photography #travel

                Return only hashtags.
                No explanations.
                No labels.
                No extra text.
                """
            ),
        },
        {
            "role": "user",
            "content": topic,
        },
    ],

    # Maximum number of tokens AI can generate
    max_tokens=256,

    # Controls creativity
    # Lower = more predictable
    # Higher = more creative/random
    temperature=0.7,

    # Controls diversity of word selection
    # 0.9 means AI chooses from top 90% probable words
    top_p=0.9,

    # Reduces repeating same words/hashtags too much
    frequency_penalty=0.5,

    # Encourages AI to introduce new words/topics
    presence_penalty=0.8,

    # False = complete response at once
    # True = response comes chunk-by-chunk (streaming)
    stream=False,
)

# Direct output (recommended when stream=False)
full_response = r.choices[0].message.content.strip()

# Typing effect
print()

for char in full_response:
    print(char, end="", flush=True)
    time.sleep(0.02)

print()