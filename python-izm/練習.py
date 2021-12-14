for x in range (20):
    x=x+1
    print('hello %s' % x)
    if x>9:
        break
    else:
        print(list(range(0,5)))

print(31%3)

fruit=['apple','banana','clementine','dragon fruit']
length=len(fruit)
for x in range(0,length):
    print('the fruit at index %s is %s' % (x,fruit[x-1]))


