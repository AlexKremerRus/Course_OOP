# волшебник (Wizard)

# воин (Figther)

# паладин (Paladin)



class Base:

    def __init__(self, health):
        self.health = health

    def go_to(self):

        print("go_to")

    def get_damage(self):

        self.health -= 10

        print(f"health = {self.health}")

    def restore_health(self):

        self.health += 5

        print(f"health = {self.health}")



class Wizard(Base):

	def __init__(self, health=100):

		super().__init__(health)



	def get_damage(self):

		self.health -= 30

		print(f"health = {self.health}")

		# print("NULL")



	def restore_health(self):

		self.health += 15

		print(f"health = {self.health}")



class Figther(Base):

	def __init__(self, health=200):

		super().__init__(health)



class Paladin(Base):

	def __init__(self, health=300):

		super().__init__(health)