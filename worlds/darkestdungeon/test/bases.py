from test.bases import WorldTestBase

from ..World import DarkestDungeonWorld

class DDTestBase(WorldTestBase):
    game = "Darkest Dungeon"
    world : DarkestDungeonWorld