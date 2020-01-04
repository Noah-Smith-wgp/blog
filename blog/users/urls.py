from django.conf.urls import url
from users.views import RegisterView, ImageCodeView
from users.views import SmsCodeView, LoginView
from users.views import LogoutView, ForgetPasswordView
from users.views import UserCenterView, WriteBlogView


urlpatterns = [
    # 参数1：路由
    # 参数2：视图函数
    # 参数3：路由名，方便通过reverse来获取路由
    url('register/', RegisterView.as_view(), name='register'),
    url('imagecode/', ImageCodeView.as_view(), name='imagecode'),
    url('smscode/', SmsCodeView.as_view(), name='smscode'),
    url('login/', LoginView.as_view(), name='login'),
    url('logout/', LogoutView.as_view(), name='logout'),
    url('forgetpassword/', ForgetPasswordView.as_view(), name='forgetpassword'),
    url('center/', UserCenterView.as_view(), name='center'),
    url('writeblog/', WriteBlogView.as_view(), name='writeblog'),
]
