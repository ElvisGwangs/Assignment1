# Base class (optional, but good practice for clarity)
class Animal:
    def make_sound(self):
        """
        Base method for making a sound.
        Subclasses will override this.
        """
        raise NotImplementedError("Subclass must implement abstract method 'make_sound'")

# Concrete class for a Dog
class Dog(Animal):
    def make_sound(self):
        """Dog's specific implementation of make_sound."""
        return "Woof!"

# Concrete class for a Cat
class Cat(Animal):
    def make_sound(self):
        """Cat's specific implementation of make_sound."""
        return "Meow!"

# Polymorphic function
def process_sound(sound_object):
    """
    This function processes any object that has a make_sound() method.
    It doesn't care if it's a Dog, a Cat, or any other class.
    """
    print(f"The animal says: {sound_object.make_sound()}")

# --- Usage Example ---
if __name__ == "__main__":
    # Create instances of the different classes
    my_dog = Dog()
    my_cat = Cat()

    # Call the same function with different object types
    process_sound(my_dog)
    process_sound(my_cat)
    