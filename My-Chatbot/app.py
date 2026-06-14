import sys

sys.path.append("src")

from generate import get_response


def main():

    print("Simple AI Chatbot")
    print("Type 'exit' to quit.\n")

    while True:

        user = input("You: ")

        if user.lower() == "exit":
            break

        reply = get_response(user)

        print("Bot:", reply)
        print()


if __name__ == "__main__":
    main()