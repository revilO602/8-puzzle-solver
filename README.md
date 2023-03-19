# 8-Puzzle Solver
**8-Hlavolam** je zložený z 8 očíslovaných políčok a jedného 
prázdneho miesta. Políčka je možné presúvať hore, dole, vľavo alebo vpravo, ale len ak je tým smerom 
medzera. Je vždy daná nejaká východisková a nejaká cieľová pozícia a je potrebné nájsť postupnosť 
krokov, ktoré vedú z jednej pozície do druhej.
Príkladom môže byť nasledovná začiatočná a koncová pozícia (0 = medzera):

**1 2 3 \
4 5 6 \
7 8 0**

**1 2 3\
4 6 8\
7 5 0**

Problém riešime využitím **A\* algoritmu** s dvoma rôznymi heuristikami:
1. Počet políčok, ktoré nie sú na svojom mieste
2. Súčet vzdialeností jednotlivých políčok od ich cieľovej pozície
Riešenie
Program je konzolová aplikácia, ktorá bola vytvorená v programovacom jazyku Python 3. Spúšťa sa 
súbor Main.py a to štandardne:\
`$ python Main.py`

## Štruktúra

**Program** sa skladá zo štyroch súborov:

_Main.py_ : Spustiteľná časť programu, riadi vstup a výstup 

_Solver.py_: Obsahuje triedu Solver, ktorá overuje riešiteľnosť a rieši hlavolam (obsahuje aj funkciu s A* 
algoritmom)

_Node.py_: Obsahuje triedu Node, ktorá predstavuje jeden uzol v stavovom priestore

_Generator.py_: Obsahuje triedu Generator, ktorá slúži na generovanie vstupov pre účely testovania

V programe sú využité **knižnice**:

_Heapq_: poskytuje minimálnu haldu na reprezentáciu prioritného radu uzlov v stavovom priestore.

_Numpy_: poskytuje vhodné polia (najmä 2D) na reprezentáciu stavu hlavolamu.

_Timeit_: umožňuje merať čas trvania programu.

_Random_: umožňuje generovanie náhodných stavov pre vstup.
