from django.urls import path

from webapp.views import IndexView, PhotoDetail, CreatePhoto, PhotoUpdate, DeleteTrackerView, FavoriteView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('photo/<int:pk>/', PhotoDetail.as_view(), name='photo_view'),
    path('create/', CreatePhoto.as_view(), name='create_photo'),
    path('photo/<int:pk>/update', PhotoUpdate.as_view(), name='photo_update'),
    path('photo/<int:pk>/delete/', DeleteTrackerView.as_view(), name='photo_delete'),
    path('photo/<int:pk>/confirm_delete/', DeleteTrackerView.as_view(), name='confirm_delete'),
    path('photo/<int:pk>/to-favorite', FavoriteView.as_view(), name='to_favorite')
]