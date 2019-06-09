import operator

class Rare:

    @staticmethod
    def nth_most_rare(elements, n):
        # map to store {element, times}
        ele_times = {}
        for ele in elements:
            if ele in ele_times:
                ele_times[ele] += 1
            else:
                ele_times[ele] = 1
        print('after count, map is:', ele_times)
        sorted_x = sorted(ele_times.items(), key=operator.itemgetter(1))
        print('after sort by value, map is:', sorted_x)
        if len(sorted_x) < n:
            return None
        k,_ = sorted_x[n-1]
        return k

print(Rare.nth_most_rare([5, 4, 3, 2, 1, 5, 4, 3, 2, 5, 4, 3, 5, 4, 5], 2))