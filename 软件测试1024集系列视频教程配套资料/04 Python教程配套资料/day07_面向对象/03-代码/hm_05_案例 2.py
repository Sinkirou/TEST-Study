class LoginPage:
    def __init__(self, username, password, code):
        self.username = username
        self.password = password
        self.code = code
        self.btn = '登录'

    def login(self):
        print(f'1. 输入用户名 {self.username}')
        print(f'2. 输入密码 {self.password}')
        print(f'3. 输入验证码 {self.code}')
        print(f"4. 点击按钮 {self.btn}")


login = LoginPage('admin', '123456', '8888')
login.login()
