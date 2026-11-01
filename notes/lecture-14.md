---
title: "Lecture 14"
---

# Extensive and Intensive Properties


**Intensive**: state variable that is independent of system size. These are the variables that determine equilibrium between two bodies:
- Temperature T -  two systems share a temperature when they are in thermal equilibrium, regardless of their size and composition
- Pressure P - two systems are in mechanical equilibrium (forces are balanced) when they have same pressure. 
- Chemical Potential $\mu$ - determines diffusive equilibrium


**Extensive**: state variable that grows with system size, keeping intensive variables fixed. Examples include: 
- Internal Energy U
- Entropy S
- Volume V
- Number of Particles N


## Natural Variables

Just recalling the thermodynamic identity:
$$
dU = T dS - P dV + \mu dN
$$

This relation implies that the natural coordinates for the energy are $S, V, N$, i.e. changes in internal energy $dU$ are related to changes in entropy, volume, and number. All of the arguments are extensive. So we may write $U = U(S, V, N)$, i.e. the internal energy as a function of $S$, $V$ and $N$. 

## Euler Relation

A particularly interesting identity comes from considering how extensive properties change with system size. 

Let us consider changing $S \to \lambda S$, $V \to \lambda V$ and $N \to \lambda N$, $U \to \lambda U$. As we observed from the thermodynamic, the internal energy is a natural function of these extensive variables, so it depends on $S$, $V$, and $N$. However, since $U$ is also extensive, as a result of this transformation of all extensive variables, $U$ will also transform like all of the other extensive variables, $U \to \lambda U$. Writing this as an equation, we get:

$U(\lambda S, \lambda V, \lambda N) = \lambda U(S, V, N)$

Differentiating both sides then setting $\lambda = 1$, we get

$$
U = \left( \frac{\partial U}{\partial S}\right)_{V,N} S + \left( \frac{\partial U}{\partial V}\right)_{S,N} V +\left( \frac{\partial U}{\partial N}\right)_{S,V} N 
$$
From the thermodynamic identity, we get the partial derivative relations

$$
T =  \left( \frac{\partial U}{\partial S}\right)_{V,N} , \quad - P = \left( \frac{\partial U}{\partial V}\right)_{S,N} , \quad \mu = \left( \frac{\partial U}{\partial N}\right)_{S,V} 
$$

Therefore, we arrive at the very handy and remarkable Euler relation for thermodynamics: 

$$
U = T S - P V + \mu N \tag{1}
$$




# Thermodynamic Potentials

## Legendre Transformation

It is sometimes not convenient to work with purely extensive dependent variables. $U$ depends naturally on extensive variables. This motivates the question: is there a thermodynamic state function that depends naturally on different variables? How do we even change variables? 

This is what the **Legendre transformation** is for. 

Take a function $f(x)$ that depends on $x$. Its differential is given by
$$
df = \left( \frac{\partial f}{\partial x}\right) dx
$$
We can define $p = \partial_{x} f$, and define a new function $g = x p - f$. Then differentials of $g$ are 

 $dg = x dp + p dx - p dx = x dp$
So $dg$ is naturally a variable of $p$. 

(N.B. This comes up in classical mechanics, when we want to go from lagrangian to hamiltonian: $H(x, p) = \dot{x} p - L(x, \dot{x})$, with $p = \partial_{\dot{x}} L$ )

So it is possible to change variables by redefining the function. But we cannot do it willy-nilly. Each extensive variable has a natural partner (conjugate) intensive variable:

$S \to T$
$V \to P$
$N \to \mu$

So we can take a function of $S$ and convert it to a function of $T$. Similarly with $V$ and $P$, and $N$ and $\mu$. 

## Energy

We start with the energy, and the conventional thermodynamic identity

$U = U(S, V, N)$,  $dU = TdS - P dV + \mu dN$

I will use the notation $\Phi(S, V, N)$ to denote a function $\Phi$ of the variables $S, V, N$. 


## Enthalpy: $H = U + PV$

If we replace volume with pressure, we get the enthalpy:

$H(S, P, N) =  U  + PV$  

The differential of enthalpy then satisfies a new thermodynamic identity:

$dH  = dU + P dV + V dP = T dS + V dP + \mu dN$

To get the second equality, just substitute the conventional thermodynamic identity to cancel $P dV$. 



## Gibbs Free Energy: $G = U - TS + PV$

Replacing both $S$ and $V$ with their intensive conjugate variables ends up giving the Gibbs Free energy:

$G = \Phi(T, P, N) = U - TS + PV$  which satisfies the differential identity:

$dG = dU - T dS - S dT + P dV + V dP + \mu dN=- S dT +V dP + \mu dN$

A few partial derivative relations that will be useful later on come directly from this:

$$
S = - \left( \frac{\partial G}{\partial T}\right)_{P,N}, \quad V = \left( \frac{\partial G}{\partial P}\right)_{T, N}
$$

Notice that if we use the Euler relation Eq. (1), it implies the Gibbs free energy is directly proportional to the number of particles:

$$ G = \mu N$$


## Grand Potential: $\Phi = U - TS - \mu N$

We now consider replacing $S \to T$, $N \to \mu$. This produces the Grand potential:

$\Phi(T, V, \mu) = U - TS - \mu N$ 

which satisfies

$d\Phi = - S dT - N d\mu - P dV$

Notice again that using the Euler relation Eq. (1) implies: $\Phi = -PV$

See problem 5.23 in Schroeder for more on this thermodynamic potential.


### Gibbs-Duhem Equation

There is an interesting relation which follows when we replace all the extensive variables with their conjugate intensive variables. Following the logic above, we should define a new thermodynamic potential

$\phi(T, P, \mu) = U - TS  + PV  - \mu N$

However, by the Euler relation Eq. (1), $\phi = 0$, and furthermore the differentials must be exactly zero. However, this implies a nontrivial relation connecting variations between intensive variables, called the [**Gibbs-Duhem equation**](https://en.wikipedia.org/wiki/Gibbs–Duhem_equation):

$$
- S dT + V dP - N d \mu = 0
$$
