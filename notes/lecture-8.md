---
title: "Lecture 8"
---

topics covered: Sections 3.3 and 3.4

In [Lecture 4](lecture-4.html) , you looked at the multiplicity of a two-state paramagnet. The result for the multiplicity at fixed magnetization

$$\Omega(N,M) =  \left( { N \atop \frac{1}{2}(N + U/\mu B)}\right)$$

where the magnetization was
$$
M = \sum_{i = 1}^{N} s_{i}
$$
and the energy is $U = - \mu B M$.

**Exercise:** 
1) Find the entropy for large $N$ and zero energy $U = 0$ . Use Stirling's approx *to leading order*. Recall that the Stirling approximation is best understood as an asymptotic expansion of the log of the factorial:

$$
\ln N! = N \ln N - N + \frac{1}{2} \ln N + O(1)
$$
Each successive term is smaller. 

*Solution:*
At $M = 0$, $\Omega = \left( { N \atop N/2}\right) = \frac{N!}{\left(( N/2)! \right)^{2}}$, and so 

$S/k = \ln N! - 2 \ln (N/2)!$ and for large $N$, Stirling's approximation gives

$$
S/k = N \ln N - N + \frac{1}{2} \ln N - 2 \left( \frac{N}{2} \ln \frac{N}{2} - \frac{N}{2} + \frac{1}{2} \ln N/2\right) = N \ln 2  - \frac{1}{2} \ln N  + O(1)
$$
The dominant term is linear in $N$, and proportional to $\ln 2$. 

2) When the magnetic field is zero, all configurations have the same energy (which is zero). What is the multiplicity now, in which all macrostates are equivalent (have the same energy)? What is the entropy? 

*Solution:*

There are a total of $2^{N}$ configs, so that $\Omega = 2^{N}$ and $S = N k \ln 2$. 

3) The results of (1) and (2) are nearly same (in the limit of large $N$). What is the difference? 

This result suggests that approximately all configurations are accessible at $U = 0$ at finite magnetic field. The dominant linear in $N$ contribution is the same for both. However, the entropy at $U = 0$ and $B>0$ computed in (1), is strictly smaller than the $B = 0$, $U = 0$ entropy computed in (2). This makes sense, because (2) is the largest possible value the entropy of this system can take. Now writing entropy as a function of $U$ and $B$, $S(U, B)$, I get 

$S( 0, B)= S(U,0) - \frac{1}{2} \ln N$

Note also that S(U) is maximal at $U = 0$ for this system. This means this corresponds to infinite temperature. Another interpretation then is that at infinite temperature, the magnetization will vanish even for finite magnetic field. This is essentially because in this limit, each spin becomes an independently fluctuating variable which has on average a zero dipole moment.

Treating the magnetic field as a thermodynamic variable is a bit jumping the gun - we'll get to that much later in the semester. For now, we focus on the thermodynamic variables that are more familiar: energy, number, and volume. 

### Thermodynamic Identity

Entropy is a thermodynamic state function, which depends on these three thermodynamic variables:
$$
S(U, N, V)
$$
Therefore, we can relate changes in entropy to changes in any of these three thermodynamic variables by using the chain rule along with partial derivatives, making sure to fix the appropriate variables:


$$
dS = \left( \frac{\partial S}{\partial U}\right)_{N,V} d U + \left( \frac{\partial S}{\partial V}\right)_{U, N} dV + \left( \frac{\partial S}{\partial N}\right)_{U,V} dN \tag{1}
$$

We already know that the temperature is defined via:

$$
\frac{1}{T} =  \left( \frac{\partial S}{\partial U}\right)_{N,V}
$$

Next, we can identify which thermodynamic variables the other partial derivatives are calculating. If we take for now $dN = 0$ (which corresponds to a process that involves a fixed quantity of stuff), we get from (1):

$$
dS = \frac{1}{T} dU + \left( \frac{\partial S}{\partial V}\right)_{U, N} dV
$$

We will match this to the first law of thermodynamics to interpret the partial derivative and the differential of the entropy. For the work done by a differential change in volume, we get $dW = - P dV$ (check the sign: if the volume change is positive, the gas is doing work, and losing energy from doing such work, so this sign is correct). Therefore, the first law gives us

$$
dU = Q + W = Q - P dV = T dS - T \left( \frac{\partial S}{\partial V}\right)_{U,N} dV
$$
Now matching terms, we can identify first what the differential of heat must look like

$$
Q = T dS
$$

and that the pressure can be defined in terms of entropy!

$$
\boxed{P = T \left( \frac{\partial S}{\partial V}\right)_{U,N}}
$$

This is a shortcut to the thermodynamic identity, but it's not generally true. In particular, identifying $Q = T dS$ is only correct for *quasistatic* processes. In general, the thermodynamic identity and the first law of thermodynamics are independent, and both generally true. Combined, they imply that in general

$$
dS \ge \frac{Q}{T}
$$
### Exercises:

- An adiabatic process is one which does not involve any heat transfer. What is the change in entropy for such a process? (Hint: it depends on the process)

- How does the entropy of an ideal gas depend on volume? Use this to compute the pressure. Does it make sense?



The manipulations above lead to the **thermodynamic identity**, which is another fundamental equation:

$$
\boxed{dU = T dS - P dV}
$$
You will use it to think about the following problem:

![](images/Screenshot%202025-09-21%20at%201.44.54%20PM.png)

Enthalpy was introduced in the previous chapter. It is defined
$$
H = U + PV
$$
It is a convenient way to define heat capacity at constant pressure:

$$
C_{P} = \left( \frac{\partial H}{\partial T}\right)_{P}
$$
This is all you need for the exercises below. 

**Exercise:** Find an expression for $dH$ in terms of $dS$ and $dP$ using the thermodynamic identity:

*Solution:* 

$$
dH = dU + P dV + V dP = T dS + V dP
$$


This will be useful to solve the next problem:

![](images/Screenshot%202025-09-21%20at%202.05.58%20PM.png)









***
