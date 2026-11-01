---
title: "Lecture 13"
---

# Recap:

In chapter 2, multiplicity was introduced, and so was entropy. Here the book shows that if we assume the postulate of stat mech, then we are given a new probabilistic law: systems tend to maximize their multiplicity. This is equivalent to the maximum entropy principle. It also implies that macroscopic systems (with many particles and thus many microstates) will not spontaneously move to systems with lower entropy. Therefore, the law is codified as the second law of thermodynamics:

$$
\Delta S \ge 0
$$
It furthermore gave us some conditions for equilibrium. If entropy is maximized at equilibrium, then if two systems are brought into contact then the total entropy is

$$
S_{AB}(U) = S_{A}(U_{A}) + S_{B}(U - U_{A})
$$
entropy is extensive, and it is additive for composite systems. This told us that a partial derivative wrt energy defines the intensive property that determines equilibrium. 

$$
T^{-1} = \partial_{U} S, 
$$

But we know from thermodynamics that it is precisely the temperature that defines thermal equilibrium. 

We can codify this in the thermodynamic identity

$$
dU = T dS - P dV
$$

This was all statistical mechanics, and we were using it to talk about thermodynamic systems. Well, we already have this huge theory of thermodynamics, and we should try to unite statistical mechanics with thermodynamics. 

The first example was in giving an entropic definition of heat. This comes directly from the first law

$$
dU = \delta Q + \delta W \Rightarrow \delta Q = T dS
$$
This gives a stat mech interpretation of heat - it is related to the change in entropy (but it's not an exact differential form because of the so-called integrating factor $T$)


## Practice Problem 1

$n$ reservoirs with the same heat capacity at different temperatures $T_{i}$ for i = 1, ..., n are all placed in contact and come to equilibrium. What does the first law imply about the final temperature? What does the second law imply?

From the first law, we know that the energy is conserved. The heat flow from reservoir $i$ is

$$
Q_{i} = C \Delta T_{i} = C ( T_{f} - T_{i})
$$
There is not external work or heat flow into the system, so 

$$
\sum_{i} Q_{i} = 0
$$
Which implies
$$
\sum_{i} C ( T_{f} - T_{i}) = 0 \Rightarrow n C T_{f} = C \sum_{i} T_{i}
$$
The LHS of the second equation follows because thermal equilibrium means all final temperatures are the same. In final form, we see that the final temperature is the arithmetic mean of all of the initial temperature. 

$$
T_{f} = \frac{1}{n} \sum_{i=1}^{n} T_{i}
$$

The change in entropy of each reservoir is bounded by the quasistatic result


$$
\Delta S_{i}= \int \frac{\delta Q}{T} = \int_{T_{i}}^{T_{f}} \frac{C dT}{T} = C \ln (T_{f}/T_{i})
$$
The total entropy of the collection of reservoirs is then bounded from below by

$$
\Delta S = \sum_{i} \Delta S_{i} = \sum_{i = 1}^{n} C \ln (T_{f}/T_{i}) = n C \ln T_{f} - C \sum_{i} \ln T_{i}
$$

Next, using the property of the logarithm that $\ln x + \ln y = \ln (x y)$, I get

$$
\Delta S = C \ln T_{f}^{n} - C \ln \left( \prod_{i = 1}^{n} T_{i}\right)
$$


The second law implies $\Delta S \ge 0$, which implies 

$$
T_{f}^{n} \ge \prod_{i = 1}^{n} T_{i}
$$
Next, using the explicit form of $T_{f}$, we have the interesting consequence

$$
\frac{1}{n} \sum_{i = 1}^{n} T_{i} \ge \left( \prod_{i = 1}^{n} T_{i}\right)^{1/n}
$$

The LHS is the arithmetic mean, the RHS is the geometric mean. The inequality we have derived using the first and second law of thermodynamics ends up being a familiar inequality between arithmetic and geometric means.



## Practice Problem 2

Two reservoirs with heat capacity $C_{h}$ and $C_{l}$ are at temperatures $T_{h}$ and $T_{l}$. A Carnot engine is hooked up between them, and is allowed to run until the reservoirs are at the same temperature. What will the final temperature be?

The infinitesimal heat transferred by a cycle of the engine from each reservoir is
$$
\delta Q_{h} = -C_{h} dT_{h}
$$
and
$$
\delta Q_{l} = C_{l} dT_{l}
$$
Since it is Carnot, the efficiency constrains the relation between these quantities:
$$
\eta = 1 - \frac{T_{l}}{T_{h}} = \frac{\delta W}{\delta Q_{h}}
$$
$$
\delta Q_{h} = \delta W + \delta Q_{l} = \eta \delta Q_{h} + \delta Q_{l}
$$

Together these imply
$$
\frac{T_{l}}{T_{h}} \delta Q_{h} = \delta Q_{l}
$$
Using the explicit forms of the differentials of heat then gives:
$$
-\frac{C_{h} dT_{h}}{T_{h}} = \frac{C_{l} dT_{l}}{T_{l}}
$$
$$
C_{h}\ln T_{h}/T = C_{l} \ln T/T_{l} 
$$

Solving for the final temperature $T$ gives:
$$
\ln T = \frac{C_{h} \ln T_{h} + C_{l} \ln T_{l}}{C_{h} + C_{l}}
$$


If you just let the two reservoirs relax to equilibrium, the final temperature will be:
$$
T_{relax} = \frac{C_{h} T_{h} + C_{l} T_{l}}{C_{h} + C_{l}}
$$

Then using the weighted arithmetic mean-geometric mean inequality $w_{1} x_{1} + w_{2} x_{2} \ge x_{1}^{w_{1}} x_{2}^{w_{2}}$, for $w_{1}, w_{2}>0$, $w_{1} + w_{2} = 1$, implies that the final temperature $T < T_{relax}$. 


### Motivating the Helmholtz Free Energy: $F = U - TS$

Replacing $S$ with $T$ gives the Helmholtz Free energy:

$F(T, V, N) = U - TS$,  which satisfies the identity

$dF = dU - T dS - S dT = - P dV + \mu dN - S dT$

Partial derivative relations imply
$$
\left(\frac{\partial F}{\partial T}\right)_{V, N} = -S, \quad \left( \frac{\partial F}{\partial V}\right)_{T, N} = - P
$$
The first relation implies we can determine the internal energy from $F$ using only derivatives wrt temperature:

$U = F - T \partial_{T} F = - T^{2} \partial_{T} \left( F/T\right)_{V}$

If you know $F(T, V, N)$, you can extract the internal energy. In this sense, F is called a thermodynamic potential (analogous to electric or gravitational potential)

From Schroeder:

![](images/Screenshot%202026-10-21%20at%209.27.01%20AM.png)
