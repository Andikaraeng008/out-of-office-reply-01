import os

TEXT = "I am currently on vacation and have set my out-of-office reply to reply to itself. We are in talks."

def main():
    assert 1 <= len(TEXT) <= 160, "entry must be 1-160 characters"
    assert TEXT == TEXT.strip(), "entry must not start or end with whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
