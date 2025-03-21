from game import Game
from scripts.core.scene import Scene


class Engine:
    def __init__(self, name):
        self.name = name
        self.game = Game()
        self.game.add_scene(scene=Scene(name="Main"))
        self.game.set_current_scene(scene=self.game.get_scene(name="Main"))
        self.is_running = False
        self.game._set_quit_callback(self.quit)

    def run(self):
        self.is_running = True
        self.awake()
        self.start()
        while self.is_running:
            for system in self.game.get_systems():
                system.update()
        self.on_destroy()

    def awake(self):
        for system in self.game.get_systems():
            system.awake()

    def start(self):
        for system in self.game.get_systems():
            system.start()

    def on_destroy(self):
        for system in self.game.get_systems():
            system.on_destroy()
        self.is_running = False
        print(f"Engine {self.name} destroyed")

    def quit(self):
        self.is_running = False