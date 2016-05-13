from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from rest_framework import routers
from jrello import views


router = routers.DefaultRouter()
router.register(r'jrello', views.JrelloViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^$', TemplateView.as_view(template_name="index.html")),
]
