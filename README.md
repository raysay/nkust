# 建置虛擬環境
py -m venv *Py36Dj22*
*Py36Dj22*\\script\\activ

# 安裝套件
pip install *django*
## 安裝所有套件
pip install -r requirement.txt

# 建立專案
django-admin startproject *nkust*
註：習慣上通常會把上一層的資料夾改名為 src
    代表該資料夾中放的是原始碼 (source code)

rename *nkust* src
↑這個動作也可以直接透過檔案總管之類的做

# 進入django 資料夾
cd src

# 更新資料庫
py manage.py migrate

# 建立超級使用者
py manage.py createsuperuser

# 運作網站
py manage.py runserver

# 建立應用程式(app)
py manage.py startapp *AppName*

# 設定檔的位置
nkust\\src\\nkust\\settings.py

# 使用預設登入機制
```python
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]
```
