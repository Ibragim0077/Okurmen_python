print(sorted({int(i) for i in input().split()}))


numbers = map(int, input().split())
print(all(map(lambda x: sum(numbers) % x == 0, numbers)))
