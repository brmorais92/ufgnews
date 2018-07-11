import models.article.data, models.article.sqlite_dao
import traceback


class ArticleServices():
    def __init__(self, request):
        self.request = request

    async def fetch_articles(self, search_string=''):
        article_list = await models.article.sqlite_dao.search_articles(self.request, search_string)
        return article_list

    async def fetch_article(self, id):
        article = await models.article.sqlite_dao.fetch_article(self.request, id)
        return article

    async def create_article(self, article):
        try:
            await models.article.sqlite_dao.create_article(self.request, article)
            return True
        except:
            print(traceback.format_exc())
            return False

    async def remove_article(self, article):
        try:
            await models.article.sqlite_dao.remove_article(self.request, article)
            return True
        except:
            print(traceback.format_exc())
            return False

    async def update_article(self, article):
        try:
            await models.article.sqlite_dao.update_article(self.request, article)
            return True
        except:
            print(traceback.format_exc())
            return False