from django.urls import include, path

from .views import (CategoriesView, CategoryView, CountriesView,
                    CountryView,IndexView, ManufacturersView,
                    ManufacturerView,ProductView, SearchView)

# '' - домашняя страница
# books/ - список всех книг
# authors/ - список всех авторов
# catalog/<id> детальная информация для определенной книги
# author/<id> - детальная инфа для определенного автора
urlpatterns = [
    path('', IndexView.as_view(), name='catalog-index'),
    path('catalog/product/<int:id>/', ProductView.as_view(), name='catalog-product'),
    path('catalog/search/', SearchView.as_view(), name='catalog-search'),
    path('catalog/manufacturers/',ManufacturersView.as_view(),name='catalog-manufacturers'),
    path('catalog/manufacturers/<str:name>/',ManufacturerView.as_view(),name='catalog-manufacturer',),
    path('catalog/countries/', CountriesView.as_view(), name='catalog-countries'),
    path('catalog/countries/<str:name>/', CountryView.as_view(), name='catalog-country'),
    path('catalog/categories/', CategoriesView.as_view(), name='catalog-categories'),
    path('catalog/category/<str:name>/', CategoryView.as_view(), name='catalog-category'),
]
