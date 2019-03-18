from abstract_character import AbstractCharacter
from random import random
class Arena:
    """Manager Class for all character classes"""
    
    def __init__(self):
        """Initializes the Arena class"""
        self._characters = []

    def add_character(self,new_character):
        """Adds a character object to the list of characters
        
        Arguments:
            character {class} -- character object
        """
        charid = random()
        charid_used = False

        for character in self._characters:
            if character.get_id() == charid:
                charid_used = True
                break
            else:
                continue
        
        if charid_used == False:
            new_character.username = charid
            self._characters.append(new_character)
        else:
            print('Character ID already in use.')

    def get_character(self,id):
        """Returns a character based on the username supplied
        
        Arguments:
            username {string} -- The username of the character
        
        Returns:
            object -- The character object
        """

        for character in self._characters:
            if character.get_id() == id:
                return character

    def get_all(self):
        """Returns all of the objects in the character list
        
        Returns:
            list -- list of all character objects
        """

        return self._characters

    def get_all_by_type(self,type):
        """Returns all characters based on their player class
        
        Arguments:
            type {string} -- The class, or type of the user
        
        Returns:
            list -- list of all objects with given type
        """

        type_list = []
        for character in self._characters:
            if character.get_type() == type:
                type_list.append(character)

        return type_list

    def update(self,character):
        """Replaces the character with the same ID with an updated character
        
        Arguments:
            character {class} -- The new character to be replaced
        """
        if character not in self._characters:
            return 'Character not in the arena'
        else:
            for character_in_list in self._characters:
                if character.get_id == character_in_list.get_id():
                    self._characters.remove(character_in_list)
                    self._characters.append(character)

    def delete(self,id):
        """Removes a character from the list of characters
        
        Arguments:
            character {class} -- Character object to be deleted
        """

        for character in self._characters:
            if character.get_id() == id:
                self._characters.remove(character)

    @staticmethod
    def _validate_string_input(id):
        """ Private helper to validate string values """
        if id is None:
            raise ValueError("ID cannot be undefined.")

        if id == "":
            raise ValueError("ID cannot be empty.")

    @staticmethod
    def _validate_student(character):
        """ Private helper to validate students """

        if character is None:
            raise ValueError("Character must be defined.")
