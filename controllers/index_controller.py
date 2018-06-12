import aiohttp_jinja2
import jinja2
from aiohttp_session import get_session
import time

@aiohttp_jinja2.template('index.html')
async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    session = await get_session(request)
    """     if session['last_visit']:
            text = "Hello, " + session['last_visit'] 
        else:
            text = "Hello, " + "EMPTY"
        session['last_visit'] = time.time() """
    #session['last_visit'] = "HAHA!"
    if 'last_visit' in session:
        print(session['last_visit'])
    else:
        session['last_visit'] = time.time()
    return {'name' : session['last_visit']}