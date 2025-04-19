def sum_dict_values(dictionary):
    """
    Returns the sum of all numeric values in the dictionary.
    Raises ValueError if any value is not numeric.
    Returns 0 for an empty dictionary.
    """
    if not isinstance(dictionary, dict):
        raise TypeError("Input must be a dictionary.")
    # Validate that all values are numeric (int or float)
    if not all(isinstance(value, (int, float)) for value in dictionary.values()):
        raise ValueError("All values in the dictionary must be numeric.")
    return sum(dictionary.values())

if __name__ == "__main__":
    # Example dictionary
    sample_dict = {'a': 100, 'b': 200, 'c': 300}

    result = sum_dict_values(sample_dict)
    print(f"Sum of all items: {result}")
