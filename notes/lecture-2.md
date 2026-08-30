---
title: "Lecture 2"
---

Quiz:
In flatland, particles exist in two-dimensions. Consider a gas in flatland. What is the average kinetic energy per particle of a gas at temperature $T$? 



In the previous lecture, I discussed the ideal gas law $PV = N kT$, discussed the fact that the temperature that appears in this equation is the absolute temperature, which reaches zero at about -273 C. Why should temperature have zero point? For a non-interacting gas of particles, it is connected to the fact that kinetic energy cannot be negative. Let's show this right now. 

### Microscopic description of Ideal Gas Law (Kinetic Theory)

What is the origin of pressure? This is in the book, and we get

$$
PV = N m \langle v_{x}^{2} \rangle
$$

From the ideal gas law, this implies
$$
KE_{x} = \frac{N}{2} k_{B} T
$$
We could have also repeated this analysis to compute the pressure on different walls. Doing so we will find that
$$
\langle KE_{x}\rangle = \langle KE_{y} \rangle = \langle KE_{z} \rangle = \frac{N}{2} k T
$$
In words, this tells us that the temperature (for a monatomic gas) is a measure of the average kinetic energy. For a gas, the interactions are weak, so in fact the kinetic energy is the total energy, which is known as the thermal energy or internal energy:
$$
U = \langle KE \rangle = \langle KE_{x} + KE_{y} + KE_{z}\rangle = \frac{3}{2} N k T
$$
This energy does not include binding energies of molecules, or rest energy of particles. This result is also a hint at a much deeper result known as the equipartition theorem. 

## Equipartition Theorem

The equipartition theorem tells us that every quadratic degree of freedom contributes $\frac{1}{2} k T$ to the internal energy. The easiest way to understand this is in terms of the Hamiltonian. For a free particle, the [Hamiltonian](https://en.wikipedia.org/wiki/Hamiltonian_mechanics#Hamiltonian) is just the kinetic energy:

$H = \frac{1}{2m} \left( p_{x}^{2} + p_{y}^{2} + p_{z}^{2}\right) \equiv \frac{1}{2m} || {\bf p}||^{2}$

For $N$ free particles (which is similar to a gas), the Hamiltonian is just the sum of kinetic energies:

$H = \frac{1}{2m} \sum_{i = 1}^{N} || {\bf p}_{i}||^{2}$

The quadratic degrees of freedom for this Hamiltonian are every component of the momentum. Each particle has $3$ components of momentum in 3D space, and so the total number of degrees of freedom is

d.o.f. = $3 \times N$. 

The equipartition theorem then says that the thermal energy is

$U = 3 N \times \frac{1}{2} k T$

If the gas consists of diatomic molecules, we must now also include a potential energy in the Hamiltonian. Assume that displacements are small, so that the interaction can be modeled by a linear spring-like force. Then the potential energy will be proportional to the displacement squared:

$V = \frac{k}{2} || {\bf x}_{1} - {\bf x}_{2}||^{2}$

This counts as 1 quadratic degree of freedom. In relative coordinates (assuming both particles are the same mass), ${\bf r} = {\bf x}_{1} - {\bf x}_{2}$, and $R = {\bf x}_{1} + {\bf x}_{2}$, the Hamiltonian (which is just the total energy, kinetic + potential)

$$
H = \frac{1}{2m} \left(|| {\bf p}_{1}||^{2} + || {\bf p}_{2}||^{2}\right) + \frac{k}{2} || {\bf x}_{1} - {\bf x}_{2}||^{2}
$$
Becomes

$$
H = \frac{1}{4m} || {\bf P}||^{2} + \frac{1}{ m} || {\bf p}||^{2}  + \frac{k}{2} r^{2}
$$

Counting *quadratic* degrees of freedom per molecule, we find $f = 3 + 3 + 1 = 7$.




***
## Exercises

### Applications of Ideal Gas Law

**Problem 1.10:** how many air molecules are in this room? What is the volume occupied by a single molecule?

*Solution:* The linear dimension of the room is maybe 5 meters, so the volume is $V \sim 10^{2} m^{3}$. The temperature is roughly $T = 300\, K$. And Boltzmann's constant is $6 \times 10^{-23} \, J/K$. $P \sim 10^{5}\, {\rm Pa}$, Then all together

$$ N = \frac{P V}{k_{B} T} = \frac{10^{5} \times 10^{2}}{18 \times 10^{2} \times 10^{-23}} \sim 10^{27}
$$
***


![](images/Screenshot%202025-09-02%20at%2012.09.25%20PM.png)
*Solution:*
Assuming there is no net air flow between the two rooms, the pressure in $A$ must be equal to the pressure in $B$. The problem also states that the volume is the same in each room. Therefore, the ideal gas law tells us that $P_{A} V_{A} = P_{B} V_{B}$ , and now substitute the RHS of the ideal gas law
$$
N_{A} T_{A} = N_{B} T_{B} \Rightarrow \frac{N_{B}}{N_{A}} = \frac{T_{A}}{T_{B}} > 1
$$
Which means $N_{A}< N_{B}$. So $B$ contains more molecules, and thus more mass. 

***

![](images/Pasted%20image%2020250831123852.png)
*Solution:*
By balancing forces  I find
$P(z+ dz) A + \rho_{m} A g dz = P(z) A$

Setting up a free body diagram, Then expanding $P(z + dz) = P(z) + dz P'(z) + O(dz^{2})$, I get

$$P'(z) =- \rho_{m} g \tag{1}$$

The issue here is that $\rho_{m}$ depends on $z$, precisely through its relation to $P(z)$. To determine this, we use the ideal gas law written for the number density $\rho$:

$P  = \rho k_{B} T$

the mass density is just $\rho_{m} = m \rho$. At this stage, we can do two things:

1) Find ODE for pressure. Substitute $\rho_{m} = m P/k T$, into (1)
$$
P'(z) = -\frac{m g}{k T} P(z)
$$
Which implies $P(z) \sim e^{ - m g z / k T} = e^{ - U_{g}/ k T}$ where $U_{g}$ is the gravitational potential energy. 

2) We can write $P = k T \rho_{m} / m$ and differentiation to get an ODE for the density

$$
\frac{k T}{m} \rho' =  -g \rho_{m} \Rightarrow \rho_{m}'(z) = - \frac{m g}{k T} \rho_{m}
$$

Which has the same functional dependence on height, $\rho_{m}(z) \sim e^{ - U_{g}/ kT}$ The 

***
### Counting Degrees of Freedom
![](images/Screenshot%202025-09-01%20at%2010.44.01%20PM.png)

*Solution:* The number of degrees of freedom per molecule: since there are three atoms in the molecule, and each has 3 momentum d.o.fs, this gives 9 degrees of freedom per molecule coming from kinetic energy. In addition to this, there is the potential energy of the interaction, which we model as springs between every pair of atoms. Therefore, a total of 3 degrees of freedom coming from potential energy. All together then $f = 12$.
