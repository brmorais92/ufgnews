class Article:
    def __init__(self, id=None, author_id=None, title=None, body=None,
                 submitted_timestamp=None, updated_timestamp=None):
        self.id = id
        self.author_id = author_id
        self.title = title
        self.body = body
        self.submitted_timestamp = submitted_timestamp
        self.updated_timestamp = updated_timestamp
