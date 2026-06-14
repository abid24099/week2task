from model import SimpleModel
from train import load_training_data


def get_response(question):

    data = load_training_data()

    chatbot = SimpleModel(data)

    return chatbot.answer(question)