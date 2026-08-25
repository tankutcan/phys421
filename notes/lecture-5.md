---
title: "Entropy, Macrostates, and Microstates"
---

## Stirling's Approximation

$$
\boxed{\log N! = N \log N - N  + \frac{1}{2}\log (2\pi N)}
$$

The fastest way to show this is by using the [Euler-Maclaurin Formula](https://en.wikipedia.org/wiki/Euler–Maclaurin_formula)
$$
\sum_{k = a}^{b} f(k) = \int_{a}^{b} dk \, f(k) + \frac{1}{2} \left( f(a) + f(b)\right) + {\rm remainder\, terms}
$$
The wikipedia page gives a formula for pushing this to higher orders, and computing as many terms in the remainder as you wish. 

I will apply it to the log of the factorial. First, notice that the factorial is a product of many integers, and that the log of a product is the sum of logs:
$$
\ln N! = \ln N (N-1) (N-2) ... 1 = \ln (1) + \ln (2) + ... + \ln (N-1) + \ln(N)
$$
This implies I can write the log of the factorial as
$$
\ln N! = \sum_{k = 1}^{N} \ln k 
$$
Now that I have a discrete sum, I can apply the Euler-Maclaurin formula. I will use $f(k) = \ln k$ , $a = 1$, and $b = N$. Using

$$
 \int_{1}^{N} dk \ln k = \left(k \ln k - k \right) \Big|_{1}^{N} =  N \log N- N
$$
This gives the leader order terms in Stirling's approximation, and the boundary correction adds the factor of $\frac{1}{2} \ln N$. What this approach cannot immediately get you is the constant correction. Can you 



**Extra Practice:**
If you've taken complex analysis, you know the following remarkable identity: 

$$
\sum_{n = 1}^{\infty} \frac{1}{n^{2}} = \frac{\pi^{2}}{6} \approx 1.64
$$
Using the Euler-Maclaurin formula gives ~ 1.5, not bad!

When you are expanding $ln N!$, you need to be able to keep track of terms according to how large they are. Below, you will see a plot of different functions. Even for modestly large $x$, they establish a hierarchy. $ln(x)$ is slowest growing, then comes linear $x$, and somewhat larger than linear is $x \ln x$. This will be helpful in one of the problems below. 

![](images/Screenshot%202025-09-11%20at%203.37.08%20PM.png)

## **Exercises**
---

### Necessary Knowledge:
You must be 100% confident with this problem.

![](images/Screenshot%202025-09-11%20at%2010.52.06%20AM.png)



***
### Applications of Stirling's Formula in different Limits

![](images/Screenshot%202025-09-11%20at%2010.54.14%20AM.png)

*Solution:*

We will solve two versions of this problem. The first one, I will say that $q = O(1)$, while $N >>1$. This means that only $N$ is large, and $q$ is a small number, like 2 or 3. 

Starting with the multiplicity of an Einstein solid is

$$
\Omega(q, N) = \frac{(N +q - 1)!}{q! (N-1)!}
$$

For $N >>1$ and $q \sim 1$, we notice that

$$
(N+q - 1)! = (N+q - 1)\times  ( N+q - 2)\times ... \times N \times (N - 1)! 
$$
When I divide by $(N-1)!$, I get

$$
\Omega(q, N) = \frac{N (N+1) (N+2) .... (N+q - 1)}{q! }
$$
Now since $q$ is much smaller than $N$, I can treat the numerator as a product of $q$ terms, each of order $N$, so I get

$$
\Omega \approx \frac{N^{q}}{q!}
$$
Next, consider both $q, N>>1$, but in addition $q << N$. A very convenient way to deal with this limit is to take $q = x N$, and take $x <<1$.  The first thing we do is apply Stirling's formula for large $N$, and then expand the result for small $x$. 

We need to apply Stirling's formula to the following:

$$
\ln q! = \ln (x N)! = x N \ln (x N) - x N
$$
$$
\ln(N+q)! = \ln \left( (1 + x)N\right)! = (1 + x)N \ln ( (1 + x)N) - (1 + x)N
$$
Using these, 
$$
\ln \Omega \approx  (1 + x) N \left( \ln (1 + x) + \ln N\right) - (1+x)N - (x N \ln x + x N \ln N - x N) - (N \ln N - N)  + ...
$$


Plus corrections which are order $\ln N$, and thus much smaller. Simplifying this with algebra gives

$$
\ln \Omega \approx N  \left[ (1 + x) \ln (1 + x)  - x  \ln x \right] + ...
$$
Which is remarkably simple already. Next, we expanding $\ln (1+x)$, 

$$
\ln (1 + x) \approx  x 
$$

$$
\ln \Omega \approx  N x \left[ (1 + x) -  \ln x \right]  \approx - N x \ln x
$$

For $x << 1$, the hierarchy from before flips: $- \ln x$ is much larger than $x + 1$, so this term wins. We can rewrite this term using the definition $x = q/N$, and get

$$
 \ln \Omega \approx  q \log (N/q)
$$
---

### Extra problem to think about accessible states
![](images/Screenshot%202025-09-11%20at%2012.35.31%20PM.png)

![](images/Screenshot%202025-09-11%20at%2012.37.03%20PM.png)

***
