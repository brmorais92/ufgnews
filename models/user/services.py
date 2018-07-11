import models.user.data, models.user.sqlite_dao


class UserServices:
    def __init__(self, request):
        self.user = None
        self.request = request
    async def login(self):
        self.user = await models.user.sqlite_dao.fetch_user(self.request, self.user)
        if self.user:
            return True
        else:
            return False
