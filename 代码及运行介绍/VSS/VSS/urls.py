from django.contrib import admin
from django.urls import path
from vsapp import views as vsapp_views
from vsapp import visualViews
urlpatterns = [
    path('admin/', admin.site.urls),
    path('basic/', vsapp_views.basic, name="basic"),
    path('list/', vsapp_views.list, name="list"),
#数据库的增删查改功能
    path('find/', vsapp_views.find, name="find"),
    path('show/', vsapp_views.show, name="show"),
    path('edit/', vsapp_views.edit, name="edit"),
    path('editSuccessful/', vsapp_views.editSuccessful, name="editSuccessful"),
    path('add/', vsapp_views.add, name="add"),
    path('AddSuccessful/', vsapp_views.AddSuccessful, name="AddSuccessful"),
    path('delete/', vsapp_views.delete, name="delete"),
    path('deleteSuccessful/', vsapp_views.deleteSuccessful, name="deleteSuccessful"),
    path('deleteAll/', vsapp_views.deleteAll, name="deleteAll"),
    path('deleteAllSuccessful/', vsapp_views.deleteAllSuccessful, name="deleteAllSuccessful"),
    #excle表格导入数据功能
    path('upload/', vsapp_views.upload, name="upload"),
    path('importExcel/', vsapp_views.importExcel, name="importExcel"),
    path('index/', vsapp_views.index, name="index"),
#可视化部分
    #条形统计图
    path('barVisval/', visualViews.barVisval, name="barVisval"),
    path('bar_is_selected/', visualViews.bar_is_selected, name="bar_is_selected"),
    #目标完成情况扇形统计图
    path('targetVisval/', visualViews.targetVisval, name="targetVisval"),
    path('target_pie_label/', visualViews.target_pie_label, name="target_pie_label"),
    #工作职位类别扇形统计图
    path('jobVisval/', visualViews.jobVisval, name="jobVisval"),
    path('pie_rich_label/', visualViews.pie_rich_label, name="pie_rich_label"),
    #目标城市分布情况
    path('cityVisval/', visualViews.cityVisval, name="cityVisval"),
    path('city_label/', visualViews.city_label, name="city_label"),

]