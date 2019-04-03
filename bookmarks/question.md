<h4> 遇到的问题

><h5> {% load static%} 和 {% load staticfiles %}
> 
> 
内置的 static 模板标签 “将[s]链接到保存在的静态文件中 STATIC_ROOT”。
该 staticfiles 贡献应用程序 static 模板标签 “使用配置的 STATICFILES_STORAGE 存储以创建给定相对路径的完整URL“，这在使用非本地存储后端部署文件时特别有用”。
内置的 static 模板标签的文档（链接到上面）有一个说明使用的说明 staticfiles 贡献应用程序 static 模板标记“如果您有一个高级用例，例如使用云服务来提供静态文件”，那么它就是这样做的例子：
{% load static from staticfiles %}
<img src="{% static "images/hi.jpg" %}" alt="Hi!" />
你可以用 {% load staticfiles %} 而不是 {% load static from staticfiles %} 如果你想，但后者更明确。


>wrapper()

> Django 如何添加用户的~ **(solved)**

> novalidate 的意思是

novalidate 属性规定当提交表单时不对其进行验证。

> 关于url栏的问题


```
path("reset/<uidb64>/<token>/",)
```
把uidb64 写出了uid64，导致系统500，
说明变量自己跟系统一致的重要性

> instance 用于指定表单内某个具体的数据对象

> enctype="multipart/form-data"
 
 用来处理头像的