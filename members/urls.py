
from members.views import Index
from django.contrib.auth.decorators import login_required
from django.urls import path


urlpatterns = [
     path('', Index.as_view(), name='home'),

]