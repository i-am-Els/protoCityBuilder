from enum import Enum


class Resources:
    __iron = 10
    __stone = 10
    __food = 10
    __wood = 10
    __gold = 10
    __coin = 20
    def __init__(self):
        pass
    
    @classmethod
    def getIron(cls):
        return cls.__iron
    
    @classmethod
    def addIron(cls, value):
        cls.__iron += value

    @classmethod
    def getStone(cls):
        return cls.__stone
    
    @classmethod
    def addStone(cls, value):
        cls.__stone += value

    @classmethod
    def getFood(cls):
        return cls.__food
    
    @classmethod
    def addFood(cls, value):
        cls.__food += value

    @classmethod
    def getWood(cls):
        return cls.__wood
    
    @classmethod
    def addWood(cls, value):
        cls.__wood += value

    @classmethod
    def getGold(cls):
        return cls.__gold
    
    @classmethod
    def addGold(cls, value):
        cls.__gold += value

    @classmethod
    def getCoin(cls):
        return cls.__coin
    
    @classmethod
    def addCoin(cls, value):
        cls.__coin += value

class Stats:
    __population = 20
    __population_capacity = 50
    __diplomacy= 10
    __leadership = 10
    __morale = 85
    __research_progress  = 5
    __defence_strength = 70

    def __init__(self):
        pass

    @classmethod
    def addPopulation(cls, value):
        cls.__population += value

    @classmethod
    def getPopulation(cls):
        return cls.__population
    
    @classmethod
    def addPopulationCapacity(cls, value):
        cls.__population_capacity += value

    @classmethod
    def getPopulationCapacity(cls):
        return cls.__population_capacity
    
    @classmethod
    def addDiplomacy(cls, value):
        cls.__diplomacy += value

    @classmethod
    def getDiplomacy(cls):
        return cls.__diplomacy
    
    @classmethod
    def addLeadership(cls, value):
        cls.__leadership += value

    @classmethod
    def getLeadership(cls):
        return cls.__leadership

    @classmethod
    def addMorale(cls, value):
        cls.__morale += value

    @classmethod
    def getMorale(cls):
        return cls.__morale
    
    @classmethod
    def addResearchprogress(cls, value):
        cls.__research_progress += value

    @classmethod
    def getResearchProgress(cls):
        return cls.__research_progress
    
    @classmethod
    def addDefenseStrength(cls, value):
        cls.__defence_strength += value

    @classmethod
    def getDefenseStrength(cls):
        return cls.__defence_strength
    
class PopulationGrowthRate(Enum):
    NoGrowth = 0
    Low = 1
    Moderate = 2
    High = 3


class Economy:
    def __init__(self):
        pass

    def checkPopulationGrowth(self):
        percentage = self.getPopulationPercentage()
        if percentage > 80: 
            return PopulationGrowthRate.High
        elif percentage > 40: 
            return PopulationGrowthRate.Moderate
        else: 
            return PopulationGrowthRate.Low
        
    def getPopulationPercentage(self)-> float:
        return Stats.getPopulation() / Stats.getPopulationCapacity() * 100

    def checkCanAddPeople(self) -> bool:
        return Stats.getPopulation() < Stats.getPopulationCapacity()

