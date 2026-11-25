import os

JOKE = "My fridge light has seen me at my worst so often, it should be my emergency contact."
MAX_CHARS = 140  # the gate accepts 1..140 characters


def entry_text():
    text = JOKE.strip()
    assert 1 <= len(text) <= MAX_CHARS, "entry must fit the gate"
    return text


def main():
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
    except OSError:
        path = "entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(entry_text())


if __name__ == "__main__":
    main()
