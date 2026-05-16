"""chat.py — terminal chat loop with conversation memory."""

import os
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic()

SYSTEM_PROMPT = """You are a patient coding tutor for someone learning Python.

Your style:
- Ask Socratic questions instead of giving direct answers when the learner is
  exploring a concept they could figure out themselves.
- When the learner is truly stuck, give a small hint first, then a bigger hint,
  only then the answer.
- Keep responses short — 3-5 sentences unless explicitly asked for more.
- Use concrete, runnable code examples when explaining concepts.
- Encourage curiosity. Celebrate progress, no matter how small.
"""

EXIT_WORDS = {"quit", "exit", "bye", "q"}


def chat():
    """Run an interactive chat loop with Claude."""
    print("Coding Tutor — type 'quit' to exit, or hit Ctrl+C.\n")

    # The conversation history. Grows turn by turn.
    messages = []

    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not user_input:
            continue
        if user_input.lower() in EXIT_WORDS:
            print("Goodbye!")
            break

        # 1. Add user's turn to history.
        messages.append({"role": "user", "content": user_input})

        # 2. Send the WHOLE conversation. The `system` prompt is separate.
        response = client.messages.create(
            model="claude-haiku-4-5",
            max_tokens=500,
            system=SYSTEM_PROMPT,
            messages=messages,
        )

        # 3. Pull out Claude's reply text.
        reply = response.content[0].text

        # 4. Add Claude's turn to history so the next call has context.
        messages.append({"role": "assistant", "content": reply})

        print(f"\nTutor: {reply}\n")


if __name__ == "__main__":
    chat()