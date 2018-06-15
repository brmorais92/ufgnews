async def get_noticia(request):
    c = request.app['db'].cursor()
    c.execute("SELECT * FROM noticias")
    print(c.fetchall())
    return "HEHE"