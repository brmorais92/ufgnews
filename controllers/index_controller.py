import aiohttp_jinja2
import aiohttp

from aiohttp_session import get_session
import controllers.controller
import models.article.sqlite_dao, models.article.data, models.article.services


class IndexController(controllers.controller.Controller):
    routes = aiohttp.web.RouteTableDef()

    @routes.get('/')
    @aiohttp_jinja2.template('index.html')
    async def handle(request):
        article_services = models.article.services.ArticleServices(request)
        article_list = await article_services.fetch_articles()
        session = await get_session(request)
        if 'username' in session:
            username = session['username']
        else:
            username = None
        return {'username': username, 'article_list': article_list}
