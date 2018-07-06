import models.article.data

async def search_articles(request, search_string):
    article_list = []
    query = "SELECT * FROM noticias WHERE titulo LIKE :search_string"
    query_dict = {'search_string': '%' + search_string + '%'}
    c = request.app['db'].cursor()
    c.execute(query, query_dict)
    rows = c.fetchall()
    for row in rows:
        article = models.article.data.Article(row[0], row[1], row[2], row[3], row[4], row[5])
        article_list.append(article)
    return article_list