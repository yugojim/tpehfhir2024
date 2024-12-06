'''
class CustomAuthBackend:
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username == "testuser" and password == "testpassword":
            from django.contrib.auth.models import User
            user, _ = User.objects.get_or_create(username=username)
            return user
        return None

    def get_user(self, user_id):
        from django.contrib.auth.models import User
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

'''
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
'''
from ldap3 import Server, Connection, ALL

# 定義 AD 伺服器
server = Server('ldap://tpech.gov.tw', get_info=ALL)

# 定義憑證
username = 'dr.gojim@WTEST.com'  # 或 'example\\Administrator'
password = 'p@ssw0rdd'

# 建立連線
try:
    conn = Connection(server, user=username, password=password, auto_bind=True)
    print("成功連線至 AD")
except Exception as e:
    print(f"連線失敗: {e}")
'''    
class CustomAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # 替换为您希望的特殊用户名和密码
        special_username = "special_user1"
        special_password = "special_password1"

        if username == special_username and password == special_password:
            # 检查是否已有此用户，不存在时创建用户
            user, created = User.objects.get_or_create(username=special_username)
            if created:
                user.set_password(special_password)  # 设置用户为无密码
                user.save()
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
