from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder


class Register(Widget):
    txt_username = ObjectProperty(None)
    txt_password = ObjectProperty(None)

    def check_status(self, btn):
        print('button state is : {state}'.format(state=btn.state))
        print('text txt_username is : {txt}'.format(txt=self.txt_username))
        print('text txt_password is : {txt}'.format(txt=self.txt_password))


# 两种方式加载其他目录的文件 1
Builder.load_file('../ui/user_register.kv')