class Action:
    def __init__(self, actor, target, action_type, priority):
        self.actor = actor
        self.target = target
        self.type = action_type
        self.priority = priority
