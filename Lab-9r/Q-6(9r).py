def sanitize_list(lst):
    if not lst:
        return []
    head = 0 if lst[0] < 0 else lst[0]
    return [head] + sanitize_list(lst[1:])

print("Sanitized list:", sanitize_list([-1, 5, -3, 7, 0, -2]))