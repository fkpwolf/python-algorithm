class MovingTotal:
    array1 = []
    array2 = []
    array3 = []

    def append(self, numbers):
        """
        :param numbers: (list) The list of numbers.
        """
        for n in numbers:
            if n not in self.array1:
                for a1 in self.array1:
                    new_a2 = n + a1
                    if new_a2 not in self.array2:
                        for a2 in self.array2:
                            new_a3 = n + a2
                            if new_a3 not in self.array3:
                                self.array3.append(new_a3)
                        self.array2.append(new_a2)
                self.array1.append(n)
                

    def contains(self, total):
        """
        :param total: (int) The total to check for.
        :returns: (bool) If MovingTotal contains the total.
        """
        return total in self.array3

movingtotal = MovingTotal()
movingtotal.append([1, 2])
print("array1:", movingtotal.array1)
print("array2:", movingtotal.array2)
print("array3:", movingtotal.array3)
movingtotal.append([3])
print("array1:", movingtotal.array1)
print("array2:", movingtotal.array2)
print("array3:", movingtotal.array3)
print(movingtotal.contains(6))
print(movingtotal.contains(9))
movingtotal.append([4])
print(movingtotal.contains(9))



