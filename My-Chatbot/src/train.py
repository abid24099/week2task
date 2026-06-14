DATA_FILE = "data/scraped_data.txt"


def load_training_data():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return f.read()


if __name__ == "__main__":
    text = load_training_data()

    print("Characters:", len(text))
    print()
    print(text[:500])