from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    url = "https://api.themoviedb.org/3/discover/movie?api_key=58817b1d581d4e9595c92a28c167872f&sort_by=popularity.desc"
    header = {
    "Content-Type":"application/json",
    }
    result = requests.get(url, headers=header)
    data = {
        "list": result.json(),
        "selected" : {
            "title" : "",
            "desc" : "",
            "img" : ""
        }
    }
    return render(request, 'basewebsite/index.html', {'data': data})