import random
from faker import Faker

fake = Faker()


class Helpers:
    def __init__(self, minId=1, maxId=50):
        self.minId = minId
        self.maxId = maxId

    def getRandomId(self):
        return random.randint(self.minId, self.maxId)

    def generatePostData(self):
        return {
            "title": f"Updated Title {random.randint(1, 1000)}",
            "body": fake.paragraph(nb_sentences=3),
        }

    def generateCommentData(self):
        return {"title": fake.name(), "body": fake.sentence(nb_words=10)}

    def generatePatchPostData(self):
        return {"title": f"Partially Updated Title {random.randint(1, 1000)}"}

    def generatePatchCommentData(self):
        return {"body": "Partially Updated Comment"}
