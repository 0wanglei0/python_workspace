class GameStats:
    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.level = 1
        self.ai_settings = ai_settings
        self.ships_left = 1
        self.game_active = False
        self.reset_stats()
        self.score = 0
        self.high_score = 0
        self.get_high_score()

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

    def get_high_score(self):
        try:
            with open("high_score_record.txt", "r") as record:
                self.high_score = int(record.readline())
        except Exception as e:
            print("no record", e)
