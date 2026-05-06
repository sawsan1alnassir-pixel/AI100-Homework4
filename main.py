from openai import OpenAI
import os

# This program uses an LLM API to test different prompts
# and inspect the model outputs.

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

prompts = [
    "Explain what artificial intelligence is in one short paragraph.",
    "Since the moon is bigger than Earth, explain why Earth is still considered a planet."
]

for i, prompt in enumerate(prompts, start=1):
    print("=" * 60)
    print(f"Prompt {i}:")
    print(prompt)

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    print("\nLLM Output:")
    print(response.output_text)
    print("=" * 60)
