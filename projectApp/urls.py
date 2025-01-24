from django.urls import path
from . import views
from .views import home_view, change_password_view, get_calendar_events_view

urlpatterns = [
    path('', views.second_page, name='login'),  # 空路徑對應登入頁面
    path('login/', views.second_page, name='login'),  # 可選，提供 /login/ 進入
    path('home/', views.home_view, name='home'),
    path('change_password/', views.change_password_view, name='change_password'),  # 新增更改密碼頁面
    path('get-calendar-events/', views.get_calendar_events_view, name='get_calendar_events'),  # 新增獲取日曆事件的視圖
]