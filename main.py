from aiohttp import web
import os
import aiohttp_jinja2
import jinja2
import aiohttp_session
import sqlite3
from aiohttp_session.cookie_storage import EncryptedCookieStorage

import controllers.index_controller
import controllers.session_controller


app = web.Application()
app.add_routes(controllers.session_controller.SessionController().routes)
app.add_routes(controllers.index_controller.IndexController().routes)
app['db'] = sqlite3.connect('database.sqlite3')
aiohttp_session.setup(app, EncryptedCookieStorage(os.urandom(32)))
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('views/templates/'))
app.router.add_static('/static/', path='views/static/', name='static')

web.run_app(app)