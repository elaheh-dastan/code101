# A Python generator is a special kind of function that lets you produce a sequence of values lazily — meaning it generates each value only when needed 
# instead of building the entire list in memory.

# This makes generators great for:

# Handling large datasets without memory issues
# Creating infinite sequences
# Writing cleaner, more readable code compared to manual iteration logic

def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

gen = count_up_to(3)

next(gen)  # 1
next(gen)  # 2
next(gen)  # 3
next(gen)  # StopIteration

# When Python sees a yield:

# It pauses the function and returns a value.

# The function’s internal state is saved (local variables, instruction pointer).

# When you call next() again, execution resumes right after the yield.

# Generator Expressions
# Short form of generators:

gen = (x*x for x in range(5))

# List comprehension → makes a full list
# Generator expression → generates lazily
