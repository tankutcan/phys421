---
title: "Lecture 3"
---

Quiz:
A gas is compressed to half its volume at constant pressure, slowly such that it remains in equilibrium the entire time. Sketch this on a PV diagram. 

## Review of the Basic Equations so far


#### Ideal Gas Law (equation of state):

$$
PV = N k T
$$

#### Equipartition theorem for an ideal gas:

$$U = \frac{f N}{2} k T = \frac{f}{2} PV$$

For non-interacting particles, the internal energy (aka thermal energy) is the average kinetic energy that gives rise to the temperature measurements. The binding energy of nuclei, the rest energy of electrons, etc., doesn't contribute to thermal energy in the energy ranges that matter for classical thermodynamics. They are said to be "frozen out". Rotational and vibrational motion of molecules also doesn't matter at all temperatures - they are only relevant at very high temperatures. 

Factoid:
The RHIC has created quark-gluon plasma at approx. $4 \times 10^{12}$ Celsius. Measured by wavelength of emitted light. 

## State Variables

We have discussed the ideal gas law, and in this lecture we will discuss the first law of thermodynamics, which is the equation for energy conservation. Very importantly, in understanding the first law, it's crucial to keep track of state variables. 

A state variable is just what I described as macroscopic or thermodynamic variables in the first lecture. They are the small number of variables that we believe completely describe a thermodynamic system in equilibrium. From the ideal gas, we get a few: pressure, temperature, volume. Equipartition tells us also that internal energy $U$ is a state variable. Anticipating future developments, we can also mention that entropy is a state variable.

## Heat and Work

In this lecture, we'll cover the first law of thermodynamics, which is summarized in the equation:
$$\Delta U = Q + W$$
This is a simple statement of the conservation of energy for thermal systems. Internal energy $U$ is a **state variable**, which an equilibrium system. However, heat flow $Q$ and work $W$ are not state variables. They do not describe a state a system is not, but rather a process that the system undergoes. 

$W$ is the work done *on the system*. The way I remember this is that if there is work done on the system, that's like squeezing it. And when I squeeze e.g. a stress ball, it gets hot, so the internal energy goes up. 

Q is the total heat flow into the system. If heat flow is positive ($Q>0$), then the energy increases. If heat flow $Q<0$, then energy decreases 

For this reason, the book uses the confusing notation that on the LHS there is a $\Delta$, while on the RHS there is no $\Delta$. This is to remind you that the state variable $U$ changes via non-state-variable process variables $W$ and $Q$. 

## Irreversible Expansion into Vacuum

A thermally insulated box is partitioned into two regions. The left region is filled with gas and in equilibrium, the right region is empty. At some time t = 0, the partition is opened and the gas expands into the full volume. How much a) Work is done by the gas, 2) heat is exchanged, and 3) thermal energy change?

![](images/Screenshot%202025-09-04%20at%2011.58.29%20AM.png)
*Solution:* $W = Q = 0$, and by the first law, $\Delta U = 0$, which means the temperature is unchanged. 

from *Fermi's Thermodynamics*:
![](images/Screenshot%202025-09-04%20at%2012.09.57%20PM.png)

#### State space and PV diagrams

Every point on a PV diagram describes the complete state of a gas, if we are also given the total number of molecules $N$ and the type of molecules (degrees of freedom). For $PV = N k T$ if $N$ does not change, then there are only two independent variables governing the state of the gas. So we can represent the state on a P-V diagram. A curve on the P-V plane represents a reversible process

In classical mechanics, the state of a system is described completely by its momentum and position. Sometimes this space is called [phase space](https://en.wikipedia.org/wiki/Phase_space). Here is an example:

![](images/Screenshot%202025-09-03%20at%206.04.45%20PM.png)
$x^{2} + p^{2} = constant$ is just the Harmonic oscillator. In units more familiar, $H = \frac{1}{2m} p^{2} + \frac{1}{2} m \omega x^{2}$ . At a fixed energy (which is a conserved quantity after all, and thus stays constant throughout the motion), the simple harmonic oscillator exchanges energy between the kinetic and potential energy. In phase space, it traces an oval (or a circle in appropriate coordinates). 


## Heat Capacities

The heat capacity is defined

$$
C = \frac{Q}{\Delta T} = \frac{\Delta U - W}{\Delta T}
$$

For this reason, there are some important conditions. 

If work is zero:

$$ C_{V} = \left( \frac{\partial U}{\partial T}\right)_{V}$$
Otherwise, if pressure is constant:

$$ C_{P} = \left( \frac{\partial U}{\partial T} \right)_{P} + P \left( \frac{\partial V}{\partial T}\right)_{P}$$

The first part is the same for both

$U = \frac{f}{2} nR T$  so that $C_{V} = \frac{f}{2} n R$

For an ideal gas, we have

$V = \frac{n R T}{P}$, so that 

$$
C_{P} = C_{V} + n R = \left(\frac{f}{2} + 1\right) n R 
$$
This means that

$$
\gamma \equiv C_{P}/C_{V} = 1 + \frac{n R}{C_{V}}  = \frac{f + 2}{f}
$$


$U = C_{V} T$ by definition. Classical physics predicts that $C_{V}$ is independent of temperature. But it depends!


### Revisiting equipartition

Vibrational modes are simple harmonic oscillators, $H_{vib} = p^{2} + x^{2}$, and so each mode has two degrees of freedom. 

Thus for diatomic molecules, we saw above that $f = 7$. Three of these degrees of freedom we can account for with the center of mass momentum. That leaves 4. Two of these we can account for by the vibrational degrees of freedom, since the vibrational mode is a simple harmonic oscillator. What's left are 2 degrees of freedom that must be due to rotational degrees of freedom. Quantum mechanics will tell us that these modes have different energies, and thus come into play at different temperatures, as seen in the plot of the heat capacity from Schroeder (reproduced below)

![](images/Screenshot%202025-09-02%20at%205.11.19%20PM.png)


# Exercises
***

### Practice with PV diagrams:
![](images/Screenshot%202025-09-02%20at%204.25.23%20PM.png)

*Solution:*

**A** The gas does positive work, so the work done ON the gas is negative. Temperature increases, so the energy goes up. This is accomplishes by heat going INTO the system: W < 0, Q, U > 0
**B** No work is done, the temperature increases, so both $\Delta U = Q > 0$
**C** Work is done ON the gas, $W > 0$.  The temperature decreases so that $\Delta U < 0$. In order to make $\Delta U < 0$ with positive work done on the gas, we have have heat leaving system $Q < 0$. 

Overall, the total work done BY THE GAS is negative $W_{tot} < 0$, so that the total work done ON THE GAS is positive $W > 0$.  since $\Delta U_{tot} = 0$, we must have $Q < 0$. Net heat flows OUT OF the system. Maybe this is a fridge.
 
***
### Rising Bubbles:

![](images/Pasted%20image%2020250902164728.png)
*Solution:*

For bubble A, the total change in internal energy is given by the work done. Therefore $\Delta U = - |W|$. 

For bubble $B$, which stays in thermal equilibrium, the temperature remains constant, so that all the work done by the bubble in expanding is converted to heat $W = Q$. This is heat flowing into the bubble. 

For the bubble B, $P V = N k T$, we have that $PV = {\rm constant}$ in the bubble, so that the volume grows inversely as the pressure decreases. For bubble A, the temperature changes with the pressure and volume. We have that

$dU = - P dV$

**Checking Signs:** If the gas DOES positive work, $PdV > 0$, i.e. it is expanding and doing work on its environment (e.g. lifting a piston). If its doing positive work, and there is no heat flow (adiabatic expansion), then the change in internal energy must be negative. Hence $dU = - P dV$. 


 $$
 dU = \frac{f}{2} N k d T = -P dV =  \frac{N k T}{V} dV
 $$
Rearranging, I get
$$
\frac{f}{2} \frac{d T}{T} = -\frac{d V}{V}
\Rightarrow \frac{f}{2} \log T = -\log V
$$

Or
$V T^{f/2} = {\rm constant}$

This means that
$$
\frac{PV}{T} = \frac{P V}{V^{-2/f}}  = P V^{1 + 2/f}= {\rm constant}
$$

This is the crucial equation. For bubble $A$, we get

Bubble A: $P V^{1 + 2/f} = {\rm constant}$

Bubble B: $P V = {\rm constant}$

The ratio of these is constant. Since the pressure is the same, we get

$\frac{V_{A}^{1 + 2/f}}{V_{B}} = {\rm constant}$. 

If they start at the same volume, then after rising, bubble $A$ will be larger. $V \sim 1/P$ vs. $V \sim 1/P^{f/(2 + f)}$ 

***

### Equation of State of a Photon Gas

In this problem, we will write down the equation of state of a gas of weakly interacting photons. In cosmology, this serves as a model for an ultrarelativistic gas. We cannot apply kinetic theory for particles and the equipartition theorem to write the average internal energy in terms of temperature. But we can get a relation between pressure, volume, and energy, essentially using only Newton's Laws and a few facts from relativity.

a) To begin, assume a single photon is in a container with linear dimension $L$, and elastically reflects off of the walls. Show that the magnitude of the change in momentum after reflection from a single wall is
$$
\Big| \Delta {\bf p} \cdot {\bf n} \Big| = 2 \Big|({\bf p} \cdot {\bf n}) \Big| 
$$
Where ${\bf n}$ is the vector perpendicular to the wall.

***Solution:***

Reflection from the wall satisfies the property that the angle of incidence is equal to the angle of reflection. So that the initial momentum ${\bf p}_{i}\cdot {\bf n} = -| {\bf p}_{i}| \cos(\theta)$ , and the final momentum ${\bf p}_{f} \cdot {\bf n} = | {\bf p}_{f}| \cos\theta$, (the angles are the same). Furthermore, for an elastic collision, $| {\bf p}_{i}| = | {\bf p}_{f}| = |{\bf p}|$ . Therefore, the change in momentum is

$$
\left({\bf p}_{f} - {\bf p}_{i} \right) \cdot {\bf n} = 2 | {\bf p}| \cos(\theta) = 2 | {\bf p} \cdot {\bf n}|
$$


b) Show that the time between reflections is just the time to travel across the box (compare this to Schroeder Eq. 1.10 ):
$$
\Delta t = \frac{2 L}{\Big| {\bf v} \cdot {\bf n}\Big|}
$$
***Solution:***
The time to travel across the box is twice the linear dimension (which is the total distance traveled), divided by the average speed along this direction. The numerator gives just twice this linear dimension, whereas the denominator is just the speed along the relevant direction. 


c) Now use Newton's second law $F = \Delta p / \Delta t$ to find the magnitude of the average force exerted on the wall. 

***Solution:***
The magnitude of the force is 

$$
F = \frac{\Big| \Delta {\bf p} \Big |}{\Delta t} = \frac{2 |{\bf p} \cdot {\bf n}| | {\bf v} \cdot {\bf n}|}{2L}
$$



d) To get this in final form, note that ${\bf n}$ is arbitrary, which means this equation is true for any orientation of ${\bf n}$. Use this fact to argue that we can write the average force as

$$
F_{ave} = \frac{1}{L}  \frac{1}{3} \langle {\bf p} \cdot {\bf v} \rangle
$$

***Solution:***

We can select ${\bf n} = \hat{x}$, i.e. the unit vector in the (arbitrarily chosen) x direction. Then

$$
|{\bf p} \cdot {\bf n}| | {\bf v} \cdot {\bf n}| = p_{x} v_{x}
$$

But since this is arbitrary, we can easily choose ${\bf n} = \hat{y}$ or $\hat{z}$. All of these will be equivalent. Therefore, 

$$
|{\bf p} \cdot {\bf n}| | {\bf v} \cdot {\bf n}| = \frac{1}{3} \left( p_{x} v_{x} + p_{y} v_{y} + p_{z} v_{z}\right) = \frac{1}{3} {\bf p} \cdot {\bf v}
$$

Averaging this quantity gives the expression for the average force.


e) Use this result for the average force exerted by a single photon on the container, to show that the pressure for a gas of $N$ photons in a container with volume $V$ is
$$
P = \frac{N}{V}  \frac{1}{3} \langle {\bf p} \cdot {\bf v}\rangle  
$$

***Solution:***

To get pressure for $N$ photons, we use $P = N F_{ave}/A$, and note that $V = A L$. 


f) The velocity of a photon always points in the same direction as its momentum. Since the velocity is the speed of light $| {\bf v}| = c$, and the energy of a single photon is $E = p c$, show that the equation of state is:
$$
P V = \frac{1}{3}U
$$
Compare this to an ideal gas with $f$ degrees of freedom. Does the photon gas equation of state also reflect the degrees of freedom of photons? 

***Solution:***

Since velocity is the speed of light, and is co-linear with momentum, we get

$$
{\bf p} \cdot {\bf v} = p c
$$

Next, using the relation between momentum and energy per photon, I get

$$
PV = \frac{N}{3} \langle {\bf p} \cdot {\bf v}\rangle = \frac{N}{3} \langle E\rangle  = \frac{1}{3} U
$$
Where the internal energy is just $N$ times the average energy per photon. 



There is also a nice discussion of this in *Feynman's lecture*:

![](images/Screenshot%202025-09-02%20at%209.15.09%20AM.png)
