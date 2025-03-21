class Accessor:
    # Provide global static access to several objects to down the tree objects
    # This is a singleton class
    _instance = None

    # Prevent multiple instances of this class
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Accessor, cls).__new__(cls)
            cls._instance.__initialized = False
        return cls._instance

    def __init__(self):
        if not self.__initialized:
            self._accessors = {}
            self.__initialized = True

    @classmethod
    def add_accessor(cls, name, obj):
        instance = cls.__get_instance()
        instance._accessors[name] = obj

    @classmethod
    def get_accessor(cls, name):
        instance = cls.__get_instance()
        return instance._accessors.get(name, None)
    
    @classmethod
    def remove_accessor(cls, name):
        instance = cls.__get_instance()
        if name in instance._accessors:
            del instance._accessors[name]

    @classmethod
    def get_accessors(cls):
        instance = cls.__get_instance()
        return instance._accessors

    @classmethod
    def __get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance