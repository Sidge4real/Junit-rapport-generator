class DictionaryList:
    def __init__(self, dictionaries, sort_by):
        """
        Initializes a DictionaryList object with a list of dictionaries and a sort order.
        Gives possibility to get a sorted list based on a specific sort order defined in argument 'sort_by'.

        Args:
            dictionaries (list): A list of dictionaries to be managed.
            sort_by (list): A list specifying the order of keys for sorting.

        Attributes:
            data (list): Stores the list of dictionaries.
            sort_by (list): Stores the order of keys used for sorting.
            key (dict): selected key to sort by in you're dictionary (wich has to be sorted)

        Example:
            data = [
                {'name': 'Alice', 'currency': "dollars"},
                {'name': 'Bob', 'currency': "euros"},
                {'name': 'Charlie', 'currency': "dollars"}
            ]
            sort_by = ["dollars", "euros", "pond", "kronen"];
            dictionary_list = DictionaryList(data, sort_by);
            dictionary_list.sort_by_key("currency");
        """
        self.data = dictionaries
        self.sort_by = sort_by
        self.order = {status.lower(): index + 1 for index, status in enumerate(sort_by)}

    def sort_by_key(self, key):
        """
        Sorts the list of dictionaries by a specified key using a predefined order.

        Args:
            key (str): The key in the dictionaries to sort by.

        Raises:
            KeyError: If the specified key is not found in any dictionary.

        Example:
            dictionary_list.sort_by_key('age')
        """
        try:
            n = len(self.data)
            for i in range(n):
                for j in range(0, n-i-1):
                    if self.order[self.data[j][key]] > self.order[self.data[j+1][key]]:
                        self.data[j], self.data[j+1] = self.data[j+1], self.data[j]
        except KeyError:
            print(f"Key '{key}' not found in dictionaries.")

    def to_list(self):
        """
        Easy way to convert you're dictionary list to a standard Python list.
        Returns the list of dictionaries stored in the object. 

        Returns:
            list: The list of dictionaries.

        Example:
            sorted_data = dictionary_list.to_list()
        """
        return self.data

    def __repr__(self):
        """
        Returns a string representation of the DictionaryList object.

        Returns:
            str: String representation of the list of dictionaries.

        Example:
            print(dictionary_list)
        """
        return repr(self.data)
