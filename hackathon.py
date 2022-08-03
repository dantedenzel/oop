import random
import time
import math
"""Agenda

Ninja Dante/Matthew pirates
Setup
1: User input and output for ninja and pirate weapons-->alters ninja stats.
2:"Set standards for ninjas and pirates"
3:Health, strength, speed. energy

Battle related Ninja items Kevin /Anwar battle related pirate items.
Code that runs during battle
4: Code a battle function->either autorun battle or user input oriented
5: Code methods for attack, superattack
6: Win quotes

oPtional:program Different starting characters, different defense stats,energy constraints,multiple players,consolodiate attack variables, take user input correctly
"""
class Player:
    def __init__( self ,name, strength=5, speed=20,health=100,energy=0,power=0 ):
        self.name = name
        self._strength = strength
        self.speed = speed
        self.health = health
        self.energy=energy
        self.power=power

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\nEnergy: {self.health}\n")

    def health_regeneration(self):
        if self.health < 100:
            self.health += 10
        print(self.name,'health increses by 10')
        print(self.name,'health:',self.health)
        if self.health > 100:
            self.health = 100
        print(self.name,'has maximum health')

    def energy_regeneration(self):
        if self.energy < 100:
            self.energy += 15
        print(self.name,'energy increses by 15')
        print(self.name,'energy:',self.energy)
        if self.energy > 100:
            self.energy = 100
        print(self.name,'has maximum energy')

    @property
    def strength (self):
        if self.energy <25:
            return self._strength - 2
        return self._strength

class Ninja(Player):

    def __init__( self ,name, strength=5, speed=20,health=100,energy=0,power=0 ):
        super().__init__(name, strength, speed,health,energy,power)
    
    def swing_sword(self , enemy):
        print("Ninja swings sword!")
        ninja_rand=random.randint(50,100)
        if ninja_rand>90:
            print("Critical Hit!")
        enemy.health -= math.floor(self.strength * (100/ninja_rand))
        self.power += math.floor(self.speed * (100/ninja_rand))
        if self.power>=100:
            print("---Active ultimate!---")
            print ("Genji: Strength flows through me!")
            print("Bonus Damage!")
            enemy.health -=self.strength*2
            self.power=0
        self.energy -=15
        print(enemy.name,"has",enemy.health,"health")
        return self

    def throw_ninja_star( self , enemy ):
        print("Ninja throws star!")
        ninja_rand=random.randint(1,50)
        if ninja_rand>45:
            print("Critical Hit!")
        enemy.health -= math.floor(self.strength * (100/ninja_rand))
        self.power += math.floor(self.speed * (100/ninja_rand))
        if self.power>=100:
            print ("Genji:Strength flows through me!")
            enemy.health -=self.strength
            self.power=0
        self.energy -=5
        print(enemy.name,"has",enemy.health,"health")
        return self

class Pirate(Player):
    def __init__( self ,name, strength=5, speed=20,health=100,energy=0,power=0 ):
        super().__init__(name, strength, speed,health,energy,power)
    
    def throw_bottle ( self , enemy ):
        print("Pirate throws bottle!")
        pirate_rand=random.randint(1,50)
        if pirate_rand>45:
            print("Critical Hit!")
        enemy.health -= math.floor(self.strength * (100/pirate_rand))
        self.power += math.floor(self.speed * (100/pirate_rand))
        if self.power>=100:
            print('Abduwali Muse: This is my ship')
            enemy.health -=self.strength
            self.power=0
        self.energy -=5
        print(enemy.name,"has",enemy.health,"health")
        return self

    def swing_sword (self , enemy ):
        print("Pirate swings sword!")
        pirate_rand=random.randint(50,100)
        if pirate_rand>90:
            print("Critical Hit!")
        enemy.health -= math.floor(self.strength * (100/pirate_rand))
        self.power += math.floor(self.speed * (100/pirate_rand))
        if self.power>=100:
            print("---Activate ultimate!---")
            print('Abduwali Muse: This is my ship')
            print("Bonus Damage!")
            enemy.health -=self.strength*2
            self.power=0
        self.energy -=10
        print(enemy.name,"has",enemy.health,"health")
        return self

ninja=Ninja("Genji")
pirate=Pirate("Abduwali Muse")

def commencebattle(user1,user2):
        user1.show_stats() 
        user2.show_stats()
        counter=0
        while (user1.health>=0) and (user2.health>=0):
            print("Round:",counter)
            user1.swing_sword(user2)
            user2.swing_sword(user1)
            counter+=1
            if (user2.health<=0) and (user1.health<=0):
                print()
                print("\nTied!")
                return
            if user2.health<=0:
                print()
                print ("Genji Wins!")
                print()
                print("Genji:An excellent fight.")
                return
            if user1.health<=0:
                print()
                print ("Abduwali Muse Wins!")
                print("Abduwali Muse:I am the captain!")
                return
            print()
commencebattle(ninja,pirate)