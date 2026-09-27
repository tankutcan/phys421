---
title: "Lecture 8"
---

Temperature is defined by

$$
\boxed{\frac{1}{T}=\left(\frac{\partial S}{\partial U}\right)_{N,V}}
$$

This is the fundamental equation. Let us revisit the problem of two gases brought into thermal contact.

Recall from [Lecture 7](lecture-7.html) that the multiplicity of an ideal gas has the energy dependence

$$
\Omega_N\approx f(N,V)U^{fN/2},
$$

where $f=1$ for a one-dimensional monatomic gas, $f=3$ for a three-dimensional monatomic gas, and so on. All other dependence is included in $f(N,V)$. The entropy is therefore

$$
S=k\ln\Omega=\frac{fkN}{2}\ln U+k\ln f(N,V).
$$

In the previous class, two gases $A$ and $B$ had identical containers and the same number of molecules, but started with energies $U_A$ and $U_B$. After thermal contact, each had half the total energy, $(U_A+U_B)/2$. We found this by maximizing multiplicity. Because the logarithm is monotonic, maximizing $\Omega$ also maximizes $S$:

$$
\frac{\partial S}{\partial U}=\frac{k}{\Omega}\frac{\partial\Omega}{\partial U}=0.
$$

For the combined system, $\Omega_{AB}\approx\Omega_A\Omega_B$, so its entropy has the form

$$
S_{AB}=S_0(N,V)+\frac{fkN}{2}\ln U_A+\frac{fkN}{2}\ln U_B,
$$

where $S_0(N,V)$ collects the terms independent of energy. To maximize $S_{AB}$ with respect to $U_A$, set

$$
\frac{\partial S_{AB}}{\partial U_A}
=\frac{\partial S_A}{\partial U_A}+\frac{\partial S_B}{\partial U_A}=0.
$$

The total energy $U=U_A+U_B$ is fixed, so $U_B=U-U_A$ and $\partial U_B/\partial U_A=-1$. By the chain rule,

$$
\frac{\partial S_B}{\partial U_A}
=\frac{\partial S_B}{\partial U_B}\frac{\partial U_B}{\partial U_A}
=-\frac{\partial S_B}{\partial U_B}.
$$

The maximum-entropy condition is therefore

$$
\frac{\partial S_A}{\partial U_A}-\frac{\partial S_B}{\partial U_B}=0.
$$

By the definition of temperature, this means $T_A=T_B$. Thermal equilibrium follows from maximizing entropy or multiplicity.

## Thinking about equilibrium visually

For an ideal gas,

$$
S\sim\frac{Nfk}{2}\ln U,
\qquad \frac{1}{T}=\frac{Nfk}{2U},
\qquad U=\frac{Nf}{2}kT.
$$

The last result agrees with equipartition. For two identical subsystems with $U=U_A+U_B$,

$$
T_A=\frac{2U_A}{Nfk},
\qquad T_B=\frac{2U_B}{Nfk}=\frac{2(U-U_A)}{Nfk}.
$$

As functions of $U_A/U$, these are straight lines that intersect at $U_A/U=1/2$. On the left, $T_B>T_A$, heat flows into $A$, and $U_A$ increases. On the right, $T_A>T_B$, heat flows out of $A$, and $U_A$ decreases. Both directions lead toward the intersection, so the equilibrium is stable.

The figure below shows the temperature for the two systems as a function of the energy $U_{A}$ of the subsystem. 
![](images/Screenshot%202025-09-17%20at%202.45.43%20PM.png)



## Exercises: revisiting heat and entropy

**Problem 2.34.** Show that during a quasistatic isothermal expansion of a monatomic ideal gas, the entropy change is related to the heat input by

$$
\Delta S=\frac{Q}{T}.
$$

The next chapter proves this formula for any quasistatic process. Show that it does not hold for free expansion.

*Solution:* This problem combines the first law, the ideal gas law, and equipartition. The volume dependence of entropy can be written

$$
S(N,V,U)=Nk\ln V+g(N,U).
$$

More generally, at constant volume the definition of temperature gives

$$
dS=\frac{dU}{T}.
$$

By the first law, $dU=dW+dQ=dQ$ at constant volume because work is zero. Hence

$$
dS=\frac{dQ}{T}.
$$

Using the constant-volume heat capacity, $dU=C_V\,dT$, we can write

$$
dS=C_V\frac{dT}{T}
\quad\Longrightarrow\quad
S(T)-S(0)=\int_0^T\frac{C_V(T')}{T'}\,dT'.
$$



## Visual reasoning about thermal equilibrium

**Problem 3.3.** Consider graphs of entropy versus energy for two objects, $A$ and $B$, drawn on the same scale. Both curves increase and bend downward. At the marked initial energies $U_{A,\mathrm{initial}}$ and $U_{B,\mathrm{initial}}$, the slope of $S_A(U_A)$ is steeper than the slope of $S_B(U_B)$. The objects are then brought into thermal contact. Explain what happens and why, *without using the word “temperature.”*


## Miserly systems

As in Exercise 2.42, the entropy of a black hole is a quadratic function of energy: $S\sim U^2$. Its temperature therefore scales as

$$
T\sim\frac{1}{U}.
$$

For two such systems $A$ and $B$ with total energy $U=U_A+U_B$, does an equilibrium exist? Will systems starting at different energies reach it?

The temperature curves as functions of $U_A/U$ intersect at equal energies. To the left of the intersection, $T_A>T_B$, heat flows into $B$, and $U_A$ decreases. To the right, $T_B>T_A$, heat flows into $A$, and $U_A$ increases. The intersection exists, but any small energy imbalance drives the systems farther from it: the equilibrium is unstable.

The figure below shows the temperature for the two systems as a function of the energy $U_{A}$ of the subsystem. 

![](images/Screenshot%202025-09-17%20at%202.37.53%20PM.png)
