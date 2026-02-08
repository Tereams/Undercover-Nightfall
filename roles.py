class Role:
    def __init__(self, name, team=None, can_act_at_night=False):
        self.name = name
        self.team = team
        self.can_act_at_night = can_act_at_night
