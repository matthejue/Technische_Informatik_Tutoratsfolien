# Bezeichnungen
- $\boxed{r=a\mod m = a - q\cdot m} \Leftrightarrow \text{Rest modulo m}=\text{Dividend} \mod \text{Modul}=\text{Dividend} - \text{Quotient}\cdot \text{Modul}$
  - $a, q\in\mathbb{Z}, m\in\mathbb{N}$, $\boxed{r\in \{0,1,\dotsc ,m-1\}}$ und $\boxed{r \text{ ist kleinstmögliche nichtnegative Zahl}}$
- **Beispiele:**
  - $17 \operatorname{mod} 5 = 17 - 5\cdot 3= 2$
    - da $r \text{ ist kleinstmögliche nichtnegative Zahl}$, ist $17- 5\cdot 4=-3$ nicht möglich
  - $-17 \operatorname{mod} 5 = -17 - (-4\cdot 5)= -17 + 20= 3$
    - da $-17 - 3\cdot5 = -2$ negativ ist, ist es nicht erlaubt
  - $35 \mod 5 = 35 - 7\cdot 5 = 0$
  - $3 \mod 5 = 3 - 0\cdot 5 = 3$

# Restklassen
![_2020-10-29-01-18-05](_resources/_2020-10-29-01-18-05.png)
- $\mathbb{Z}/m\mathbb{Z}=\{0, \ldots, m-1\}$: Menge aller Restklassen modulo $m$ / alle Reste, die bei der Division modulo $m$ entstehen können
  - es gibt $m$ Restklassen modulo $m$, für jeden der Reste $0, 1, \ldots, m-1$ genau eine Restklasse

## Kongruent modulo m
- "$a, b\in\mathbb{Z}$ haben bei Division durch $m$ denselben Rest" $\Leftrightarrow$ "$a, b\in\mathbb{Z}$ sind kongruent modulo $m$" $\Leftrightarrow$ $a\equiv b\quad(\operatorname{mod} m)$ $\Leftrightarrow$ $a-b=k\cdot m,\quad k\in\mathbb{Z}$ (unterscheiden sich um ein Vielfaches von $m$)
- **Beispiele:**
  - $17\equiv 22\quad(\operatorname{mod}5)$, denn $17-22=(-1)\cdot 5\Leftrightarrow -5=-5$
  - $17\equiv 2\quad(\operatorname{mod}5)$, denn $17-2=3\cdot 5\Leftrightarrow 15=15$
  - $17\equiv -3\quad(\operatorname{mod}5)$, denn $17+3=4\cdot 5\Leftrightarrow 20=20$
  - $18\not\equiv 25\quad(\operatorname{mod}6)$, denn $18-25\ne k\cdot 6,\quad \forall k\in\mathbb{Z}$

## Rechenregeln innerhalb einer Restklasse
- alle Zahlen innerhalb einer Restklasse verhalten sich bei Addition bzw. Multiplikation gleich
  - man darf in Summen und Produkten eine Zahl durch irgendeinen anderen Vertreter aus ihrer Restklasse ersetzen
- $a=b,\;(\operatorname{mod} m)\wedge c=d,\;(\operatorname{mod} m)\Rightarrow$
  - **Addition:** $a+c =b+d,\;(\operatorname{mod} m)$
    - $a=qm+r_1$ und $b=pm+r_1$
    - $c=km+r_2$ und $d=hm+r_2$
    - $a+c=q m+r_{1}+k m+r_{2}=(q+k) m+\left(r_{1}+r_{2}\right)$
    - $b+d=p m+r_{1}+h m+r_{2}=(p+h) m+\left(r_{1}+r_{2}\right)$
    - $c$ und $d$ sind beliebige Zahlen, beide aus irgendeiner Äquivalenzklasse (meistens $c=d$). Rechts steht beide male der gleich Rest $(r_1 + r_2)$
  - **Multiplikation:** $a \cdot c =b \cdot d,\;(\operatorname{mod} m)$
  - **Kürzen:**
    - $a\cdot c\equiv b\cdot c\quad (\bmod m)\Leftrightarrow a\equiv b\quad (\bmod m)$ für $c\in\mathbb{Z}/m\mathbb{Z}$
    - **Beispiele:**
      - $10\equiv 40 (\bmod 6)\Leftrightarrow 5\cdot\dfrac{1}{5}\cdot 2\equiv 5\cdot\dfrac{1}{5}\cdot 8 (\bmod 6)\Leftrightarrow 2\equiv 8 (\bmod 6)$, denn $\dfrac{1}{5}=\dfrac{1+4\cdot 6}{5}=5\in\mathbb{Z}$ und damit ist $5\in(\mathbb{Z}/6\mathbb{Z})^*$
      - $8\equiv 2\quad(\operatorname{mod}6)$ kann man **nicht kürzen** zu $4\equiv 1\quad(\operatorname{mod}6)$, da man dazu mit dem Bruch $\dfrac{1}{2}$ multiplizieren müsste, aber es sind für den Rest nur $r\in\mathbb{Z}$ erlaubt
- **Beispiele:**
  - $38+22=2+4=6\quad (\operatorname{mod} 9)$
    - kleinsten Vertreter aus Restklasse finden: $38\mod 9=2$ ($38\equiv 2\;(\operatorname{mod}9)$) und $22\mod 9= 4$ ($22\equiv 4\;(\operatorname{mod}9)$). Einfach Modulo rechnen, denn $r \text{ ist kleinstmögliche nichtnegative Zahl}$, also kleinster Vertreter der Restklasse
  - $101+234=1+4=0\quad (\operatorname{mod} 5)$
  - $38\cdot 22=2\cdot 4=8\quad (\operatorname{mod} 9)$
  - $101\cdot 234=1\cdot 4= 4\quad (\operatorname{mod} 5)$
  - $38+22\cdot 17=2+2\cdot 1= 0\quad (\operatorname{mod} 4)$

# Additives Inverses
- für $S=\mathbb{Z}/m\mathbb{Z}$:
  $d=\begin{cases}
  m-e & \text{wenn } e\ne0\\
  0 & \text{wenn } e=0\\
  \end{cases}
  $

# Multiplikatives Inverses
- $(\mathbb{Z}/m\mathbb{Z})^{*}=\left\{a \in \mathbb{Z}_{m} \mid \operatorname{ggT}(a, m)=1\right\}$: Menge der Zahlen aus $\mathbb{Z}/m\mathbb{Z}$ für die es ein multiplikatives Inverses gibt
    - das sind genau die Zahlen aus $\mathbb{Z}/m\mathbb{Z}$, die zu $m$ teilerfremd sind (z.B. bei $\mathbb{Z}/4\mathbb{Z}$ sind es $(\mathbb{Z}/4\mathbb{Z})^*=\{1, 3\}$)
    - Modul ist eine Primzahl $p$ $\Rightarrow$ $(\mathbb{Z}/m\mathbb{Z})_{p}^{*}=(\mathbb{Z}/m\mathbb{Z})_{p} \backslash\{0\}$
- zu $0$ gibt es niemals ein multiplikatives Inverses in $\mathbb{Z}/m\mathbb{Z}$, denn $\forall d\in\mathbb{Z}/m\mathbb{Z}:0\cdot d=0\ne 1$ (in $\mathbb{R}$ gibt es für jede Zahl außer $0$ einen Kehrwert)
- $e\ne 0\wedge e\in\mathbb{Z}/m\mathbb{Z}, m\in\N:$ "$e$ hat einen Kehrwert" $\Leftrightarrow$ "$e$ und $m$ sind teilerfremd"
  -  **Herleitung:**
      - $2\cdot d\equiv 1\quad(\operatorname{mod}6)$, es muss gelten $2\cdot d\equiv 1 + 6n\Leftrightarrow 2\cdot d - 6n\equiv 1\Leftrightarrow 2\cdot(d - 3n)\equiv 1\Leftrightarrow 2\cdot(d - 3n)\equiv 1,\quad n\in\mathbb{Z}$. Da $2$ und $6$ einen gemeinsamen Teiler haben, gibt es kein multiplikatives Inverses, denn es gibt kein $d\in\mathbb{Z}$ mit welchem die Gleichung: $2\cdot (d-3n)=1\Leftrightarrow 2\cdot z=1,\quad z\in\mathbb{Z}$ erfüllbar ist
  - **Berechnung:**
    - <u>sukzessive:</u> $e\cdot d\equiv 1 + n\cdot m\Leftrightarrow\dfrac{1+n\cdot 9}{e}=d,\quad d\in\mathbb{Z}$, alle $n$ durchprobieren, bis ein ganzzahliges Ergebnis rauskommt
    - mit dem <u> Erweiterten Euklidischen Algorithmus</u>
  - **Anwendung:**
    - <u>verschlüsseln</u> ($y=3\cdot x\; (\operatorname{mod} 26)$) und <u>entschlüsseln</u> ($x=\frac{1}{3}y\; (\operatorname{mod} 26)$), Kehrwert muss existieren
  - **Beispiele:**
    - $\displaystyle\frac{1}{2}=\frac{1+1\cdot5}{2}=3,\quad S=\mathbb{Z}/5\mathbb{Z}$, denn $2\cdot 3\equiv 1\quad(\operatorname{mod}5)$

    - $\displaystyle\frac{1}{4}=\frac{1+3\cdot 9}{4}=7,\quad S=\mathbb{Z}/9\mathbb{Z}$,

<!--
  - $q=a \operatorname{div} m\Leftrightarrow \text{Quotient} = \text{Dividend} \operatorname{div} \text{Modul}$
  - $a=q\cdot m+r\Leftrightarrow \text{Dividend}=\text{Quotient}\cdot\text{Modul}+\text{Rest modulo m}$
-->
