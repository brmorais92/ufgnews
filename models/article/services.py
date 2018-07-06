import models.article.data, models.article.sqlite_dao

class ArticleServices():
    def __init__(self, request):
        self.article_list = []
        self.request = request
    async def search_articles(self, search_string):
        print(await models.article.sqlite_dao.search_articles(self.request, search_string))