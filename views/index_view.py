import aiohttp_jinja2


# @aiohttp_jinja2.template('index.html')
async def handle(request, context):
    response = aiohttp_jinja2.render_template('index.html', request, context)
    return response