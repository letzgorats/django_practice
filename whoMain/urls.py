from django.urls import path
from . import views

urlpatterns = [

    path("",views.index), # /whoMain/ 을 뜻함
            # 프로젝트 단에서, urls 파일에 
            # 모든 url경로를 적용하니까 빈 값은 그냥 /whoMain/이다.
    # path("input_name",views.whoAreU),
    
    # path("all_ranking",views.ranking),

    path("<int:number>",views.whoamInumber,name = "ss"),
    # path("mainClick",views.whoamI),
    path("<str:subject>",views.whoamIstr, name = "whoMain-guess")

]