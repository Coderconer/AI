% Addition
add(X, Y, Z) :- Z is X + Y.

% Subtraction
subtract(X, Y, Z) :- Z is X - Y.

% Multiplication
multiply(X, Y, Z) :- Z is X * Y.

% Division
divide(X, Y, Z) :- Z is X / Y.

% Main predicate for calculating
calculate(Operator, X, Y, Result) :-
    Operator == '+',
    add(X, Y, Result).
calculate(Operator, X, Y, Result) :-
    Operator == '-',
    subtract(X, Y, Result).
calculate(Operator, X, Y, Result) :-
    Operator == '*',
    multiply(X, Y, Result).
calculate(Operator, X, Y, Result) :-
    Operator == '/',
    divide(X, Y, Result).
