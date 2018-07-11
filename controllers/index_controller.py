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
        session = await get_session(request)
        article_services = models.article.services.ArticleServices(request)
        if 'q' in request.rel_url.query:
            search_string = request.rel_url.query['q']
            print('opa: ' + search_string)
        else:
            search_string = ''
        article_list = await article_services.fetch_articles(search_string)
        if 'username' in session:
            username = session['username']
        else:
            username = None
        return await views.index_view.handle(request, {'username': username, 'article_list': article_list})