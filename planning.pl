% initial state
at(robot, A).
at(obstacle, C).
at(obstacle, D).
door(A, B).
door(B, A).
door(B, C).
door(C, B).
door(C, D).
door(D, C).

% possible actions
% move through a door
move(robot, A, B) :-
    door(A, B),
    \+ at(obstacle, B).

move(robot, B, A) :-
    door(B, A),
    \+ at(obstacle, A).

% goal state
goal :- at(robot, B).

% find a plan
plan :-
    goal,
    write('Goal state reached!'), nl.

plan :-
    \+ goal,
    move(robot, A, B),
    write('Moving from '), write(A), write(' to '), write(B), nl,
    retract(at(robot, A)),
    assert(at(robot, B)),
    plan.