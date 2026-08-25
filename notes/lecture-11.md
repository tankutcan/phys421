---
title: "Lecture 11"
---

## Reservoirs in Reversible and Irreversible Processes

In thinking of heat engines, we often make use of the idea of a reservoir: some gigantic system whose temperature does not really change in the process of transforming the working substance, which we may assume is an ideal gas. 

Consider two systems in thermal contact. Assume they are composed of the same material in the same phase. However, one system has $N_{1}$ molecules, and one has $N_{2}$ molecules, but with $N_{1}/N_{2} = r <<1$. They are initially at different temperatures $T_{1} < T_{2}$, and then placed in thermal contact. 
![](images/Screenshot%202025-10-09%20at%202.26.14%20PM.png)
**What is the final temperature?**

We know that in thermal equilibrium, $T_{1} = T_{2} = T$. Since the process is at constant volume

$\Delta U = Q = C_{V} \Delta T$

The heat absorbed by 1 is taken from 2. Use the fact that if the two systems are composed of the same material, the ratio of their heat capacities is proportional to the ratio of their system size: $C_{V}^{1} /C_{V}^{2} = N_{1}/N_{2} = r$ (for example, consider the case of an ideal gas, where $C_{V} = \frac{f}{2} N k$) 

$$
C_{V}^{1} \left( T - T_{1}\right) = C_{V}^{2} \left( T_{2} - T\right)
$$
Solving for $T$ gives

$$
T =  \frac{ T_{2} +r T_{1}}{1 + r} \approx T_{2} - r \left(T_{2} - T_{1}\right)
$$

The change in entropy of each system is

$$
\Delta S_{1} = \int \frac{C_{V} dT}{T} = C_{V}^{1} \ln \left( T/T_{1}\right)
$$

$$
\Delta S_{2} = \int \frac{C_{V}^{2} dT}{T} = C_{V}^{2} \ln \left( T/T_{2}\right)
$$
Next, using

$$
\frac{T}{T_{1}} = \frac{T_{2}}{T_{1}} - r \frac{\Delta T}{T_{1}}
$$

$$
\frac{T}{T_{2}} =1 - r \frac{\Delta T}{T_{2}}\\
$$
The total change in the entropy of this entire system becomes

$$
\Delta S = \Delta S_{1} + \Delta S_{2} = C_{V}^{1} \ln \left( \frac{T_{2}}{T_{1}}  \left( 1 - \frac{r \Delta T}{T_{2}}\right)\right) + C_{V}^{2} \ln \left( 1 - \frac{r \Delta T}{T_{2}}\right)
$$
$$
=  C_{V}^{1} \ln \left( T_{2}/T_{1}\right) + \left(C_{V}^{1} + C_{V}^{2}\right) \ln \left( 1 - \frac{r \Delta T}{T_{2}}\right)
$$
$$
=  C_{V}^{1} \ln \left( T_{2}/T_{1}\right) + C_{V}^{2} \left(1 +r\right) \ln \left( 1 - \frac{r \Delta T}{T_{2}}\right)
$$
For small $r$, I expand this
$$
\Delta S \approx C_{V}^{1} \ln (T_{2}/T_{1}) - C_{V}^{2} ( 1 + r)\frac{r \Delta T}{T_{2}}  =r  C_{V}^{2} \left(  \ln (T_{2}/T_{1})- (1 + r)  \Delta T/ T_{2}\right)
$$

Next, I will assume the fractional change in temperature is small, so that I can write

$$
\frac{T_{2}}{T_{1}} = \frac{T_{1} + \Delta T}{T_{1}} = 1 + \frac{\Delta T}{T_{1}}, \quad \ln \left( T_{2}/T_{1}\right) = \ln \left( 1 + \frac{\Delta T}{T_{1}}\right) \approx \frac{\Delta T}{T_{1}}
$$

Using this above, gives me the change in the total entropy

$$
\Delta S \approx r C_{V}^{2} \left(\frac{1}{T_{1}} - \frac{1}{T_{2}}\right) \Delta T = r C_{V}^{2} \frac{(\Delta T)^{2}}{T_{1} T_{2}}> 0
$$
When does the change in entropy vanish? Evidently in the limit $\Delta T \to 0$, when the difference in temperature between the system and the reservoir goes to zero. This is the definition of a reversible cycle. 

Takeaway: in order for a process to be **reversible** (i.e. $\Delta S = 0$) and have heat transfer, the heat transfer must happen at a constant temperature, i.e. there can be no temperature difference ($\Delta T = 0$)

Conversely, if heat is exchanged across a temperature difference, net entropy is generated, and the process is described as being **irreversible** (i.e. $\Delta S > 0$)


## Carnot's Theorem:

![](images/Screenshot%202025-10-09%20at%202.42.15%20PM.png)


The Carnot cycle (shown in on the P-V plane above) is the simplest reversible cycle. It operates between two temperatures, and only absorbs or loses heat along isotherms at these two temperature. To move between temperatures, it follows an adiabatic trajectory with $Q = 0$. 


To compute the efficiency, we need to be careful about keeping track of the direction in which heat is transferred. Along the $T_{h}$ isotherm, the gas absorbs heat. Let's call this $Q_{h}$. The total change in entropy along this trajectory is

$$\Delta S_{AB} = \int \frac{\bar{d} Q}{T_{h}} = \frac{1}{T_{h}} \int \bar{d} Q = \frac{Q_{h}}{T_{h}}$$
(Note: only use this formula for isothermal processes!)

The path $B\to C$ is adiabatic, which means $\Delta S_{BC} = 0$. Similarly, $\Delta S_{DA} = 0$. The process from $C \to D$ will lose heat. Let us denote the heat lost by the positive quantity $Q_{l}$, so that the change in entropy is

$$
\Delta S_{CD} = - \frac{Q_{l}}{T_{l}}
$$
Along this process, the gas is compressed, and therefore the entropy decreases. This explains the minus sign here. 

Since the cycle returns to the origin, the total change in entropy is zero. 

$$
\Delta S_{gas} = \Delta S_{AB} + \Delta S_{CD} = 0 = \frac{Q_{h}}{T_{h}} - \frac{Q_{l}}{T_{l}}
$$
Which gives the important relationship
$$
\frac{Q_{h}}{T_{h}}  = \frac{Q_{l}}{T_{l}}
$$

Next, we apply the first law to get the work done by the gas: $\Delta U = Q_{net} - W^{by\, gas}$, and using $\Delta U = 0$ for a cycle, and $Q_{net} = Q_{h} - Q_{l}$ as the net heat exchanged with the environment:

$$
W^{by \, gas} = Q_{h} - Q_{l}
$$

The efficiency of the cycle is defined by the work done by gas, divided by the total heat input, or absorbed, by the gas in the cycle. This is by definition:

$$
\eta = \frac{W^{by \, gas}}{Q_{in}}
$$

For the Carnot cycle, we get

$$
\eta_{C} = \frac{Q_{h} - Q_{l}}{Q_{h}} = 1 - \frac{Q_{l}}{Q_{h}} = 1 - \frac{T_{l}}{T_{h}}
$$

Beautiful!


### Irreversible Engines

What does the second law of thermodynamics imply about the efficiency of heat engines. The second law states that

$$
\Delta S = \Delta S_{gas} + \Delta S_{res} \ge 0
$$

Here $\Delta S_{gas}$ is the change in entropy of the working substance (which is an ideal gas in our case), and $\Delta S_{res}$ is the change in entropy of the reservoir. For a quasistatic process which is represented on the P-V diagram, $\Delta S_{gas} = 0$, so what's left is $\Delta S_{res} \ge 0$. 

Above, we compute the entropy change of the gas. 

$\Delta S_{gas}^{AB} = \frac{Q_{h}}{T_{h}}$

This means the entropy change of the reservoir is 

$\Delta S_{res}^{AB} = - \frac{Q_{h}}{T_{h}}$

Now there is some general process, which is not Carnot, which also operates between two reservoirs, and only draws heat from these reservoirs. These reservoirs are similarly held at $T_{h}$ and $T_{l}$. This means that if we describe the change in entropy of the reservoir, we can write this as $Q_{h}/T_{h}$ and $- Q_{l}/T_{l}$. Therefore, the sum of the entropy change of the reservoir is

$$\Delta S_{res} = - \frac{Q_{h}}{T_{h}} + \frac{Q_{l}}{T_{l}} \ge 0$$
This implies

$$
\frac{T_{l}}{T_{h}} \le \frac{Q_{l}}{Q_{h}} \Rightarrow \eta = 1 - \frac{Q_{l}}{Q_{h}} \le 1- \frac{T_{l}}{T_{h}} = \eta_{C}
$$
So the second law of thermodynamics implies that the Carnot efficiency is maximal. Below, we gives some alternative proofs of this same result. 



## Carnot, Kelvin, and Clausius Formulations of Second Law:

A note about the proof below. The Carnot engine efficiency is taken to be 

$$
\eta_{C} = \frac{W^{by \, system}}{Q_{h}} = 1 - \frac{T_{l}}{T_{h}}
$$

When the Carnot cycle is reversed, the work done by the system now becomes work done on the system. However, the ratio stays the same. For the reversed Carnot cycle in Fig. 13.4 of the excerpt below:

$$
\frac{W^{on\, system}}{Q_{h}} = \eta_{C} = 1 - \frac{T_{l}}{T_{h}}
$$
However, the reversed Carnot cycle is now acting as a refrigerator, which means the metric of performance is no longer the efficiency but the so-called coefficient of performance:

$$
\epsilon = \frac{Q_{l}}{W^{on \, system}}
$$
Just as the Carnot cycle gives the optimal efficiency for a heat engine, it will give the maximal coefficient of performance. Having fixed the identity above, we know that 

$$
W^{on \, system}+ Q_{l} = Q_{h}
$$
This implies

$$
\epsilon_{C} = \frac{Q_{l}}{Q_{h} - Q_{l}} = \frac{Q_{l}}{Q_{h}} \left(1 - \frac{Q_{l}}{Q_{h}}\right)^{-1}
$$
But note that $\eta_{C} = 1 - Q_{l}/Q_{h}$, which means we can write

$$
\epsilon_{C} = (1 - \eta_{C})/\eta_{C} = \eta_{C}^{-1} - 1
$$

From the textbook ***Blundell & Blundell, Ch. 13***:

![](images/Screenshot%202025-10-06%20at%204.07.24%20PM.png)




![](images/Screenshot%202025-10-06%20at%204.08.06%20PM.png)![](images/Screenshot%202025-10-06%20at%204.09.00%20PM.png)
