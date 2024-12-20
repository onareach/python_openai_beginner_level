import argparse
import os
import tomllib
from pathlib import Path

from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "developer", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about surfing."
        }
    ]
)

print(completion.choices[0].message)

# Alternate content: "Say something about surfing."