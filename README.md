# Undercover Nightfall

**Undercover Nightfall** is a single-player, text-based social deduction game inspired by classic hidden-role games such as *Who Is the Undercover* and *Night Falls, Eyes Closed*.

In this game, one human player competes alongside AI-controlled agents, each assigned a hidden role with unique abilities. The game emphasizes logical reasoning, incomplete information, and strategic decision-making under uncertainty.

---

## Game Overview

- **Total Players**: 16  
  - 1 Human player  
  - 15 AI-controlled players

- **Game Mode**: Single-player  
- **Interface**: Text-based (console output)

The game alternates between **Night** and **Day** phases until one faction meets its victory condition.

---

## Roles and Factions

### Good Faction
- **Police ×4**
- **Doctor ×1**
- **Guard ×1**
- **Cowboy ×1**
- **Civilians ×4**

### Evil Faction
- **Killers ×4**
- **Sniper ×1**

Each player is randomly assigned a role at the start of the game.  
Roles are hidden except where explicitly stated.

---
## Night Phase

During the night, players with night abilities may perform actions.  
All actions are **decided independently** and then **resolved in a fixed order**.

### Night Actions

- **Police**  
  - Vote to inspect one *alive* player  
  - Inspection results apply only after night resolution  

- **Killers**  
  - Jointly vote to eliminate one player  

- **Sniper**  
  - May eliminate one player independently  

- **Guard**  
  - Protects one player from all night damage  
  - Cannot protect the same player on consecutive nights  

- **Doctor**  
  - Has **two injection opportunities** throughout the game  
  - Injecting a player **once** saves them from night damage  
  - Injecting the **same player twice** results in that player being eliminated  
  - Injection effects can be blocked by the Guard

- **Cowboy**  
  - Draws lots each night and may:
    - Fire one shot
    - Fire two shots
    - Be unable to fire  


### Action Resolution Order

Night actions are resolved in the following strict order:

1. **Guard** – Blocks all incoming damage and effects  
2. **Doctor** – Healing or poisoning takes effect  
3. **Sniper & Cowboy** – Weapon-based eliminations  
4. **Killers** – Final elimination  

All eliminations are applied **after** resolution is complete.

---
## Day Phase

- All *alive* players vote to eliminate one player.
- A player is eliminated only if they receive **more than half of the votes** from all living players.
- If no player reaches this threshold, no one is eliminated.


---
## Victory Conditions

- **Good Faction Wins** if:
  - All **4 Killers** are eliminated

- **Evil Faction Wins** if:
  - **4 Police** are eliminated, **or**
  - **4 Civilians** are eliminated

---

UI and visualization may be added in future versions.
