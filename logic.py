from random import randint
import requests
import random

classes = ['Wizard', 'Fighter']

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   
        self.level = random.randint(1, 100)
        self.pokemon_number = randint(1,1000)
        self.hp = randint(1,267)
        self.power = randint(1,67)
        self.img = self.get_img()
        self.name = self.get_name()
        self.type = self.get_type()
        self.cl=random.choice(classes)

        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['other']['home']['front_default'])
        else:
            return "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/home/1.png"
    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"

    def get_type(self):
        # Здесь должен быть код для получения типа Покемона
        types = ["Fire", "Water", "Grass", "Electric", "Psychic"]
        return random.choice(types)

    def attack(self, enemy):
        if isinstance(enemy, Wizard): # Check that enemy is a Wizard data type (is an instance of the Wizard class)
            enemy.power -= 10
            chance = randint(1,5)
            if chance == 1:
                  enemy.power == 0
                  return "Покемон-волшебник применил щит в сражении"
        #if isinstance(enemy, Fighter):
            #enemy.power += 10
        #if enemy.level > enemy.level:
            #enemy.power +=15
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"
        else:
            enemy.hp = 0
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "

    # Метод класса для получения информации
    def info(self):
        return f"Имя, тип и уровень твоео покемона: имя - {self.name} , уровень - {self.level} , тип - {self.type} , хп - {self.hp}, сила - {self.power} , класс - {self.cl}"
    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img

class Wizard(Pokemon):
    pass

class Fighter(Pokemon):
    def attack(self, enemy):
        super_power = randint(5,15)
        self.power += super_power
        res = super().attack(enemy)
        self.power -= super_power
        return res + f"\nБоец применил супер-атаку силой:{super_power} "
    
if __name__ == '__main__':
    wizard = Wizard("username1")
    fighter = Fighter("username2")

    print(wizard.info())
    print()
    print(fighter.info())
    print()
    print(fighter.attack(wizard))




