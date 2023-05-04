% Greatest Common Divisor (GCD)
gcd(X, Y, G) :-
    Y =:= 0,
    G is X.
gcd(X, Y, G) :-
    Y > 0,
    Z is X mod Y,
    gcd(Y, Z, G).

% Least Common Multiple (LCM)
lcm(X, Y, L) :-
    gcd(X, Y, G),
    L is X * Y / G.
