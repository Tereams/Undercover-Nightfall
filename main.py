import random

from game import Game
from player import Player
from roles import Role
from resolver import Resolver
from win_checker import WinChecker
from ai.dummy_ai import DummyAI
from team_memory import TeamMemory

def create_roles():
    roles = []

    roles += [Role("police", team="police", can_act_at_night=True) for _ in range(4)]
    roles += [Role("killer", team="killer", can_act_at_night=True) for _ in range(4)]
    roles += [Role("civilian", team="good") for _ in range(8)]

    return roles

def main():
    random.seed(42)

    # 1. 创建角色并打乱
    roles = create_roles()
    random.shuffle(roles)

    # 2. 创建阵营记忆
    police_memory = TeamMemory("police")
    killer_memory = TeamMemory("killer")

    players = []

    # 3. 创建 Player + AI
    for i, role in enumerate(roles):
        ai = DummyAI()

        team_memory = None
        if role.team == "police":
            team_memory = police_memory
        elif role.team == "killer":
            team_memory = killer_memory

        player = Player(
            pid=i,
            role=role,
            ai=ai,
            team_memory=team_memory
        )

        players.append(player)

    # 4. 阵营内部互认（开局信息）
    for p in players:
        if p.role.team == "police":
            police_memory.known_roles[p.id] = "police"
        elif p.role.team == "killer":
            killer_memory.known_roles[p.id] = "killer"

    # 5. 创建 Game
    game = Game(
        players=players,
        resolver=Resolver(),
        win_checker=WinChecker()
    )

    # 6. Run
    game.run()

if __name__ == "__main__":
    main()
