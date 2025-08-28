def greet(name: str) -> str:
    return f"Hello, {name}! Welcome to CI/CD with Agile DevOps."


if __name__ == "__main__":
    # This runs only when you call: py src/app.py
    print(greet("LeBonCyl"))
