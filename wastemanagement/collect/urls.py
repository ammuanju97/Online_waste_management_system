from django . urls import path
from . import views


urlpatterns = [
    
    path('addproducts/',views.addproducts, name='addproducts'),
    path('addsell/',views.addsell, name='addsell'),
    path('ordertable/',views.ordertable, name='ordertable'),
    path('editprofile/<str:cname>',views.editprofile, name='editprofile'),
    path('collectprofile/<str:cname>',views.collectprofile, name='collectprofile'),
    path('userbuy/',views.userbuy, name='userbuy'),
    path('byustatus/<int:id>',views.byustatus,name='byustatus'),
    path('buyfun/<int:id>',views.buyfun,name='buyfun'),
    path('orderfun/<int:id>',views.orderfun,name='orderfun'),
    path('colorder/<int:id>',views.colorder,name='colorder'),
    path('colfun/<int:id>/<str:cname>/',views.colfun,name='colfun'),
    path('notifications/',views.notifications,name='notifications'),
    path('collectingagent/<str:name>',views.collectingagent, name='collectingagent'),
    path('sitevisit/<str:name>/<int:id>',views.sitevisit,name='sitevisit'),
    path('collectvisit/',views.collectvisit,name='collectvisit'),
    path('visitdate/',views.visitdate,name='visitdate'),
    
    path('payment/',views.payment,name='payment')

]