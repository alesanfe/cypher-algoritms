from dataclasses import dataclass


class RailFenceCipher:

    def __init__(self, matrix, skip='\n'):
        self.matrix = [-1 if i == skip else i for i in matrix]
        self.skip = skip

    def _get_num_skip(self, limit: int) -> int:
        """
        Count the number of occurrences of -1 in the matrix up to the given limit.

        Args:
            limit (int): The limit up to which to count the occurrences.

        Returns:
            int: The number of occurrences of -1.

        """
        return sum(1 for elemento in self.matrix[:limit] if elemento == -1)

    def get_translation(self, current: int) -> int:
        """
        Get the translation of the current value based on the matrix and the number of skips.

        Args:
            current (int): The current value.

        Returns:
            int: The translated value.
        """
        num_skip = self._get_num_skip(current)  # calculate the number of skips
        return self.matrix[current] + num_skip  # return the translated value

    def transpose(self, my_list: list, current: int):
        """
        Transpose the element at the current position in the given list.

        Args:
            my_list (list): The list to transpose.
            current (int): The current position in the list.

        Returns:
            The transposed element at the current position, or the skip value if the element is to be skipped.
        """
        # Check if the current element is to be skipped
        if my_list[current] == self.skip:
            return self.skip

        # Get the new position for the current element
        new_position = self.get_translation(current)

        # Get the new object based on the new position
        new_object = my_list[new_position] if new_position != -1 else my_list[current]

        # Check if the new object is to be skipped and the current element is different from the skipped element
        if new_object == self.skip and new_object != self.matrix[current]:
            return my_list[new_position + 1]

        # Return the new object
        return new_object

    def transpose_all(self, my_list: list) -> list:
        """
        Transposes each sub-list in the given list of lists.

        Args:
            my_list (list): The list of lists to transpose.

        Returns:
            list: The transposed list of lists.
        """
        # Create a copy of the input list
        new_list = my_list.copy()

        # Iterate over the sub-lists in the input list
        for i in range(len(my_list)):
            # Transpose the current sub-list
            new_list[i] = self.transpose(my_list, i)

        # Return the transposed list of lists
        return new_list

    def encrypt(self, text: list[str]) -> str:
        """
        Encrypt the given text using the rail fence cipher.

        Args:
            text (str): The text to encrypt.

        Returns:
            str: The encrypted text.
        """
        # Create a list of lists with the given text
        my_list = [char for char in text]

        # Transpose the list of lists
        new_list = self.transpose_all(my_list)

        # Join the list of lists into a string
        return ''.join(new_list)

    @staticmethod
    def from_path(route_file: str, separator: str) -> list[str]:

        with open(route_file, "r") as f:
            route = f.read()
        items = [int(i) if i.isdigit() else i for i in route.split(separator)]

        return items
