from typing import List
from scripts.core.engine import clear_screen
from scripts.game.economy import Resources, Stats

class MainDashboard:
    __max = 5
    __notifications: List[str] = []
    def __init__(self):
        pass

    @classmethod
    def get_notifications(cls):
        return cls.__notifications
    
    @classmethod
    def push_notification(cls, new_notification):
        if len(cls.__notifications) == cls.__max:
            cls.__notifications.pop(-1)
        cls.__notifications.insert(0, new_notification)

    @classmethod
    def pop_notification(cls, index):
        cls.__notifications.pop(index)

    @classmethod
    def pop_notification(cls, notification):
        cls.__notifications.remove(notification)
    

    @classmethod
    def draw_ui(cls):
        clear_screen("")
        print(f"-------------------- Welcome to TextCraft ---------------------\n"
            f"Quest: [New Quest]        Progress: 0       Food: {Resources.getFood()}\n"
            f"Population: {Stats.getPopulation()}/ {Stats.getPopulationCapacity()}                          Gold: {Resources.getGold()}\n"
            f"Morale: {Stats.getMorale()}                                  Iron: {Resources.getIron()}\n"
            f"Defensive Strength: {Stats.getDefenseStrength()}                      Stone: {Resources.getStone()}\n"
            f"Leadersip: {Stats.getMorale()}                               Wood: {Resources.getWood()}\n"
            f"Diplomacy: {Stats.getDiplomacy()}                               Coin: {Resources.getCoin()}\n\n"
            f"------------------------- Notifications ------------------------"
            )
        notifications = cls.get_notifications()
        if len(notifications) > 0:
            for notification in notifications:
                print(f"* {notification}")
        else:
            print(f"No Notifications yet.")
        print("\n -------------------------------------------------------------------\n")
