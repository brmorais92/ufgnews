import aiohttp_jinja2
import jinja2
from aiohttp_session import get_session
import time
#import models.noticia_model
from models import noticia_model
@aiohttp_jinja2.template('index.html')
async def handle(request):
    #name = request.match_info.get('name', "Anonymous")
    session = await get_session(request)
    if 'usuario' in session:
        user = session['usuario']
    else:
        user = 'anonimo'
    return {'name': user}