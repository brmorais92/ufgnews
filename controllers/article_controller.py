import aiohttp_jinja2
import aiohttp
import aiohttp_session

from aiohttp_session import get_session
import controllers.controller
import views.add_article_view, views.index_view, views.remove_article_view
import models.article.sqlite_dao, models.article.data, models.article.services


class ArticleController(controllers.controller.Controller):
    routes = aiohttp.web.RouteTableDef()

    @routes.get('/add_article')
    @aiohttp_jinja2.template('add_article.html')
    async def add_article_get(request):
        return {}
 
    @routes.post('/add_article')
    async def add_article_post(request):
        data = await request.post()
        session = await aiohttp_session.get_session(request)
        services = models.article.services.ArticleServices(request)
        article = models.article.data.Article()
        article.author_id = session['user_id']
        article.title = data['title']
        article.body = data['body']
        if await services.create_article(request, article):
            return await views.index_view.handle(request, {})
        else:
            return await views.add_article_view.handle(request, {'errors': ['Artigo inválido']})

    @routes.get('/remove_article/{id}')
    async def remove_article_get(request):
        return await views.remove_article_view.handle(request, {'id': request.match_info['id']})

    @routes.post('/remove_article')
    async def remove_article_post(request):
        data = await request.post()
        services = models.article.services.ArticleServices(request)
        article = models.article.data.Article()
        article.id = data['id']
        await services.remove_article(request, article)
        return await views.index_view.handle(request, {})
