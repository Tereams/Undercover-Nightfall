class Player:
    def __init__(self, pid, role, ai, team_memory=None):
        self.id = pid
        self.role = role
        self.ai = ai
        self.alive = True
        self.belief = {}
        self.team_memory = team_memory

        ai.player = self  # 反向绑定
