import aiohttp_jinja2
import aiohttp_session
import aiohttp

import views.index_view, views.login_view

routes = aiohttp.web.RouteTableDef()

@routes.get('/login')
async def login_get(request):
    return await views.login_view.handle(request, {})

@routes.post('/login')
async def login_post(request):
    session = await aiohttp_session.get_session(request)
    data = await request.post()

    if data['usuario'] == 'eduardo':
        context = {'errors': []}
        context['errors'].append('Falha no login')
        context['errors'].append('Segundo erro')
        return await views.login_view.handle(request, context)
    else:
        session['usuario'] = data['usuario']
        raise aiohttp.web.HTTPFound('/')

@routes.get('/logout')
async def logout_get(request):
    session = await aiohttp_session.get_session(request)
    session.invalidate()
    raise aiohttp.web.HTTPFound('/')