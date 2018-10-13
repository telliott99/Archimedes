\subsection*{Calculation}

Let's run a simulation to see what kind of numbers we get.  Start with the square ($n=2$, $2^n = 4$)
Previously we found that $S=1/\sqrt{2}$ and $T=1$ so
\[ p = 2^n S = \frac{4}{\sqrt{2}} = 2.8284 \]
\[ P = 2^n T = 4 \]
Let's try a script to calculate this to larger $n$.

\url{https://gist.github.com/telliott99/19f521c807210171a4847b319104b3df}

\begin{verbatim}        
Output:

> python pi.py
 2 2.8284271247  4.0000000000
 3 3.0614674589  3.3137084990
 4 3.1214451523  3.1825978781
 5 3.1365484905  3.1517249074
 6 3.1403311570  3.1441183852
 7 3.1412772509  3.1422236299
 8 3.1415138011  3.1417503692
 9 3.1415729404  3.1416320807
10 3.1415877253  3.1416025103
11 3.1415914215  3.1415951177
12 3.1415923456  3.1415932696
13 3.1415925766  3.1415928076
14 3.1415926343  3.1415926921
15 3.1415926488  3.1415926632
16 3.1415926524  3.1415926560
17 3.1415926533  3.1415926542
18 3.1415926535  3.1415926537
19 3.1415926536  3.1415926536
> 
\end{verbatim}

That looks pretty good to me, although it's a bit slow to converge.


\subsection*{test}
I wrote a simple test of the area formulas using Python.

The script is here:

\url{https://gist.github.com/telliott99/5269b48672cdaeca95c9c9c9d163321d}

It gives this output:

\begin{verbatim}
> python script.py 
    4 2.0000000000 4.0000000000
    8 2.8284271247 3.3137084990
   16 3.0614674589 3.1825978781
   32 3.1214451523 3.1517249074
   64 3.1365484905 3.1441183852
  128 3.1403311570 3.1422236299
  256 3.1412772509 3.1417503692
  512 3.1415138011 3.1416320807
 1024 3.1415729404 3.1416025103
 2048 3.1415877253 3.1415951177
 4096 3.1415914215 3.1415932696
 8192 3.1415923456 3.1415928076
16384 3.1415925766 3.1415926921
32768 3.1415926343 3.1415926632
65536 3.1415926488 3.1415926560
>
\end{verbatim}

The digits of the output appear to be identical or nearly so.  The only difference is that in this script I computed $2^n$ to give the number of sides.  In the previous chapter, we just print $n$.