class Game:
    def __init__(self):
        self.scenes = []
        self.current_scene = None
        self.systems = []

    def _set_quit_callback(self, callback):
        self.callback = callback

    def add_system(self, system):
        for sys in self.systems:
            if sys._component_type == system._component_type:
                return
        self.systems.append(system)

    def get_systems(self):
        return self.systems
    
    def get_system(self, component_type):
        for system in self.systems:
            if system._component_type == component_type:
                return system

    def add_scene(self, scene):
        self.scenes.append(scene)

    def set_current_scene(self, scene):
        self.current_scene = scene

    def get_current_scene(self):
        return self.current_scene
    
    def get_scene(self, name):
        for scene in self.scenes:

            if scene.name == name:
                return scene
        return None
    
    def get_scenes(self):
        return self.scenes

    def has_scene(self, name):
        return any(scene.name == name for scene in self.scenes)
    
    def quit(self):
        self.current_scene = None
        self.scenes = []
        self.systems = []
        print("Game quit")
        if self.callback:
            self.callback()
    
    def remove_scene(self, scene):
        if scene in self.scenes:
            self.scenes.remove(scene)