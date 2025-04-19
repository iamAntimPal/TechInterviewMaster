# Sum of All Items in a Dictionary

This Python script calculates and returns the sum of all numeric values in a dictionary.

## Features

- Accepts a dictionary with integer or float values.
- Validates that all values are numeric.
- Handles empty dictionaries (returns 0).
- Raises clear errors for invalid input.

## Usage

1. Place your dictionary in the `sample_dict` variable in `sum_dict_values.py`.
2. Run the script:
   ```
   python sum_dict_values.py
   ```

## Example

```python
sample_dict = {'a': 100, 'b': 200, 'c': 300}
```
**Output:**
```
Sum of all items: 600
```

## Error Handling

- Raises `TypeError` if input is not a dictionary.
- Raises `ValueError` if any value is not numeric.

## Author

Contributed for [TechInterviewMaster](https://github.com/your-repo-link).