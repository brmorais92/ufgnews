import models.user.data


async def fetch_user(request, user):
    query = 'SELECT * FROM usuarios WHERE nome_usuario=:username'
    query_dict = {'username': user.username}
    if user.password:
        query += ' AND senha=:password'
        query_dict['password'] = user.password
    c = request.app['db'].cursor()
    c.execute(query, query_dict)
    row = c.fetchone()
    if row:
        user = models.user.data.User()
        user.id = row[0]
        user.username = row[1]
        user.real_name = row[2]
        user.password = row[3]
        print('usuario existe: ' + user.username)
        return user
    else:
        print('usuario não existe')
        return None
