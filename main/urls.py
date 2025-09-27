from django.urls import path
from main.views import show_main, new_item, show_item, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, edit_item, delete_item#, new_employee

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
#    path('employee/', new_employee, name='employee'),
    path('new_item/', new_item, name='new_item'),
    path('item/<uuid:id>/', show_item, name='show_item'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:item_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:item_id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('news/<uuid:id>/edit', edit_item, name='edit_item'),
    path('news/<uuid:id>/delete', delete_item, name='delete_item')
]