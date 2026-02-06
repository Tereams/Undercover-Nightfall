class Resolver:
    def resolve(self, actions):
        for action in sorted(actions, key=lambda a: a.priority):
            print(f"{action.actor.id} does {action.type} on {action.target.id}")

    def resolve_votes(self, votes, players):
        from collections import Counter
        count = Counter(votes)

        if not count:
            return

        target, num = count.most_common(1)[0]
        alive = [p for p in players if p.alive]

        if num > len(alive) / 2:
            target.alive = False
            print(f"Player {target.id} eliminated by vote")
