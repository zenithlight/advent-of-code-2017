import sympy

# this was hardcoded for my specific input
# other inputs might not work with this code

start = 107900
end = 124900

print(len([number for number in range(start, end + 1, 17) if not sympy.isprime(number)]))
