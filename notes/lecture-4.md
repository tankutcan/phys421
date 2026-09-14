---
title: "Lecture 4"
---

## Review so far:

- Ideal Gas law: $PV = N k T$ what are the physical assumptions that you need to believe this formula? 1) the gas particles are dilute and thus very weakly interacting. Otherwise they are classical. 
- Equipartition Theorem: $U = N_{dof} \times \frac{1}{2} k T$
- First Law (energy conservation): $\Delta U = Q + W$. Q is heat flow into the system, $W$ is work done ON the system. 
- If process is quasi-static, $W = - \int P dV$
- Heat Capacity


## Quiz:
a hot rock is thrown into a pool. The final temperature of the rock is pretty close to the pool. What can you say about the heat capacity of the pool wrt to the rock? Say it in words and equations.


## Heat Capacities

Recall again the definition of heat capacity. It is the ratio between the heat flow and the temperature change. 


$$
C = \frac{Q}{\Delta T} = \frac{\Delta U - W}{\Delta T}
$$

We also have to assume that there are no tricky nonlinearities, and that $C$ is constant. 

In the quiz, the heat flow out of the rock is the same as the heat flow into the pool. However, the final temperatures are different:

$$
Q = C_{rock} \left( T_{rock} - T_{f}\right), \quad Q = C_{pool} ( T_{f} - T_{pool}) ) 
$$
Solving this gives

$$
T_{f} = \frac{C_{rock} T_{rock} + C_{pool} T_{pool}}{C_{rock} + C_{pool}}
$$

If the pool doesn't really change in temperature, we get that $T_{f} \approx T_{pool}$. Plugging this in gives the following condition

$$
\frac{C_{rock}}{C_{rock} + C_{pool}} T_{f} \approx \frac{C_{rock}}{C_{rock} + C_{pool}} T_{rock}
$$
Since $T_{f} < T_{rock}$ by construction, the only way this squigglequality makes sense is if the coefficients are close to zero, i.e.

$$
\frac{C_{rock}}{C_{pool} + C_{rock}} \approx 0, \Rightarrow C_{pool} >> C_{rock}
$$
The pool is acting like a reservoir in this case. It's temperature is fixed, and being in contact with it brings you to its temperature. This is only possible because it has a very high heat capacity. Formally, such a fixed temperature thermal reservoir is said to have infinite heat capacity. 


### Ideal Gas Law 

The ideal gas law is known as an equation of state. An equation of state is an equation which relates the thermodynamic variables of a given substance. Typically we have variables like pressure, volume, number of particles, temperature (also chemical potential, and sometimes magnetization, etc.). Every system in equilibrium has a well defined set of thermodynamic variables which describe it completely. In other words, the **equilibrium state** is specified by a coordinate in the space of thermodynamic variables $(P, V, T, N, ...)$. The equation of state tells you what submanifolds in this space are possible - in other words, it tells you that some regions are not possible for a particular substance. For an ideal gas, the equation of state is the ideal gas law:

$$
PV = N k T
$$

For instance, this says that $PV/ NT$ cannot be arbitrary in an ideal gas. It is actually a constant (the Boltzmann constant). 


## PV diagrams

An ideal gas can be described by a limited number of thermodynamic variables: Pressure P, Volume V, temperature T, total number of particles N. This means if we specify these four variables (P, V, T, N), we have completely specified the state of an ideal gas. Since four dimensions is hard to visualize, usually we visualize the state of a thermal system on the P-V plane. Some alternatives we'll encounter later on are P-T (useful for describing phase transitions), and even S-T (i.e. entropy-temperature plane). To build intuition about processes in the P-V plane, I'll enumerate some particularly interesting/useful examples. Throughout I will assume that the gas does not lose particles or gain particles, so $N$ is constant. I will also always assume that the ideal gas law is true, $PV = N k T$. For concreteness, I'll assume all processes are quasi-static, and so every stage in the evolution can be represented as a point on the PV plane. I also consider only expansion. 


#### Constant Temperature
Isothermal process, which occurs at fixed temperature $T$. In this case, using the ideal gas law, we find that a quasi-static process which is isothermal will, by keeping temperature constant, change the pressure like $P \sim 1/V$. 

![](images/isothermal.png)

- Work: For a gas initially at $V_{0}$ that is expanded isothermally to $V_{f}$, the work done **by the gas** is
$$
W_{by\,\, gas} = \int_{V_{0}}^{V_{f}} P dV = N k T \int \frac{dV}{V} = N k T \ln\left( V_{f}/V_{0}\right)
$$

- The change in internal energy $\Delta U = 0$ because according to the equipartition theorem, $U = \frac{f}{2} N k T$, and if the temperature is held constant, the energy does not change
- Heat flow is obtained form the first law

$$
Q = \Delta U - W_{on \, \, gas} = W_{by \, \, gas} = N k T \ln \left( V_{f}/V_{0}\right)
$$

The gas does work to expand, and so loses energy. But the internal energy is forced to be held the same. To make up for the energy lost in the expansion, the gas must absorb heat from the environment. So $Q$ is positive. 



#### Constant Volume
This process occurs at fixed volume. Let's say the initial pressure is $P_{0}$, and the system increases in pressure to $P_{f} > P_{0}$. 
![](images/isochoric.png)


- Since there is no change in volume, the work done by the gas is zero, $W_{by \, \, gas} = 0$. 
- The change in internal energy is due entirely to the increase in pressure, which must have a higher final temperature. The ideal gas law tells us that at constant volume $T/P = {\rm const}$, so we can find the final temperature by

$$
\frac{T_{f}}{P_{f}} = \frac{T_{0}}{P_{0}} \Rightarrow T_{f} = \frac{P_{f}}{P_{0}} T_{0}
$$
And the change in internal energy is

$$
\Delta U = \frac{f}{2} N k \left( T_{f} - T_{0}\right) = \frac{f}{2} N k \left( \frac{P_{f}}{P_{0}} - 1\right) T_{0} = \frac{f}{2}  \left( \frac{P_{f}}{P_{0}} - 1\right) P_{0} V_{0} = \frac{f}{2} \left( P_{f} - P_{0}\right)V_{0}
$$

- The heat flow is equal to the change in internal energy, since work is zero. So $Q = \Delta U$. 

#### Constant Pressure

![](images/isobaric.png)

- The work done by the gas is particular easy to calculate, since the area under this curve is just the area of the rectangle of sides $P_{0}$ and $V_{f} - V_{0}$, therefore $W_{by \, gas} = P_{0} (V_{f} - V_{0})$
- The change in internal energy can be computed using equipartition $U = \frac{f}{2} N k T = \frac{f}{2} P V$, from which 
$$
\Delta U = \frac{f}{2} P_{0} (V_{f} - V_{0})
$$
- Finally, the heat flow into the gas is given by 
$$
Q = \Delta U - W_{on \, gas} = \Delta U + W_{by \, gas} = \left( \frac{f}{2} + 1\right) P_{0} (V_{f} - V_{0})
$$

### Exercise: PV process and First Law

Below are two paths denoted 1 and 2, which take the system reversibly from $A$ to $B$. Along which path does the **gas do more work**? Along with path does more heat flow into the system?

![](images/Screenshot%202025-09-25%20at%2011.47.07%20AM.png)

Since the area under the curve described by Path 1 is greater than the area under Path 2, the gas will do more work along Path 1. The change in internal energy between these two paths is the same. 


## First Appearance of Exact and Inexact Differentials

The first law has a differential form, and it's always a bit funny how it's presented. 

$$
dU = \delta Q + \delta W
$$

Is one common convention, although sometimes you'll find a $d$ with a bar through it. We can understand this by example. Let's assume the energy depends only on temperature $U(P,V)$. Then under an infinitesimal change in temperature, we have $dU = \partial_{P}U dP + \partial_{V} U dV$ Then upon integrating, since the integrand is an exact derivative, 

$$
\int_{T_{1}}^{T_{2}} dU = \int_{1}^{2} \nabla U  \cdot d{\bf x} = U(P_{2}, V_{2}) - U(P_{1}, V_{1})
$$
In other words, the integral of an exact differential is equal to the difference between the endpoints - it doesn't depend on the path. This is known as the [Gradient Theorem](https://en.wikipedia.org/wiki/Gradient_theorem).

In contrast, the work and heat cannot in general be written as exact forms. Instead, they have the form

$$
\delta Q = A(P,V) dP + B(P, V) dV, \quad \delta W = - P(V) dV
$$

To be an exact differential requires satisfying the following  would require $\partial_{V} A = \partial_{P} B$, which is generally not the case. However,if the coefficients come from a potential $\Phi$ such that $A = \partial_{P} \Phi$, and $B = \partial_{V} \Phi$, then this condition is automatically satisfied. Note also that in general $\partial_{V} P \neq 0$, which is why work is not an exact differential. 

The existence of an integrating factor prevents you from just evaluating the integral. In general, these integrals will depend on the trajectory. 



### Exercise: Adiabatic and Isothermal processes 

Two identical gases start initially at the same pressure and volume, and end at the same pressure. Assume one process is isothermal, and the other is adiabatic. Sketch these processes on a P-V diagram under two conditions: 1) the gases are compressed, and  2) the gases are expanded. What is the difference in final volume between the two gases in each of these scenarios? (c.f. Problem 1.38)


If the gases start at the same point on the PV diagram, then we have for compression:

$$
V_{f} = P_{0} V_{0}/P_{f} = \alpha V_{0}
$$
vs
$$
V_{f}^{\gamma} = \frac{P_{0} V_{0}^{\gamma}}{ P_{f}} \Rightarrow V_{f} = \alpha^{1/\gamma} V_{0}
$$

Now $\alpha < 1$. This means

$$
\alpha^{1 + \delta} < \alpha
$$
And since $\gamma >1$, we get $\alpha < \alpha^{1/\gamma}$, and therefore

$$
V_{f}^{t} < V_{f}^{a}
$$
If it's expansion, then $P_{f}< P_{0}$ and $\alpha > 1$. The inequalities flip, since $\alpha > 1$ and $\alpha^{\gamma} > \alpha$. 




### Exercise: Rising Bubbles:

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
