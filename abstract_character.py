from random import randint

class AbstractCharacter:
    """ AbstractCharacter class that models an Arena fighter
    """
    def __init__(self, username):
        """ Initializes class with username
        
        Arguments:
            username {int} -- Username for Character
        """

        self._username = username
        self._health = 0
        self._attack = 0
        self._defence = 0
        self._attack_speed = 0
    
    def get_username(self):
        """ Returns Character's username
        
        Returns:
            string -- Character's initialized username
        """

        return self._username

    def get_health(self):
        """ Returns instance's current health
        
        Returns:
            int -- Character's current health
        """

        return self._health

    def get_damage(self):
        """ Calculates damage based on 50% to 100% of Character's attack
        
        Returns:
            int -- Damage Character deals when attacking
        """

        damage = randint(int(self._attack * 0.5), self._attack)
        return damage

    def take_damage(self, damage):
        """ Calculates and deals damage to Character based on input damage and Defence
        
        Arguments:
            damage {int} -- Damage dealt to Character
        """

        damage = damage - int(self._defence * 0.1)
        self._health -= damage
    
    def get_attack_speed(self): 
        """ Returns Character's attack speed
        
        Returns:
            int -- Character's Attack Speed
        """

        return self._attack_speed
    
    def get_die_roll(self):
        """ Returns an integer between 1,20 to simulate a d20 roll
        
        Returns:
            int -- Die roll between 1,20
        """

        return randint(1,20)

    def get_stats(self):
        """ Returns a string of stats for the Character
        
        Raises:
            NotImplementedError -- Raises error if not implemented by child class
        """

        raise NotImplementedError

    def get_type(self):
        """ Returns a string with the Character's type
        
        Raises:
            NotImplementedError -- Raises error if not implemented by child class
        """

        raise NotImplementedError