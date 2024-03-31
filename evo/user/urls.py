from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
        path('uhome',UserhomeView.as_view(),name="uhome"),
        path('pro',SpareView.as_view(),name="pro"),
        path('sro/<str:cat>',ProductView.as_view(),name="sro"),
        path('det/<int:did>',DetailsView.as_view(),name="det"),
        path('acart/<int:pid>',addtocart,name="addcart"),
        path('clist',CartlistView.as_view(),name="clist"),
        path('dcart/<int:cid>',CartdeleteView.as_view(),name="cdelt"),
        path('porder/<int:cid>',PlaceorderView.as_view(),name="porder"),
        path('order',OrderListView.as_view(),name="order"),
        path('corder/<int:iid>',cancelorder,name="corder"),
        path('ser',ServiceView.as_view(),name="ser"),
        path('st/<str:sat>',CenterView.as_view(),name="sat"),
        path('sdt/<int:sid>',SdetailsView.as_view(),name="sdt"),
        path('sacart/<int:uid>',secart,name="sacart"),
        path('slist',SlistView.as_view(),name="slist"),
        path('sdet/<int:sid>',ServicedeleteView.as_view(),name="sdet"),
        path('sorder/<int:vid>',PlaceserviceView.as_view(),name="sorder"),
        path('status',ServicelistView.as_view(),name="serv"),
        path('cb/<int:bid>',cancelbook,name="cancel")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)