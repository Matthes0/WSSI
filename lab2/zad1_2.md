A(X, Y) :-
    rodzic(X, Rodzic1),
    rodzic(Y, Rodzic1),
    rodzic(X, Rodzic2),
    rodzic(Y, Rodzic2),
    Rodzic1 \= Rodzic2.

B(X, Y) :-
    rodzic(X, Rodzic1),
    rodzic(Y, Rodzic2),
    rodzic(Rodzic1, Wspolny),
    rodzic(Rodzic2, Wspolny).
    

C(X, Y) :-
    rodzic(Wspolny, Rodzic1),
    rodzic(Wspolny, Rodzic2),
    rodzic(Rodzic1, X),
    rodzic(Rodzic2, Y).

D(X, Y) :-
    rodzic(Potomek1, Y),
    rodzic(Potomek1, Rodzic1),
    rodzic(X, Rodzic1),
    \+rodzic(X, Y).

E(X, Y) :-
    rodzic(X, Rodzic1),
    rodzic(X, Wspolny),
    rodzic(Y, Rodzic2),
    rodzic(Y, Wspolny),
    Rodzic1 \= Rodzic2.

F(X, Y) :- 
    rodzic(Y, Rodzic1),
    rodzic(Potomek1, Rodzic1),
    rodzic(Potomek2, Potomek1),
    rodzic(Potomek2, X).
G(X, Y) :-
    rodzic(X, Rodzic1),
    rodzic(X, Rodzic2),
    rodzic(Y, Rodzic2),
    rodzic(Potomek1, Rodzic1),
    rodzic(Y, Potomek1).
    
