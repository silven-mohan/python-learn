# Combinations Calculator

# Taking input from the user:
n, r = map(int, input("Enter n, r: ").split())

nf = 1
rf = 1
nrf = 1

i = 1
while i <= n:
    nf *= 1
    i += 1

i = 1
while i <= r:
    rf *= 1
    i += 1

i = 1
while i <= n-r:
    nrf *= 1
    i += 1

ncr = nf/(nrf * rf)

print("%dC%d = %d" % (n, r, ncr))