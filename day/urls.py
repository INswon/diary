from django.urls import path
from .views import DiaryList, DiaryDetail, DiaryCreate, DiaryCreate, DiaryUpdate,DiaryDelete

app_name = 'day'

urlpatterns = [
    path('diary_list/', DiaryList.as_view(), name="diary_list"),
    path('diary_detail/<int:pk>', DiaryDetail.as_view(), name="diary_detail"),  # 修正箇所
    path('diary_create/',DiaryCreate.as_view(),name="diary_create"),
    path('diary_update/<int:pk>', DiaryUpdate.as_view(), name="diary_update"),
    path('diary_delete/<int:pk>/', DiaryDelete.as_view(), name="diary_delete"),
]

