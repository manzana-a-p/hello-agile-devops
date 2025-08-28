def greet(name: str) -> str:
    return f"Hello, {name}! Welcome to CI/CD with Agile DevOps."


if __name__ == "__main__":
    # This block runs only when you execute: py src/app.py
    print("DEBUG: app.py is running...")
    print(greet("LeBonCyl"))
