def average_list(lst):
    def helper(lst, total=0, count=0):
        if not lst:
            return total / count if count > 0 else 0
        return helper(lst[1:], total + lst[0], count + 1)
    return helper(lst)

print("Average:", average_list([10, 20, 30, 40, 50]))