from django_unicorn.components import UnicornView
from unicorn.components.moviePreview import MoviepreviewView

class IndexView(UnicornView):
    data= {}
    def onTitleClick(self, title="", desc="", poster=""):
        self.data["selected"]["title"] = title
        self.data["selected"]["desc"] = desc
        self.data["selected"]["img"] = "https://image.tmdb.org/t/p/w780"+poster
        MoviepreviewView.setData(MoviepreviewView, self.data["selected"])
