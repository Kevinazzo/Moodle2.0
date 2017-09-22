"""moodle2 URL Configuration

Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from moodle2.user import views as userViews
from moodle2.request import views as requestViews

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^user/',userViews.test,name="testJSON"),
	url(r'^groups/',requestViews.req_groups,name="req_groups"),
	url(r'^auth/(?P<username>\w+)-(?P<password>\w+)$',requestViews.authentication,name="authentication")
]