from django.urls import path
from .views import Index, Additem, Deleteitem, Updateitem, Savedlist

urlpatterns = [
    path('', Index, name = 'home'),
    path('additem', Additem, name = "additem"),
    path('deleteitem/<int:id>', Deleteitem, name = "deleteitem"),
    path('updateitem/<int:id>', Updateitem, name = "updateitem"),
    path('savedlist', Savedlist, name = "savedlist")
]