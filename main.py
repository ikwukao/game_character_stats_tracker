# =========================================================
# GAME CHARACTER CLASS
# =========================================================
# This class represents a game character and manages:
# - character name
# - health points
# - mana points
# - character level
#
# The class also demonstrates:
# - encapsulation
# - property getters/setters
# - validation logic
# - object-oriented programming (OOP)
# =========================================================
class GameCharacter:
    # =====================================================
    # CONSTRUCTOR
    # =====================================================
    # Initialize a new game character with:
    # - name
    # - default health
    # - default mana
    # - default level
    # =====================================================
    def __init__(self, name):

        # Store character name
        self._name = name

        # Default health points
        self._health = 100

        # Default mana points
        self._mana = 50

        # Default starting level
        self._level = 1

    # =====================================================
    # NAME PROPERTY (READ-ONLY)
    # =====================================================
    # Returns the character's name.
    # =====================================================
    @property
    def name(self):
        return self._name

    # =====================================================
    # HEALTH PROPERTY
    # =====================================================
    # Returns the current health value.
    # =====================================================
    @property
    def health(self):
        return self._health

    # =====================================================
    # HEALTH SETTER
    # =====================================================
    # Validation Rules:
    # - health cannot go below 0
    # - health cannot exceed 100
    # =====================================================
    @health.setter
    def health(self, value):

        # Prevent negative health
        if value < 0:
            self._health = 0

        # Prevent health above maximum
        elif value > 100:
            self._health = 100

        # Assign valid health value
        else:
            self._health = value

    # =====================================================
    # MANA PROPERTY
    # =====================================================
    # Returns the current mana value.
    # =====================================================
    @property
    def mana(self):
        return self._mana

    # =====================================================
    # MANA SETTER
    # =====================================================
    # Validation Rules:
    # - mana cannot go below 0
    # - mana cannot exceed 50
    # =====================================================
    @mana.setter
    def mana(self, value):

        # Prevent negative mana
        if value < 0:
            self._mana = 0

        # Prevent mana above maximum
        elif value > 50:
            self._mana = 50

        # Assign valid mana value
        else:
            self._mana = value

    # =====================================================
    # LEVEL PROPERTY
    # =====================================================
    # Returns the current character level.
    # =====================================================
    @property
    def level(self):
        return self._level

    # =====================================================
    # LEVEL UP METHOD
    # =====================================================
    # This method:
    # - increases character level
    # - restores health
    # - restores mana
    # - prints confirmation message
    # =====================================================
    def level_up(self):

        # Increase level by 1
        self._level += 1

        # Restore health using setter
        self.health = 100

        # Restore mana using setter
        self.mana = 50

        # Display level-up message
        print(f"{self.name} leveled up to {self.level}!")

    # =====================================================
    # STRING REPRESENTATION
    # =====================================================
    # Returns a formatted string showing:
    # - name
    # - level
    # - health
    # - mana
    # =====================================================
    def __str__(self):

        return (
            f"Name: {self.name}\n"
            f"Level: {self.level}\n"
            f"Health: {self.health}\n"
            f"Mana: {self.mana}"
        )


# =========================================================
# TESTING THE PROGRAM
# =========================================================

# Create a new character
hero = GameCharacter("Kratos")

# Display default stats
print(hero)
print()

# Reduce health and mana
hero.health -= 30
hero.mana -= 10

# Display updated stats
print(hero)
print()

# Level up the character
hero.level_up()
print()

# Display final stats
print(hero)
