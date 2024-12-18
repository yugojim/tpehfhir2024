from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from .models import Permission
import re
class CustomAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # 驗證使用者名稱是否以 'D' 或 'd' 開頭
        if not username or not re.match(r'^[Dd]', username):
            print("驗證失敗：帳號未以 'D' 或 'd' 開頭")
            return None

        # 呼叫 Active Directory（AD）進行驗證（請自行實作此邏輯）
        if not self.validate_with_active_directory(username, password):
            print("驗證失敗：AD 認證失敗")
            return None

        # 確認使用者是否已存在，若不存在則自動建立使用者
        user, created = User.objects.get_or_create(username=username)
        if created:
            user.set_password(password)  # 設置初始密碼
            user.save()
            print(f"新使用者已建立：{username}")

        # 管理使用者權限
        try:
            # 嘗試更新已存在的權限紀錄
            permission = Permission.objects.get(user=user, title="預設權限")
            permission.patient = True
            permission.outpatient = True
            permission.emergency = False
            permission.inpatient = False
            permission.medication = True
            permission.report = True
            permission.administrative = False
            permission.up = False
            permission.save()
            print(f"使用者 {username} 的權限已更新")
        except Permission.DoesNotExist:
            # 如果不存在權限紀錄，則建立新的權限
            permission = Permission.objects.create(
                user=user,
                title="預設權限",
                patient=True,         # 檢驗資料
                outpatient=True,      # 門診資料
                emergency=False,      # 急診
                inpatient=False,      # 住院
                medication=True,      # 藥物資訊
                report=True,          # 影像資料
                administrative=False, # 行政管理
                up=False,             # 上傳功能
            )
            permission.save()
            print(f"為使用者 {username} 建立新權限")

        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

    def validate_with_active_directory(self, username, password):
        """
        模擬的 AD 驗證方法，請替換成實際的 AD 認證邏輯。
        """
        from ldap3 import Server, Connection, ALL

        # 定義 AD 伺服器
        server = Server('ldap://20.205.162.209', get_info=ALL)
        #server = Server('ldap://tpech.gov.tw', get_info=ALL)
        # 定義憑證
        #username = 'yugojim@wiaad.local'  # 或 'example\\Administrator'
        #password = '1qaz@WSX3edc'

        # 建立連線
        try:
            conn = Connection(server, user=username, password=password, auto_bind=True)
            print("成功連線至 AD")
            return True
        except Exception as e:
            print(f"連線失敗: {e}")
            return False
        # 示例：僅當帳號為 "Doctor123" 且密碼為 "password123" 時認證成功
        #if username == "Doctor123" and password == "password123":
        #    return True
        #return False