% facts
father(john, peter).
father(john, mary).
mother(susan, peter).
mother(susan, mary).
father(peter, george).
mother(mary, linda).
mother(mary, jack).

% rules
parent(X, Y) :- father(X, Y).
parent(X, Y) :- mother(X, Y).
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).
sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.
uncle(X, Y) :- parent(Z, Y), sibling(Z, X), father(X, Z).
aunt(X, Y) :- parent(Z, Y), sibling(Z, X), mother(X, Z).