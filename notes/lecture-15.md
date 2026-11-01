---
title: "Lecture 15"
---

# Minimization of Free Energy

In general, the thermodynamic identities imply (for $dN = 0$), 

**Helmholtz Free energy** $F = U - TS$:
$$
dF = - P dV - S dT
$$
**Gibbs Free energy** G = U - TS + PV:
$$
dG = V dP - S dT
$$

So we get 

- $V, T$ constant: $dF = 0$
- $P, T$ constant: $dG = 0$

But this is for reversible processes. What about irreversible processes?

**Entropy**

$$
dS = \frac{1}{T} dU + \frac{P}{T} dV = \frac{1}{T} \left( \delta Q + \delta W^{on} + P dV\right)  \ge 0
$$

**Helmholtz:**
$$
dF = dU - T dS = \bar{d}Q + \delta W^{on} - T dS \le \delta W^{on}
$$
This tells us that in the absence of external work being done on a system, at constant $V$ and $T$ the Helmholtz free energy is minimized in equilibrium. 


**Gibbs**:

$$
dG  = dU - T dS + P dV = \delta  Q + \delta W^{on} - T dS + P dV \le 0
$$
This inequality says similarly that when pressure and temperature are held fixed, the Gibbs free energy is minimized in equilibrium. 


To get these inequalities, I used

$$
\frac{\delta Q}{T} \le   dS  \Rightarrow \delta Q - T dS \le 0
$$

These follow from the second law + first law. The fact that the Gibbs free energy is minimized is used in thinking about phase diagrams. 


# Phase Transformations

Phase Diagrams: P-T plane

A quite general phase diagram in P-T plane looks like the one for H20:


![](images/Screenshot%202025-10-20%20at%209.49.03%20PM.png)

What can we say about the shape of these curves? There is a very general relation that seems quite informative

## Clausius- Clapeyron Relation

Schroeder equates the Gibbs Free Energy at a phase boundary $G_{1} = G_{2}$, to derive the Clausius Clapeyron relation. There is another way to think about this, using Gibbs-Duhem (derive at the end of [Lecture 14](lecture-14.html)):

### Gibbs-Duhem Equation

There is an interesting relation which follows when we replace all the extensive variables with their conjugate intensive variables. Following the logic above, we should define a new thermodynamic potential

$\phi(T, P, \mu) = U - TS  + PV  - \mu N$

However, by the Euler relation Eq. (1), $\phi = 0$, and furthermore the differentials must be exactly zero. However, this implies a nontrivial relation connecting variations between intensive variables, called the [**Gibbs-Duhem equation**](https://en.wikipedia.org/wiki/Gibbs–Duhem_equation):

$$
- S dT + V dP - N d \mu = 0
$$

In equilibrium between two phases, one must have

$T_{1} = T_{2}$, $P_{1} = P_{2}$, and $\mu_{1} = \mu_{2}$. 

The Gibbs-Duhem equation tells us how differentials of these objects are related to each other. In particular, along a coexistence curve, one must have $d\mu_{1} = d\mu_{2}$. But then we can find a relation between the other intensive quantities. Since $d\mu_{1} =- \frac{S_{1}}{N_{1}} dT + \frac{V_{1}}{N_{1}} dP$, and similarly for $d\mu_{2}$, we get 

$$
d\mu_{1} = d\mu_{2} \Rightarrow - \bar{S}_{1} dT + \bar{V}_{1} dP = - \bar{S}_{2} dT + \bar{V}_{2} dP
$$

Where I have defined $\bar{S}_{1,2} = S_{1,2}/N_{1,2}$, and $\bar{V}_{1,2} = V_{1,2}/N_{1,2}$. Rearranging terms gives


$$
dP = \frac{\bar{S}_{1} - \bar{S}_{2}}{\bar{V}_{1} - \bar{V}_{2}} dT
$$
Or 
$$
\frac{dP}{dT} = \frac{\bar{S}_{1} - \bar{S}_{2}}{\bar{V}_{1} - \bar{V}_{2}}
$$


### Making Sense of Phase Diagrams:

Recall from [Lecture 14](lecture-14.html) that the Gibbs free energy satisfies

$$
\partial_{T} G = - S, \quad \partial_{P} G = V
$$

![](images/Screenshot%202025-10-21%20at%2010.49.22%20AM.png)

 What does the G vs P plot tell us about the different phases? It tells us that at low pressures, since graphite has lower Gibbs free energy, it is the stable phase of matter. At higher pressure, Diamond is more stable. This is due to the fact that Gibbs free energy is minimized in equilibrium. 


**Exercise:** How do we understand the low temperature phase between graphite and diamond?

![](images/Screenshot%202025-10-20%20at%209.48.34%20PM.png)
In this regime, the slope $dP/dT$ tends to zero, which implies either that the change in entropy tends to zero, or the change in volume tends to infinity. The latter is unlikely, so we must have that the change in entropy tends to zero. This is reasonable, in fact, because of the third law of thermodynamics, which postulates that entropy tends to a universal constant, independent of thermodynamic variables such as pressure, as temperature goes to zero. 


**Exercise:** (c.f. Schroeder 5.32a) Sketch the phase boundary between Ice and Water. What is the slope of this curve? What should it look like?


From *Schroeder Solution Manual:*
![](images/Screenshot%202025-10-20%20at%209.48.06%20PM.png)



**Exercise**: Sketch a graph of $G$ vs. $T$ for the three phases of H20 at atmospheric pressure.

*From Schroeder Solution Manual:*
![](images/Screenshot%202025-10-20%20at%2010.06.10%20PM.png)


## The Non-ideal Gas: Van der Waals

The Van der Waals model describes a gas with interactions


$$
\left( P + \frac{a N^{2}}{V^{2}}\right) \left( V - N b\right) = N k T
$$
This comes from a model of a gas in which each particle occupied a finite volume roughly $b$, and has inter-particle interactions controlled by $a$. If the particle volume is zero $b = 0$, and there are no interactions $a = 0$, then this equation of state reduces to the ideal gas law. 

The Van der Waals equation of state can be used to study the liquid to gas transition, as well as the tricritical point.
