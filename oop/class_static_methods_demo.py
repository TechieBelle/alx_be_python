class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Adds two numbers and returns the result.
        This method does not access class or instance attributes.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Multiplies two numbers.
        This method accesses the class attribute calculation_type.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
