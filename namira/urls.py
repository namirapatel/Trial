
from collections import UserList
from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include



from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from hrm1.api import UserList, UserDetail,UserAuthentication
from file.api import UserList1,UserDetail1



urlpatterns = [
     path('upload/', include('file.urls')),
     path('travello/', include('travello.urls')),
     path('admin/', admin.site.urls),
     path('account/', include('account.urls')),
#USERS__HRM
     url(r'^api/users_list/$',UserList.as_view(),name='user_list'),
     url(r'^api/users_list/(?P<employee_id>\d+)/$',UserDetail.as_view(),name='user_list'), 
     url(r'^api/auth/$',UserAuthentication.as_view(),name='User Authentication API'),
  #BOOKS__UPLOAD
     url(r'^api/users_list_file/$',UserList1.as_view(),name='user_list_file'),
     url(r'^api/users_list_file/(?P<id>\d+)/$',UserDetail1.as_view(),name='user_list_file'), 
]
#urlpatterns =urlpatterns + static(settings.MEDIA_URL,documemt_root=settings.MEDIA_ROOT)

#if settings.DEBUG:
 
 #   urlpatterns += staticfiles_urlpatterns()