from django.urls import path

from . import views

app_name = "watches"

urlpatterns = [
    path("", views.index, name="index"),
    path("designers/", views.DesignerListView.as_view(), name="designers"),
    path("designer/<int:pk>/", views.DesignerDetailView.as_view(), name="designer-detail"),
    path("brands/", views.BrandListView.as_view(), name="brands"),
    path("brand/<int:pk>/", views.BrandDetailView.as_view(), name="brand-detail"),
    path("watches/", views.WatchListView.as_view(), name="watches"),
    path("watch/<int:pk>/", views.WatchDetailView.as_view(), name="watch-detail"),
    path("create_watch/", views.WatchCreateView.as_view(), name="create-watch"),
    path("update_watch/<int:pk>", views.WatchUpdateView.as_view(), name="update-watch"),
    path("delete_watch/<int:pk>", views.WatchDeleteView.as_view(), name="delete-watch"),
    path("stores/", views.StoreListView.as_view(), name="stores"),
    path("store/<int:pk>/", views.StoreDetailView.as_view(), name="store-detail"),
]
