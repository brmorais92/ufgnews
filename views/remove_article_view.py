import aiohttp_jinja2


async def handle(request, context):
    response = aiohttp_jinja2.render_template('remove_article.html', request, context)
    return response
