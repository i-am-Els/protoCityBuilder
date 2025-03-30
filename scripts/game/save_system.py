from typing import Dict

from scripts.game.node import Node


class SaveObject:
    def __init__(self):
        pass

    @classmethod
    def from_dict(cls, save_object_dict):
        return SaveObject()


class Profile(Node):
    __save_data: Dict[str, SaveObject]
    def __init__(self, name):
        super().__init__(display_text=name)
        pass

    def write(self, save_object: SaveObject):
        pass


class SaveSystem:
    _instance = None
    def __init__(self):
        if not self.__initialized:
            self.__profiles: Dict[str, Profile] = {}
            self.__initialized = True

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SaveSystem, cls).__new__(cls)
            cls._instance.__initialized = False
        return cls._instance

    @classmethod
    def get_profiles(cls):
        instance = cls.__get_instance()
        return instance.__profiles
    
    @classmethod
    def get_profile(cls, name: str) -> Profile:
        instance = cls.__get_instance()
        return instance.__profiles.get(name, None)
    
    @classmethod
    def add_profile(cls, profile: Profile):
        instance = cls.__get_instance()
        instance.__profiles[profile.display_text] = profile

    @classmethod
    def remove_profile(cls, profile_name):
        instance = cls.__get_instance()
        profile = instance.__profiles.pop(profile_name)
        del profile
        # TODO - Clean up all the save files attached to the profile.

    @classmethod
    def save(cls, profile_name: str, save_object_dict: dict):
        instance = cls.__get_instance()
        profile = instance.__profiles.get(profile_name, None)
        save_object = SaveObject.from_dict(save_object_dict)
        profile.write(save_object)

    @classmethod
    def __get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance