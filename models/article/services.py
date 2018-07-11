import models.article.data, models.article.sqlite_dao
import traceback


class ArticleServices():
    def __init__(self, request):
        self.request = request

    async def fetch_articles(self, search_string=''):
        article_list = await models.article.sqlite_dao.search_articles(self.request, search_string)
        return article_list

    async def create_article(self, request, article):
        try:
            await models.article.sqlite_dao.create_article(request, article)
            return True
        except:
            print(traceback.format_exc())
            return False

    async def remove_article(self, request, article):
        try:
            await models.article.sqlite_dao.remove_article(request, article)
            return True
        except:
            print(traceback.format_exc())
            return False