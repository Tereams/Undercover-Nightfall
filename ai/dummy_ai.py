# ai/dummy_ai.py
import random
from actions import Action

class DummyAI:
    def __init__(self):
        self.player = None

    def take_action(self, phase, game_state, belief):
        return None

    def vote(self, game_state, belief):
        alive = [p for p in game_state["alive_players"] if p != self.player]
        if not alive:
            return None
        return random.choice(alive)
