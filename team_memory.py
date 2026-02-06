class TeamMemory:
    def __init__(self, team_name):
        self.team = team_name
        self.known_roles = {}     # {player_id: role}
        self.suspicions = {}      # 可选
        self.shared_notes = []    # 可选
