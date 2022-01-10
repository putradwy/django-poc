from django_unicorn.components import UnicornView


class IndexView(UnicornView):
    
    def onTitleClick(self, title="", desc="", poster=""):
        self.data["selected"]["title"] = title
        self.data["selected"]["desc"] = desc
        self.data["selected"]["img"] = "https://image.tmdb.org/t/p/w780"+poster
