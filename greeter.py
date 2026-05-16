# greeter.py — Python warm-up

GREETING = "Hello, {name}! Welcome to your coding tutor project."

TOPICS = ["variables", "functions", "lists", "dicts", "loops"]

DIFFICULTY = {
    "variables": "easy",
    "functions": "easy",
    "lists": "easy",
    "dicts": "medium",
    "loops": "medium",
}


def greet(name):
    """Return a personalized greeting string."""
    return GREETING.format(name=name)


def show_topics(topics, difficulty):
    """Print each topic on its own numbered line, with difficulty."""
    print("\nWe'll cover these basics:")
    for i, topic in enumerate(topics, start=1):
        level = difficulty.get(topic, "unknown")
        print(f"  {i}. {topic} ({level})")


if __name__ == "__main__":
    name = input("What's your name? ")
    print(greet(name))
    show_topics(TOPICS, DIFFICULTY)