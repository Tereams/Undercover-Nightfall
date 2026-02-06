class Game:
    def __init__(self, players, resolver, win_checker):
        self.players = players
        self.resolver = resolver
        self.win_checker = win_checker
        self.phase = None
        self.round = 0

    def alive_players(self):
        return [p for p in self.players if p.alive]

    def run(self):
        while True:
            self.round += 1
            print(f"\n===== Round {self.round} =====")

            # ===== Night =====
            self.phase = "night"
            print("Night begins")

            night_actions = []
            for p in self.alive_players():
                action = p.ai.take_action(
                    phase="night",
                    game_state=self.public_state(),
                    belief=p.belief
                )
                if action:
                    night_actions.append(action)

            self.resolver.resolve(night_actions)

            if self.win_checker.check(self.players):
                break

            # ===== Day =====
            self.phase = "day"
            print("Day begins")

            votes = []
            for p in self.alive_players():
                vote = p.ai.vote(
                    game_state=self.public_state(),
                    belief=p.belief
                )
                if vote:
                    votes.append(vote)

            self.resolver.resolve_votes(votes, self.players)

            if self.win_checker.check(self.players):
                break
