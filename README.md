# AI 100 Homework 4: Using Code to Interact with an LLM API

## Project Description
This project uses Python code to interact with an LLM API.  
The goal is to test a couple of different inputs and inspect the model outputs.

## Prompts Tested

### Prompt 1
Explain what artificial intelligence is in one short paragraph.

### Prompt 2
Since the moon is bigger than Earth, explain why Earth is still considered a planet.

## What I Observed
The first prompt produced a normal explanation of artificial intelligence.

The second prompt included a false assumption because the moon is not bigger than Earth. I wanted to see whether the model would correct the false information or continue answering based on the incorrect prompt.

## Files
- main.py: Python code that sends prompts to the LLM API and prints the outputs.

## How to Run
1. Install the OpenAI Python package:
   ```bash
   pip install openai
