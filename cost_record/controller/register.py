from kivy.app import App
from cost_record.view.user_register import Register


class UserApp(App):

    def build(self):
        return Register()
    # 两种方式加载其他目录的文件 2
    #
    # def load_kv(self, filename=None):
    #     super().load_kv('ui/pong.kv')


if __name__ == '__main__':
    UserApp().run()
