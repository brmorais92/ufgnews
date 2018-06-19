import aiohttp_jinja2


# @aiohttp_jinja2.template('index.html')
async def test(request):
    response = aiohttp_jinja2.render_template('index.html',
                                              request,
                                              {'error': 'SE FUDEU'})
    return response