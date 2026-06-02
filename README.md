# Toolsan
Toolsan is the perfect library for beginners, with a calculator parser, color or regular letter-by-letter printing, and other powerful features.
# instalation
```bash
pip install toolsan
# Code example
import toolsan as ts

# Typewriter effect in green
ts.superprint("Привет, мир!", delay=0.1, color="green")

# Loading animation for 3 seconds, speed 10
ts.loadspin(3, speed=10, color="blue")

# Calculator
print(ts.calculate("2+2*2"))      # 6
print(ts.calculate("5!"))         # 120
print(ts.calculate("√9"))         # 3
print(ts.calculate("2²+3³"))      # 4+27=31

# Search between words
text = "cat dog mouse"
print(ts.beetween(text, word="dog", left="cat", right="mouse"))  # True

# Random choice
print(ts.random_obj(["mark", "igor", "oleg"]))

# Check if a number is around the target
print(ts.around(52, 50, 10))  # True (52 between 40 and 60)
And much more.
See the source code in the toolsan folder.

