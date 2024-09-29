class Api:
    def __init__(self, client):
        self.client = client

    def getPosts(self):
        with self.client.get("/posts", catch_response=True) as response:
            if response.status_code != 200:
                response.failure(f"Failed to get posts: {response.text}")
            else:
                response.success()

    def getComments(self):
        with self.client.get("/comments", catch_response=True) as response:
            if response.status_code != 200:
                response.failure(f"Failed to get comments: {response.text}")
            else:
                response.success()

    def postPosts(self, data):
        with self.client.post("/posts", json=data, catch_response=True) as response:
            if response.status_code != 201:
                response.failure(f"Failed to create post: {response.text}")
            else:
                response.success()

    def postComments(self, data):
        with self.client.post("/comments", json=data, catch_response=True) as response:
            if response.status_code != 201:
                response.failure(f"Failed to create comment: {response.text}")
            else:
                response.success()

    def putPosts(self, id, data):
        with self.client.put(
            f"/posts/{id}", json=data, name="/posts", catch_response=True
        ) as response:
            if response.status_code != 200:
                response.failure(f"Failed to update post {id}: {response.text}")
            else:
                response.success()

    def putComments(self, id, data):
        with self.client.put(
            f"/comments/{id}", json=data, name="/comments", catch_response=True
        ) as response:
            if response.status_code != 200:
                response.failure(f"Failed to update comment {id}: {response.text}")
            else:
                response.success()

    def patchPosts(self, id, data):
        with self.client.patch(
            f"/posts/{id}", json=data, name="/posts", catch_response=True
        ) as response:
            if response.status_code != 200:
                response.failure(
                    f"Failed to partially update post {id}: {response.text}"
                )
            else:
                response.success()

    def patchComments(self, id, data):
        with self.client.patch(
            f"/comments/{id}", json=data, name="/comments", catch_response=True
        ) as response:
            if response.status_code != 200:
                response.failure(
                    f"Failed to partially update comment {id}: {response.text}"
                )
            else:
                response.success()

    def deletePosts(self, id):
        with self.client.delete(
            f"/posts/{id}", name="/posts", catch_response=True
        ) as response:
            if response.status_code not in [200, 204]:
                response.failure(f"Failed to delete post {id}: {response.text}")
            else:
                response.success()

    def deleteComments(self, id):
        with self.client.delete(
            f"/comments/{id}", name="/comments", catch_response=True
        ) as response:
            if response.status_code not in [200, 204]:
                response.failure(f"Failed to delete comment {id}: {response.text}")
            else:
                response.success()
