def prime_numbers(nums):
    for num in nums:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            result.append(num)
    return result