import re


def tokenize(text):
    text = text.lower()
    tokens = re.findall(r"\b[a-zA-Z]+\b", text)
    return tokens


if __name__ == "__main__":
    sample = "Artificial Intelligence is changing the world!"
    print(tokenize(sample))