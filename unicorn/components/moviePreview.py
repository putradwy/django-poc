from django_unicorn.components import UnicornView


class MoviepreviewView(UnicornView):
    title=""
    desc=""
    img=""
    def setData(self, data):
        self.title = data["title"]
        self.desc = data["desc"]
        self.img = data["img"]