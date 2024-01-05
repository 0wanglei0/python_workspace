from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder


class PongGame(Widget):
    pass


# 两种方式加载其他目录的文件 1
Builder.load_file('ui/pong.kv')


class PongApp(App):
    def build(self):
        return PongGame()
    # 两种方式加载其他目录的文件 2
    #
    # def load_kv(self, filename=None):
    #     super().load_kv('ui/pong.kv')


if __name__ == '__main__':
    PongApp().run()
