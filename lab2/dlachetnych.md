# Zadanie 1
## a)
- człowiek(Markus)
- pompejańczyk(Markus)
- ∀x pompejańczyk(x) -> rzymianin(x)
- władca(Cezar)
- ∀x rzymianin(x) -> (lojalny(x, Cezar) ∨ nienawidzi(x, Cezar))
- ∀x ∃y lojalny(x, y)
- ∀x ∀y (człowiek(x) ∧ władca(y) ∧ próbujezamachu(x, y) -> ¬lojalny(x,y)) albo  ∀x ∀y (człowiek(x) ∧ władca(y) ∧ ¬lojalny(x,y)) -> próbujezamachu(x, y) 
- próbujezamachu(Markus, Cezar)

## adnotacja wersje tłumaczenia:
- ludzie próbują dokonać zamach na władcę, wobec którego są nielojalni (wersja z przykładu) albo ludzie próbują dokonać zamachu na władcę, więc są wobec niego nielojalni

## b)
- Czy Markus był lojalny wobec Cezara?

- wiemy, że Markus był człowiekiem a Cezar władcą
- wiemy też, że Markus próbował zamachu na Cezarze
- (1 ∧ 1 ∧ 1) -> ¬lojalny(Markus,Cezar) (całość ma wartość 1, bo próbował dokonać zamachu)
- 1 -> ¬lojalny(Markus,Cezar), skoro całość ma wartość 1, to markus był nielojalny, bo 1 -> 1 daje 1, a 1 -> 0 byłoby fałszem

## c)
- człowiek(Markus)
- pompejańczyk(Markus)
- ¬pompejańczyk(x) ∨ rzymianin(x)
- władca(Cezar)
- ¬rzymianin(x) ∨ lojalny(x, Cezar) ∨ nienawidzi(x, Cezar)
- lojalny(x, władca(x))
- ¬człowiek(x) ∨ ¬władca(y) ∨ ¬próbujezamachu(x, y) ∨ ¬lojalny(x,y) albo  ¬człowiek(x) ∨ ¬władca(y) ∨ lojalny(x,y) ∨ próbujezamachu(x, y) 
- próbujezamachu(Markus, Cezar)

## d) 
- zakładamy ¬lojalny(Markus, Cezar)
- ¬człowiek(Markus) ∨ ¬władca(Cezar) ∨ lojalny(Markus,Cezar) ∨ próbujezamachu(Markus, Cezar) 
- ¬człowiek(Markus) ∨ ¬władca(Cezar) ∨ próbujezamachu(Markus, Cezar) 
- człowiek(Markus), - władca(Cezar)
- próbujezamachu(Markus, Cezar) 
- ¬człowiek(Markus) ∨ ¬władca(Cezar) ∨ ¬próbujezamachu(Markus, Cezar) ∨ ¬lojalny(Markus, Cezar)
- ¬człowiek(Markus) ∨ ¬władca(Cezar) ∨ ¬lojalny(Markus, Cezar)
- człowiek(Markus), - władca(Cezar)
- ¬lojalny(Markus, Cezar)
- lojalny(Markus, władca(Markus) (Cezar))
- sprzeczność, więc zakończyliśmy dowód
# Zadanie 2

## a)
- ∀x lubić(jan, x)
- pożywienie(jabłka)
- pożywienie(kurczak)
- ∀x ∀y (jeść(x, y) ∧ żyć(x)) -> pożywienie(y)
- jeść(adam, orzeszki) ∧ żyć(adam)
- ∀x jeść(adam, x) -> jeść(basia, x)

## b)
- lubić(jan, x)
- pożywienie(jabłka)
- pożywienie(kurczak)
- ¬jeść(x, y) ∨ ¬żyć(x) ∨ pożywienie(y)
- jeść(adam, orzeszki) ∧ żyć(adam)
- ¬jeść(adam, x) ∨ jeść(basia, x)

## c) 
- ¬lubić(jan, orzeszki)
- lubić(jan, orzeszki)
- sprzeczność, więc zakończyliśmy dowód

## d) 
- jeść(adam, x) ∧ ¬jeść(basia, x)
- ¬jeść(adam, x) ∨ ¬żyć(adam) ∨ pożywienie(x)
- ¬jeść(basia, x) ∨ ¬żyć(adam) ∨ pożywienie(x)
- ¬jeść(adam, x) ∨ jeść(basia, x)
- ¬jeść(adam, x) ∨ ¬żyć(adam) ∨ pożywienie(x)
- jeść(adam, orzeszki) ∧ żyć(adam)
- adam je orzeszki, więc basia też je orzeszki
# Zadanie 3 
- czy Markus żyje, jeśli mamy rok 2021?
## I
- człowiek(Markus)
- pompejańczyk(Markus)
- urodziny(Markus, 40)
- ∀x pompejańczyk(x) -> śmierć(x, 79)
- ∀x ∀t1 ∀t2 (człowiek(x) ∧ urodziny(x, t1) ∧ większe(t2-t1, 150)) -> ¬żyć(x, t2) 
- ∀x ∀t1 ∀t2 (człowiek(x) ∧ śmierć(x, t1) ∧ większe(t2, t1)) -> ¬żyć(x, t2) 
-  (człowiek(Markus) ∧ urodziny(Markus, 40) ∧ większe(2021-40, 150)) -> ¬żyć(Markus, 2021)
-  Markus nie żyje
## II  
- człowiek(Markus)
- pompejańczyk(Markus)
- pompejańczyk(Markus) -> śmierć(Markus, 79)
- (człowiek(Markus) ∧ śmierć(Markus, 79) ∧ większe(2021, 79)) -> ¬żyć(Markus, 2021) 
- Markus nie żyje
