Welcome to the Sample Code repo!

Here we look at four different questions:

1. FizzBuzz
2. Find lowest, highest, average number from a list of numbers.
3. Find highest prime factor of a number.
4. Generate random two-die rolls.


Prerequisites:

Please also install DDT library: https://github.com/datadriventests/ddt


Instructions:

To run tests, simply run TestingModule.
To run functions, run Main.


Optimality:

Q1: Though this is optimal solution, can probably make it a tiny bit faster if you don't separate solution into two functions.

Q2: Here I'm fairly certain this isn't the optimal solution, as we're using min, max, mean from standard (and statistics) libraries. 
    Especially with larger lists, this tends to become obvious (more so when they're unordered). You can improve that by sorting
    before finding min/max. For mean you might be able to eke out some speed imporvements from implementing in NumPy but without
    a real reason to use a heftier library it was ignored in place of the more standard libraries. I also skew towards pre-built
    solutions used by community rather than custom ones if it can be avoided (unless sufficient reason is given).
