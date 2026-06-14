class SimpleModel:

    def __init__(self, knowledge):
        self.knowledge = knowledge

    def answer(self, question):

        q = question.lower()

        for line in self.knowledge.split("\n"):

            if q in line.lower():
                return line

        return "I could not find relevant information."