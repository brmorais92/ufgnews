import aiohttp_jinja2
import aiohttp

from aiohttp_session import get_session
import controllers.controller
import views.index_view
import models.article.sqlite_dao, models.article.data, models.article.services


class IndexController(controllers.controller.Controller):
    routes = aiohttp.web.RouteTableDef()

    @routes.get('/')
    async def index_get(request):
        article_services = models.article.services.ArticleServices(request)
        article_list = await article_services.fetch_articles()
        session = await get_session(request)
        if 'username' in session:
            username = session['username']
        else:
            username = None
        return await views.index_view.handle(request, {'username': username, 'article_list': article_list})

    @routes.get('/search')
    async def search_get(request):
        data = await request.query()
        print(data['q'])
        return views.index_view.handle(request, {})