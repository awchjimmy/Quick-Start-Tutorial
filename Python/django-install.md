# [python] Django 下載與安裝 - 網頁後端系列教學

### 使用虛擬環境安裝
首先建立虛擬環境，讓每一個專案可以擁有各自的 django。
```
$ python3 -m venv venv
```

啟用虛擬環境
```
$ source venv/bin/activate
```

接著用虛擬環境裡面的 pip 安裝 django
```
(venv) $ pip install django==1.11
```

### 驗證是否安裝
```
(venv) $ python
```
```
>>> import django
>>> print(django.get_version())
1.11
```
完成，可以進入下一篇教學囉！ 

### 參考資料
https://www.djangoproject.com/download/  
https://docs.djangoproject.com/en/1.11/intro/install/
