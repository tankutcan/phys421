---
title: "Exam 1 Review"
---

# Lightning Summary of Material So Far

## Microscopic and Macroscopic

Statistical mechanics requires distinguishing microscopic variables from macroscopic variables. The essential simplification that statistical mechanics offers is a drastic reduction in the state space of a system. In this class, we have called the state space coordinates sometimes macrostates, sometimes thermodynamic variables. They depend on the setting:


- **Typical Materials:** For a gas or liquid, some typical macroscopic variables, thermodynamic coordinates, state variables, are: volume, number/density, pressure, temperature, energy, chemical potentail
- **Magnets:** Given the few examples of magnets we have seen, we know also that magnetic systems have another macroscopic variables, which is the total magnetization or magnetization density. 


## Fundamental Assumption of Statistical Mechanics

I will focus on an ideal dilute gas because it is easiest to understand. For an ideal gas with $f$ degrees of freedom per particle, we have:

**Equation of state:**
$$
P V = N k T \quad (1)
$$
**Equipartition of energy:**

$$
U = \frac{f}{2} N k T \quad (2)
$$

These are macroscopic laws; they tell us how macroscopic coordinates are related. The **macrostate** of a gas is given by a tuple of all the macroscopic coordinates that describe that gas. We have the **extensive** variables $(U, S, N, V)$, and the intensive variables $(P, T, \mu)$.  So the macrostate of an ideal gas is defined by a definite value for each of these seven variables. 

### Possible macrostates

The equations (1) and (2) impose constraints which relate thermodynamic variables. This means not all points in the state space are accessible. The thermodynamic identity gives a further constraint about transformations:

$$
dU = T dS - P dV + \mu dN
$$
which tells you how displacements from a given equilibrium point must be related. 


## Counting Microstates

The fundamental assumption states that all accessible microstates for a fixed macroscopic configuration have equal probability of obtaining. This just means we fix the macroscopic coordinates, and count all the possible microscopic configuration that produce this macrostate. 



### First Law of Thermodynamics: Energy Conservation

In finite difference form, if a system is begins and ends in equilibriumyou should in principle specify a process. So let's say that during some process, which begins and ends in equilibrium, the
$$
\Delta U = Q + W^{on\,  gas}
$$
Here $Q$ is the total heat flow *into* the system, and $W$ is the work done *on the system*. I spoke in class about the differential form of this law:

$$
dU = \bar{d} Q + \bar{d} W^{o.g.}
$$
(N.B. This is non-standard notation. I could not figure out how to do the d with a slash through it) 
$dU$ represents an exact differential, whereas $\bar{d}Q$ and $\bar{d}W$ are inexact differentials. Work and heat are the only objects you've come across so far whose differential form are inexact differentials. 

The important thing to remember is that for exact differentials, the integral along a path connecting points $A$ and $B$ is equal to the difference between the endpoints

$\int_{A}^{B} dU = U(B) - U(A)$

For inexact differentials like $\bar{d}Q$ and $\bar{d}W$, the value of the integral depends on the path.



### Second Law: Entropy and Multiplicity

The multiplicity of a system is the number of possible configurations which have fixed certain macroscopic variables. In all cases we have considered, the multiplicity is a function of three state variables: Energy U, number of particles $N$, and volume $V$ (thought not always *all* of them)

$$
\Omega(U, V, N)
$$
The entropy is then similarly a function of $U$, $V$, and $N$:

$$
\boxed{S(U, V, N)= k \ln \Omega(U, V, N)}
$$


Some examples we have studied:
- Ideal Gas: it is found that $\Omega(U, V, N) = f(N) V^{N} U^{f N/2}$
- Einstein Solid: with it's an idealized model, so volume doesn't really figure into it. $\Omega(U, N) = \left( { N - 1 + U/\epsilon \atop U/\epsilon} \right)$ (the book uses $q = U/ \epsilon$ as the integer counting energy units)
- Paramagnet: here again, volume isn't relevant. $\Omega(U, N) = \left( { N \atop - U/\mu B} \right)$ 

( N. B. These equations for multiplicity for each of these systems are not essential to memorize for the exam. )




### Thermodynamic Identity

This follows directly from the fact that entropy is a function of $U$, $V$, and $N$:

$$
dS = S(U + dU, V + dV, N + dN) - S(U, V, N)  =  \left( \frac{\partial S}{\partial U}\right)_{V,N} dU +  \left( \frac{\partial S}{\partial V}\right)_{U,N} dV +  \left( \frac{\partial S}{\partial N}\right)_{U,V} dN
$$
Identifying
$$
\frac{1}{T} = \left( \frac{\partial S}{\partial U}\right)_{V,N} , \quad \frac{P}{T} = \left( \frac{\partial S}{\partial V}\right)_{U,N} , \quad  - \frac{\mu}{T} = \left( \frac{\partial S}{\partial N}\right)_{U,V} 
$$
and rearranging terms, leads to the fundamental thermodynamic identity

$$
\boxed{dU = T dS - P dV + \mu dN}
$$
all of the differentials here are exact differentials of state variables. This identity tells you how infinitesimal changes in $U$, $S$, $V$ and $N$ are related. 



### Entropy and Heat

The thermodynamic identity is always true, and the first law is always true. For a **reversible** process, the work is given by $\bar{d}W^{o.g.} = - P dV$. Assuming $dN = 0$, we can then identify

$$
dS = \frac{\delta Q}{T}
$$
This is true for reversible processes. Integrating along a reversible path we get

$\Delta S = \int_{A}^{B} dS = \int_{A}^{B} \frac{\delta Q}{T}$




### Heat Capacity

The heat capacity is a useful quantity to define. It is the constant of proportionality relating the heat flow to a temperature difference: 

$$
Q = C \Delta T  \tag{1}
$$
There are two important specifications, which are the heat capacity at fixed volume and fixed pressure. They have the following expressions

$$
C_{V} = \left( \frac{\partial U}{\partial T}\right)_{V}, \quad C_{P} = \left( \frac{\partial U}{\partial T}\right)_{P} + P \left( \frac{\partial V}{\partial T}\right)_{P} \tag{2}
$$
These follow from (1) by applying the First Law and taking the limit $\Delta T \to 0$ . You can treat them as definitions for $C_{V}$ and $C_{P}$. They can be combined with the thermodynamic identity for some additional useful relations. The following should be viewed as consequences of these definitions and the thermodynamic identity:

- If we fix pressure, then the thermodynamic identity implies $dU = T dS - P dV$, which can be rearranged to $dS = \frac{1}{T} \left( dU + P dV\right)$, But note, the definition of $C_{P}$ implies that in differential form: $dU + P dV = C_{P} dT$, therefore:  $dS = C_{P}\, dT/T$ (see Schroeder Eq. 3.50)
- If we fix volume and number, the thermodynamic identity implies $dU = T dS$, and from the definition of $C_{V}$, we get in differential form: $dU = C_{V} dT = T dS$, so we get $C_{V} = T \left( \partial S/\partial T \right)_{V}$ (see Schroeder problem 3.33)

To review, Eqs. $(1)$ is a definition, whereas the following are consequences:
$$
C_{V} = T \left( \frac{\partial S}{\partial T}\right)_{V}, \quad C_{P} = T \left( \frac{\partial S}{\partial T}\right)_{P}
$$



### Kinetic Theory

**Equipartition theorem:** Kinetic theory relates macroscopic behavior to microscopic properties. In particular, we learned about the equipartition theorem, which states that every quadratic degree of freedom contributes $\frac{1}{2} k T$ to the total thermal energy. The total number of degrees of freedoms:
- Monatomic gas: f = 3, all translational 
- Diatomic gas: f = 7, 3 translational, 2 rotational, 2 vibrational
- Einstein Solid: f = 6, 3 independent simple harmonic oscillators, so $3\times 2$ vibrational degrees of freedom
The total internal (thermal) energy is given by:
$$
U = \frac{f}{2} N kT
$$
**Ideal Gas Law**: This we saw was a consequence of kinetic theory (Schroeder Sec. 1.2)

$$
PV = N k T = n R T
$$



### Mathematical Tools:
There are a few basic mathematical tools you should be familiar with:

 **Stirling Approximation**: most correctly it is understood as an asymptotic expansion of $\ln N!$ for large $N$:

$$
\ln N! = N \ln N - N + \frac{1}{2} \ln N + \frac{1}{2} \ln (2\pi) + O(1/N)
$$
Notice that in this expansion, each term is smaller than the preceding term. 


**Properties of logarithm**: the following properties are essential features of a logarithm

$$
\ln\left( x y\right) = \ln x + \ln y
$$
From this, a few useful properties follow: 

$$
\ln \left( x^{n}\right) = n \ln x, \quad \ln 
$$

Next, we also have the taylor expansion of $\ln(1 + x)$ for small $x$:
$$
\ln\left(1 + x\right) = x - \frac{x^{2}}{2} + O(x^{3})
$$

**Combinatorics:** The counting problems we've encountered so far are the following:
- Enumerating how many ways there are to choose a subset of $M$ items from a set of $N$, given by the binomial coefficient $\left( { N \atop M}\right)$, sometimes pronounced "N choose M". This is relevant for the paramagnet. 
- How many ways are there to pick $N$ numbers, some of which can be zero, such that their total sum is $q$. This is given by $\left( { N - 1 + q \atop q}\right)$, and is relevant for the Einstein solid. 



# Problem Solving

In class, we solved some problems from [Additional Problems](additional-problems.html). These solutions appear on this page now. 

The other problems we discussed had to do with the Stirling approximation.
