from locust import FastHttpUser, task, between
from utils.api import Api
from utils.helpers import Helpers


class JsonPlaceHolder(FastHttpUser):
    wait_time = between(2, 10)

    def on_start(self):
        self.api = Api(self.client)
        self.helpers = Helpers()

    @task(1)
    def getPosts(self):
        self.api.getPosts()

    @task(1)
    def getComments(self):
        self.api.getComments()

    @task(2)
    def postPosts(self):
        data = self.helpers.generatePostData()
        self.api.postPosts(data)

    @task(2)
    def postComments(self):
        data = self.helpers.generateCommentData()
        self.api.postComments(data)

    @task(1)
    def putPosts(self):
        id = self.helpers.getRandomId()
        data = self.helpers.generatePostData()
        self.api.putPosts(id, data)

    @task(1)
    def putComments(self):
        id = self.helpers.getRandomId()
        data = self.helpers.generateCommentData()
        self.api.putComments(id, data)

    @task(1)
    def patchPosts(self):
        id = self.helpers.getRandomId()
        data = self.helpers.generatePatchPostData()
        self.api.patchPosts(id, data)

    @task(1)
    def patchComments(self):
        id = self.helpers.getRandomId()
        data = self.helpers.generatePatchCommentData()
        self.api.patchComments(id, data)

    @task(1)
    def deletePosts(self):
        id = self.helpers.getRandomId()
        self.api.deletePosts(id)

    @task(1)
    def deleteComments(self):
        id = self.helpers.getRandomId()
        self.api.deleteComments(id)
