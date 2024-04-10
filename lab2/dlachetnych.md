# Zadanie 1
## a)
- człowiek(Markus)
- pompejańczyk(Markus)
- ∀x pompejańczyk(x) -> rzymianin(x)
- władca(Cezar)
- ∀x rzymianin(x) -> lojalny(x, Cezar) ∨ nienawidzi(x, Cezar)
- ∀x ∃y lojalny(x, y)
- ∀x ∀y człowiek(x) ∧ władca(y) ∧ próbujezamachu(x, y) -> ¬lojalny(x,y)
- próbujezamachu(Markus, Cezar)

## adnotacja wersje tłumaczenia:
- ludzie próbują dokonać zamach na władcę, wobec którego są nielojalni (wersja z przykładu) albo ludzie próbują dokonać zamachu na władcę, więc są wobec niego nielojalni
- ∀x ∀y człowiek(x) ∧ władca(y) ∧ ¬lojalny(x,y) -> próbujezamachu(x, y) 
## b)
- Czy Markus był lojalny wobec Cezara?
- zakładamy wstępnie, że ¬lojalny(Markus,Cezar), podstawiamy 
- człowiek(Markus) ∧ władca(Cezar) ∧ próbujezamachu(Markus, Cezar) -> ¬lojalny(Markus,Cezar), uwzgledniamy fakty człowiek(Markus), władca(Cezar), próbujezamachu(Markus, Cezar)
- 1 -> ¬lojalny(Markus,Cezar)
- wyrażenie po drugiej stronie musi być równe 1 skoro całość jest prawdą (implikacja), więc Markus był nielojalny

## c)
- człowiek(Markus)
- pompejańczyk(Markus)
- ¬pompejańczyk(x) ∨ rzymianin(x)
- władca(Cezar)
- ¬rzymianin(x) ∨ lojalny(x, Cezar) ∨ nienawidzi(x, Cezar)
- lojalny(x, y)
- ¬człowiek(x) ∨ ¬władca(y) ∨ ¬próbujezamachu(x, y) ∨ ¬lojalny(x,y)
- próbujezamachu(Markus, Cezar)

## d) 
- ¬człowiek(Markus) ∨ ¬władca(Cezar) ∨ ¬próbujezamachu(Markus, Cezar) ∨ ¬lojalny(Markus,Cezar) + człowiek(Markus) + władca(Cezar) + próbujezamachu(Markus, Cezar) daje ¬lojalny(Markus,Cezar)
- ¬lojalny(Markus,Cezar) +  lojalny(Markus, Cezar) daje sprzeczność
- sprzeczność, więc Markus był nielojalny Cezarowi
# Zadanie 2

## a)
- ∀x jedzenie(x) -> lubić(jan, x)
- pożywienie(jabłka)
- pożywienie(kurczak)
- ∀x ∀y jeść(x, y) ∧ żyć(x) -> pożywienie(y)
- jeść(adam, orzeszki) ∧ żyć(adam)
- ∀x jeść(adam, x) -> jeść(basia, x)

## b)
- ¬pożywienie(x) ∨ lubić(jan, x)
- pożywienie(jabłka)
- pożywienie(kurczak)
- ¬jeść(x, y) ∨ ¬żyć(x) ∨ pożywienie(y)
- jeść(adam, orzeszki) 
- żyć(adam)
- ¬jeść(adam, x) ∨ jeść(basia, x)

## c) 
- dodajemy ¬lubić(jan, orzeszki)
- ¬pożywienie(jabłka) ∨ lubić(jan, jabłka) + pożywienie(jabłka) daje lubić(jan, jabłka)
- ¬jeść(adam, orzeszki) ∨ ¬żyć(adam) ∨ pożywienie(orzeszki) + żyć(adam) + jeść(adam, orzeszki)  daje pożywienie(orzeszki)
- ¬pożywienie(orzeszki) ∨ lubić(jan, orzeszki) + ¬lubić(jan, orzeszki) + pożywienie(orzeszki) daje sprzeczność
- sprzeczność, więc zakończyliśmy dowód, jan lubi orzeszki

## d) jakie pożywienie je Basia
- ¬jeść(adam, orzeszki) ∨ jeść(basia, orzeszki) + jeść(adam, orzeszki) daje jeść(basia, orzeszki)
- Basia je orzeszki
# Zadanie 3 
- czy Markus żyje, jeśli mamy rok 2021?

- człowiek(Markus)
- pompejańczyk(Markus)
- urodziny(Markus, 40)
- ¬pompejańczyk(x) ∨ śmierć(x, 79)
- ¬człowiek(x) ∨ ¬urodziny(x, t1) ∨ ¬większe(t2-t1, 150) ∨ ¬żyć(x, t2)
- ¬człowiek(x) ∨ ¬śmierć(x, t1) ∨ ¬większe(t2, t1) ∨ ¬żyć(x, t2) 
## I
- ¬człowiek(Markus) ∨ ¬urodziny(Markus, 40) ∨ ¬większe(2021-40, 150) ∨ ¬żyć(Markus, 2021)
- fakty: człowiek(Markus), pompejańczyk(Markus), urodziny(Markus, 40), ¬większe(1981, 150)
- ¬żyć(Markus, 2021)
- Markus nie żyje w 2021 roku
## II  
- ¬człowiek(Markus) ∨ ¬śmierć(Markus, 79) ∨ ¬większe(2021, 79) ∨ ¬żyć(Markus, 2021)
- fakty: człowiek(Markus), ¬większe(2021, 79)
- ¬śmierć(Markus, 79) ∨ ¬żyć(Markus, 2021)
- fakty: ¬pompejańczyk(Markus) ∨ śmierć(Markus, 79), pompejańczyk(Markus)
- ¬żyć(Markus, 2021)
- Markus nie żyje w 2021 roku
## III
- załóżmy, że żyć(Markus, 2021)
- ¬człowiek(Markus) ∨ ¬urodziny(Markus, 40) ∨ ¬większe(2021-40, 150) ∨ ¬żyć(Markus, 2021) + żyć(Markus, 2021), człowiek(Markus), urodziny(Markus, 40)
- sprzeczność, Markus nie żyje w 2021
## IV
- załóżmy, że żyć(Markus, 2021)
- ¬człowiek(Markus) ∨ ¬śmierć(Markus, 79) ∨ ¬większe(2021, 79) ∨ ¬żyć(Markus, 2021) + żyć(Markus, 2021), człowiek(Markus), ¬pompejańczyk(Markus) ∨ śmierć(Markus, 79), pompejańczyk(Markus)
- sprzeczność, Markus nie żyje w 2021
