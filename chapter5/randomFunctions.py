# importing random module first
import random

# 1) .random(): generates a float (0,1);
num = random.random();
print(num);

# 2) .choice(): returns an item from a list randomly
l = [1,2,3,4];
num = random.choice(l);
print(num);

# 3) .randrange(a,b,step size): generates a random in range (a, b, step: skips when selecting)
num = random.randrange(1,5,2);
print(num);

# 4) .seed(int): saves the seeded state & can be used in multiple execution
# 1st random : by system current time
num = 10;
num = random.random();
random.seed(2);         # saves state 2
print(num);

num = random.random();
print(num);
random.seed(2);         # uses saved state
print(num)
num=random.random();

# 5) .shuffle(list): shuffles the position of a sequence(list)
l = [1,2,3];
num = random.shuffle(l);
print(l);

# 6) .uniform(): generates a random in range (a, b);    a-included, b-excluded
# uniform random number
num = random.uniform(10,20);
print(num);