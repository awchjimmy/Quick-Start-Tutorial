# [python] 投票系統 1/7 - 網頁後端系列教學

### 事前準備

啟動虛擬環境
```
$ source venv/bin/activate
```

驗證 django 已安裝
```
(venv) $ python -m django --version
```

### 建立新專案
建立新專案的指令可以自動生成一些重要的設定檔，如資料庫設定、django 層級設定、app 層級設定等等。
```
(venv) $ django-admin startproject mysite
```

新專案建立完成後，會看到以下目錄結構，可以自行打開觀看各自內容。
```
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        wsgi.py
```

### 啟動測試伺服器
```
(venv) $ python manage.py runserver
```
可啟動測試用伺服器，在網頁中打開 http://127.0.0.1:8000/ 即可瀏覽網頁

### 建立 app
在一個專案當中，可以分成很多小的 app 系統，例如一個登入系統、一個部落格系統、一個投票系統等等。
在與 ```manage.py``` 同一個目錄中下指令：
```
(venv) $ python manage.py startapp polls
```

會產生以下結構
```
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

### 撰寫 view
開啟 ```polls/views.py``` 編輯成以下內容

```
(venv) $ vim polls/views.py
```
```
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

### 撰寫 urls
在 django 裡面，要設定哪個 url 對應到哪個 view。

新增並編輯 ```polls/urls.py``` 內容
```
(venv) $ vim polls/urls.py
```
```
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
```

接著在告訴上層 mysite/urls.py ，引入 polls 這個 app 的相關路徑：
```
(venv) $ vim mysite/urls.py
```

```
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
]
```

### 測試結果
```
(venv) $ python manage.py runserver
```
瀏覽器打開網頁 http://localhost:8000/polls/ 應該會看到剛剛的```“Hello, world. You’re at the polls index.”```

### 參考資料
https://docs.djangoproject.com/en/1.11/intro/tutorial01/
