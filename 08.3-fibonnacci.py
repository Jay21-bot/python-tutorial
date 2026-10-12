#fibonnacci series
a = 0
b = 1

for i in range(5):
  print(a)
  c = a + b
  a = b
  b = c

# i = 0 | 1 | 2 | 3 | 4 | stopped
# o/p 0 | 1 | 1 | 2 | 3 |

# a = 0 | 1 | 1 | 2 | 3 | 5
# b = 1 | 1 | 2 | 3 | 5 | 8
# c = 1 | 2 | 3 | 5 | 8 |

#another way

print()
print('------------------------------------')
print()

a = 0
b = 1

n = int(input('How much time: '))

for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c

print()
print('------------------------------------')
print()