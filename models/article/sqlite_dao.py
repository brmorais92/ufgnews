import models.article.data


async def search_articles(request, search_string):
    c = request.app['db'].cursor()
    article_list = []
    query = "SELECT * FROM noticias WHERE titulo LIKE :search_string ORDER BY enviado_timestamp DESC"
    query_dict = {'search_string': '%' + search_string + '%'}
    c.execute(query, query_dict)
    rows = c.fetchall()
    for row in rows:
        article = models.article.data.Article(row[0], row[1], row[2], row[3], row[4], row[5])
        article_list.append(article)
    return article_list


async def fetch_article(request, id):
    c = request.app['db'].cursor()
    query = "SELECT * FROM noticias WHERE id=:id"
    query_dict = {'id': id}
    c.execute(query, query_dict)
    row = c.fetchone()
    article = models.article.data.Article(row[0], row[1], row[2], row[3], row[4], row[5])
    return article


async def create_article(request, article):
    c = request.app['db'].cursor()
    query = "INSERT INTO noticias(id_autor, titulo, corpo) VALUES (:author_id, :title, :body)"
    query_dict = {'author_id': article.author_id, 'title': article.title, 'body': article.body}
    c.execute(query, query_dict)
    request.app['db'].commit()


async def remove_article(request, article):
    c = request.app['db'].cursor()
    query = "DELETE FROM noticias WHERE id=:id"
    query_dict = {'id': article.id}
    c.execute(query, query_dict)
    request.app['db'].commit()

async def update_article(request, article):
    c = request.app['db'].cursor()
    query = "UPDATE noticias SET titulo=:title, corpo=:body, WHERE id=:id"
    query_dict = {'id': article.id, 'title': article.title, 'body': article.body}
    c.execute(query, query_dict)
    request.app['db'].commit()
