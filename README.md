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

Q3: From a mathematical point of view, the solution is probably optimal - I at least don't know of any other way to improve the
    algorithm other than going quantum. This is because once you get to square-root N speed, there's no other real way to speed things
    up except maybe with some esoteric type of sieve (if I remember correctly, those sieves were mostly used to find very very large
    primes, and aren't really suited for finding smaller primes anyway), and at any case the most difficult case you could potentially
    have is to find the largest prime factor of a two-factor number (cue cryptography speech). In that case, the quickest way I know to
    reduce your workload is to take square root - either n=p^2, or n=p*q, where p or q < sqrt(n) and the other number is greater. From
    here you kind of walk through all the possibilities from the left side until you find n%p == 0, then take the cofactor. 
    Computationally, you could make the algorithm a bit faster still by doing the sieve here, but that means you'd have to have the list
    of primes already (so instead of walking through all numbers from 2 to sqrt(n), you walk through all primes between 2 and sqrt(n)), 
    which is kind of situational - if a number is given that has primes above your list of primes, you'll miss it. So instead I opted
    for the non-sieve method.
    
    So to sum up: mathematically, probably fastest way (at least that I know of); computationally, can be imrpoved w/ sieves, but you'd
    need to know range for primes, so is avoided here. And that is only classical computational complexity.
    
Q4: The complexity here is similar to Q1 in that most of the speedups I see that can be done are by just combining the functions in Q4
    class and otherwise making things more terse. Other than that, it should be a fairly optimal solution.
