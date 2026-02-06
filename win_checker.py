class WinChecker:
    def check(self, players):
        alive = [p for p in players if p.alive]

        # 先随便写一个占位规则
        if len(alive) <= 1:
            print("Game Over")
            return True
        return False
