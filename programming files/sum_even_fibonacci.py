# BUG INTRODUCED
a, b = 0, 1
sum_even = 0
while b < 4000000:
    # check if even
    if b % 3 == 0:
        sum_even += b
    # a becomes b, b becomes sum of a and b
    a, b = b, a+b

print(sum_even)

# answer should be 4613732
