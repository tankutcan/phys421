---
title: "Lecture 18"
---

# Question: 
what is the average velocity and speed at constant temperature $T$? Use the boltzmann distribution and assume a collection of non-interacting particles in a box of volume $V$. 


Use this to derive the maxwell distribution. We will use a few important concepts from probability to derive this. First, let's denote the full joint probability for a configuration of particles 

$$
P({\bf r}_{1}, ..., {\bf r}_{N}, {\bf p}_{1}, ..., {\bf p}_{N}) = \frac{1}{Z} \exp \left( - \beta \sum_{i = 1}^{N} E({\bf r}_{i}, {\bf p}_{i})\right)$$

For shorthand, I will call this $P( \{ {\bf r}_{i}, {\bf p}_{i}\})$

The one-particle distribution is defined as

$$
P_{1}({\bf r}, {\bf p}) = \int \prod_{i = 2}^{N} d^{3} {\bf r}_{i} d^{3} {\bf p}_{i} P( {\bf r}, {\bf r}_{2}, ..., {\bf r}_{N}, {\bf p}, {\bf p}_{2}, ..., {\bf p}_{N})
$$
Notice that all I'm doing is integrating over every particle with index $1$, and setting the position and momentum of that particle to ${\bf r}$ and ${\bf p}$. This is occasionally called "integrating out" all particles but one, or in probability "marginalizing out" all other particles. The result is a probability for observing a single particle in the system at position and momentum ${\bf r}, {\bf p}$. 

Time to be more precise with language. If we take a snapshot of a gas, we will have $N$ velocities. The average velocity of the particles at this instant in time is

$$
{\bf v}_{ave} = \frac{1}{N} \sum_{i = 1}^{N} {\bf v}_{i} = \frac{1}{m} \frac{1}{N} \sum_{i = 1}^{N} {\bf p}_{i}
$$

If we look at the average velocity at a different time point, we will get a different answer. In general, the average velocity will behave like a random variable, and the Boltzmann distribution is supposed to tell us what the distribution of this random variable is. Similarly, if we want to get the expected value of this random variable, we must calculate it using the probability distribution defined by the Boltzmann distribution. 

$$
\langle {\bf v}_{ave} \rangle = \int \prod_{i = 1}^{N} d^{3} {\bf r}_{i} d^{3} {\bf p}_{i} \, \left( \frac{1}{m} \frac{1}{N} \sum_{k=1}^{N} {\bf p}_{k}\right) P(\{ {\bf r}_{i}, {\bf p}_{i}\})
$$

This is just the rule for how to calculate expectation values given a probability distribution. Now, we can simplify this. First, note that because the expectation value is a linear functional of its argument, we can write the expected value of the sum of terms as the sum of expected values. 



$$
\langle {\bf v}_{ave} \rangle = \frac{1}{m} \frac{1}{N} \sum_{k} \int \left(\prod_{i = 1}^{N} d^{3} {\bf r}_{i} d^{3} {\bf p}_{i}\right) \,\Big({\bf p}_{k}\Big) P(\{ {\bf r}_{i}, {\bf p}_{i}\})
$$

Next, let me evaluate the sum over $k$ one term at a time. I'll start with $k = 1$, let

$$
\langle {\bf v}_{ave} \rangle = \frac{1}{m} \frac{1}{N} \sum_{k} I_{k}
$$
where

$$
I_{k} = \int \left(\prod_{i = 1}^{N}  d^{3} {\bf r}_{i} d^{3} {\bf p}_{i}\right) \,\Big({\bf p}_{k}\Big) P(\{ {\bf r}_{i}, {\bf p}_{i}\})
$$
Starting with $k = 1$. If we integrate everything but ${\bf p}_{1}$, I can use the one-particle probability to rewrite this term

$$
I_{1} = \int d^{3} {\bf r}_{1} d^{3} {\bf p}_{1} \,\,{\bf p}_{1} \left( \prod_{i = 2}^{N} d^{3} {\bf r}_{i} d^{3} {\bf p}_{i} P(\{ {\bf r}_{i}, {\bf p}_{i}\})\right)  = \int d^{3} {\bf r}_{1} d^{3} {\bf p}_{1} \,\,{\bf p}_{1}  P_{1}({\bf r}_{1}, {\bf p}_{1})
$$

Next, I claim that we will end up with the same equation for $I_{2}$ becase the probability is invariant under permutations of particle index. In other words, if we exchange $1 \leftrightarrow 2$, the probability doesn't change. 
$$
P({\bf r}_{1}, {\bf r}_{2}, ...., {\bf p}_{1}, {\bf p}_{2}, ....) = P({\bf r}_{2}, {\bf r}_{1}, ...., {\bf p}_{2}, {\bf p}_{1}, ....)
$$

This will imply that $I_{2} = I_{1}$. And the same argument implies that all $I_{k}$ are equal. Therefore, 

$$
\langle {\bf v}_{ave} \rangle = \frac{1}{m} I_{1}
$$
Let's take stock. In this problem, I started with the goal of calculated the expected value of the average velocity. The average velocity is a simple function of the momenta of the particles, in particular

$$
{\bf v}_{ave} = \frac{1}{m} \frac{1}{N}\sum_{i = 1}^{N} {\bf p}_{i}
$$
Taking the average, I found that I could write it like

$$
\langle {\bf v}_{ave} \rangle = \frac{1}{m} \frac{1}{N}\sum_{i = 1}^{N} \langle {\bf p}_{i}\rangle = \frac{1}{m} \langle {\bf p}_{1}\rangle 
$$
Note that $\langle {\bf p}_{1}\rangle = I_{1}$, which I can express using a single-particle probability


$$
\langle {\bf p}_{1}\rangle = \int d^{3} {\bf r}_{1} d^{3} {\bf p}_{1} \, {\bf p}_{1}\, P_{1}({\bf r}_{1}, {\bf p}_{1})
$$

Now, since the integrand doesn't depend on ${\bf r}_{1}$, I can simply integrate that out and define a new function called the momentum distribution function

$$
Q({\bf p}) = \int d^{3} {\bf r} P_{1}({\bf r}, {\bf p})
$$

My result above about the expectation value of ${\bf p}_{1}$ actually tells me something more general. If ever I want to calculate the expectation value (wrt the Boltzmann distribution) of the average value of some observable of the momentum $F({\bf p})$, I could write it

$$
\left\langle \frac{1}{N} \sum_{i = 1}^{N}F({\bf p}_{i}) \right\rangle  = \int d^{3} {\bf p}\, F({\bf p}) \, Q({\bf p})
$$

The momentum distribution function tells me how the single-particle momenta are distributed in the gas. Let us now evaluate it for the ideal gas limit. In this case, we have the total energy

$$
E = \sum_{i = 1}^{N} \left( \frac{| {\bf p}_{i}|^{2}}{2m} + U({\bf r}_{i})\right)
$$
Here $U = 0$ inside a region of volume $V$, and is infinite outside this region. This allows us to easily integrate each position variable to get a factor of $V$. Let's now try to evaluate the single-particle probability

$$
P_{1}({\bf r}, {\bf p}) = \frac{1}{Z} \int \prod_{i = 2}^{N} d^{3} {\bf r}_{i} d^{3} {\bf p}_{i} \, e^{ - \beta |{\bf p}|^{2}/2m} \prod_{k = 2}^{N} e^{ - \beta |{\bf p}_{k}|^{2}/2m} = \mathcal{C} e^{ - \beta |{\bf p}|^{2}/2m}
$$
Where I have introduced a constant 

$$
\mathcal{C} = \frac{1}{Z} \left( V \int d^{3} {\bf p} \, e^{ - \beta |{\bf p}|^{2}/2m}\right)^{N-1}
$$
We want $P_{1}({\bf r}, {\bf p})$ to be normalized correctly, 

$$
1 = \int d^{3} {\bf r} d^{3} {\bf p} P_{1}({\bf r}, {\bf p})  = \mathcal{C}V \int d^{3} {\bf p} e^{- \beta |{\bf p}|^{2}/2m} = \mathcal{C} V \left( 2 \pi m /\beta\right)^{3/2}
$$
Therefore

$$
\mathcal{C} = \frac{1}{V (2\pi m/\beta)^{3/2}}
$$
And the exact value of the probability is

$$
P_{1}({\bf r}, {\bf p}) = \frac{e^{ - \beta |{\bf p}|^{2}/2m}}{V (2\pi m /\beta)^{3/2}}
$$

To get the momentum distribution function, we just integrate over position,

$$
Q( {\bf p}) = \frac{e^{ - \beta |{\bf p}|^{2}/2m}}{ (2\pi m /\beta)^{3/2}}
$$

Let's proceed now to make a connection to the Maxwell distribution. This emerges if we care about understanding the distribution of particle speeds. For instance, assume the observable is the average speed

$$
v_{ave} = \frac{1}{N} \sum_{i} | {\bf v}_{i}| = \frac{1}{N} \sum_{i} \frac{1}{m} |{\bf p}_{i}|
$$
Then what matters is the norm of the momentum, and we need to calculate

$$
\langle | {\bf p}| \rangle = \int d^{3} {\bf p} \, | {\bf p}| Q({\bf p})
$$

Since we only care about the norm, we can integrate out the other degrees of freedom, which are the angular degrees of freedom that determine orientation. To do this, we go to spherical coordinates, in which case

$$
d^{3} {\bf p} = dp_{x} dp_{y} dp_{z} = p^{2} dp \sin (\theta) d\theta d\phi
$$
Which will make the integral

$$
\langle p \rangle = \int p^{2} dp \sin(\theta) d\theta d\phi \,   \frac{e^{ - \beta p^{2}/2m}}{(2\pi m/\beta)^{3/2}} \, p = \int_{0}^{\infty} dp \,\, p\, \, \mathcal{D}(p)
$$

Where I have introduced a new object

$$
\mathcal{D}(p) = \frac{4\pi}{(2\pi m/\beta)^{3/2}} p^{2} e^{ - \beta p^{2}/2m}
$$


Notice that

$$
\int_{0}^{\infty} dp \mathcal{D}(p) = 1
$$
Indeed, $\mathcal{D}(p)$ represents a probability distribution, giving the probability observing a particle with a momentum of magnitude $p$. This can be converted quite simply to the distribution over particle speeds using $p = mv$ and transforming the Jacobian $dp = m dv$,

$$
\int dp \mathcal{D}(p) = \int m dv \mathcal{D}(m v) \equiv \int dv \, \mathcal{\tilde{D}}(v)
$$
where 
$$
\mathcal{\tilde{D}}(v) = m \mathcal{D}(m v) = \frac{4\pi m^{3}}{(2\pi m/\beta)^{3/2}} v^{2} e^{ - \beta m v^{2}/2}
$$
which is the Maxwell distribution for particle speeds. 

We can use this as an alternative route to the equipartition theorem. Let us calculate the average kinetic energy per particle

$$
\langle \frac{1}{N} \sum_{i= 1}^{N} \frac{1}{2} m v_{i}^{2}\rangle = \frac{m}{2} \int_{0}^{\infty} dv \, v^{2} \mathcal{\tilde{D}}(v) = \frac{m}{2} \frac{4\pi m^{3}}{(2 \pi m k_{B} T)^{3/2}}  \int dv \, v^{4} e^{ - \beta m v^{2}/2}
$$

We are encountering a tricky integral. Let's use tricks to solve it. First, note that under a change of variables, $x = \sqrt{ \beta m/2} v$, it becomes

$$
 \int_{0}^{\infty} dv \, v^{4} e^{ - \beta m v^{2}/2} = \left( \frac{2}{\beta m} \right)^{5/2}\int_{0}^{\infty}  dx \, x^{4} e^{ - x^{2}}
$$

Next, to get a handle on the remaining integral, I will use the following fact. 

$$
\int_{0}^{\infty} dx \, e^{ - a x^{2}} = \frac{1}{2}\frac{1}{\sqrt{a}} \sqrt{\pi}
$$
This is the usual change of variable trick, combined with the fact that $\int_{-\infty}^{\infty} dx e^{ - x^{2}} = 2 \int_{0}^{\infty} dx e^{ - x^{2}}$ by symmetry of the integrand. But notice now that if i differentiate both sides wrt $a$, I get

$$
\frac{\partial}{\partial a} \int dx e^{ - a x^{2}} = -   \int \, dx \, x^{2} e^{- a x^{2}}
$$
And if I do it again

$$
\frac{\partial^{2}}{\partial a^{2} } \int dx \, e^{ - a x^{2}} = \int dx \,x^{4}\,  e^{ - a x^{2}} 
$$

using the exact value of this integral, I get

$$
\frac{\partial^{2}}{\partial a^{2} } \int dx \, e^{ - a x^{2}} = \frac{\partial^{2}}{\partial a^{2} } \frac{1}{2}\sqrt{\pi} a^{ - 1/2} = \frac{\partial}{\partial a} \left( - \frac{1}{4} \sqrt{\pi} a^{ - 3/2}\right) = \frac{3}{8} \sqrt{\pi} a^{ - 5/2}
$$
Therefore

$$
\int dx\, x^{4} e^{ - a x^{2} } = \frac{3}{8} \sqrt{\pi } a^{ - 5/2}
$$

We ultimately wanted $\int dx \, x^{4} e^{ - x^{2}}$, which we can now get by setting $a = 1$. Going back to our integral, we find


$$
 \int dv \, v^{4} e^{ - \beta m v^{2}/2} = \left( \frac{2}{\beta m} \right)^{5/2} \frac{3}{8} \sqrt{\pi}
$$
Therefore, the average kinetic energy per particle is

$$
KE/N = \frac{m}{2} \frac{4\pi m^{3}}{(2 \pi m k_{B} T)^{3/2}}  \left( 2 k_{B} T/m\right)^{5/2} \frac{3}{8} \sqrt{\pi} = \frac{3\sqrt{\pi}}{8} \left(2\pi m^{4} \right)\frac{2 k_{B} T}{m}  \left( \frac{1}{\pi m^{2}}\right)^{3/2} = \frac{3}{2} k_{B} T
$$
Which is precisely the equipartition result, giving $3$ translational degrees of freedom per particle, and each d.o.f. contributing $k_{B} T / 2$ average KE. 


## Many Identical Particles

When we are dealing with classical systems, we must be careful with many particle systems. The difficulty comes mainly from the position space integral, and how to correctly count distinct configurations. The resolution is not entirely convincing, but ends up being the correct prescription: Compute the partition function for $N$ particles in the obvious way, i.e.

$$
Z_{N} = \int \prod_{i= 1}^{N} \frac{d^{3}{\bf x}_{i}d^{3} {\bf p}_{i}}{h^{3}} \exp \left( - \beta \sum_{i = 1}^{N} E({\bf x}_{i}, {\bf p}_{i}) \right)
$$
The total energy is a sum of single-particle energies because the particles do not interact. Since the exponent is just a sum of single-particle terms, the partition function will factorize, and we get

$$
Z_{N} = Z_{1}^{N}
$$

However, this will have overcounted the distinct spatial configurations, for the following reason: if two spatial configurations of particles are related by permutation of the particle's index, then these are counted as distinct configurations. However, for indistinguishable particles, these should not be separate. The particle index has no meaning - it is just a mathematical trick to keep track of variables. Therefore, we must divide by the number of possible permutations, which is $N!$. So the partition function of $N$ classical indistinguishable particles is

$$
Z_{N} = \frac{1}{N!} Z_{1}^{N}
$$

This slick reasoning will be unnecessary for quantum partition functions. 


### Ideal Gas - Classical
The partition function for an ideal gas will be


$$
Z_{N} = \frac{V^{N}}{N!} \left( \frac{\sqrt{2 \pi k mT}}{ h}\right)^{3 N}
$$

In the book, we learn about the quantum volume, which is just a definition:

$$
v_{Q} = \left( \frac{h}{\sqrt{2\pi m k T}} \right)^{3}
$$

Therefore our partition function becomes

$$
Z_{N} = \frac{V^{N}}{v_{Q}^{N}} \frac{1}{N!}
$$


From this, we can get the relevant properties using the Helmholtz free energy:


$$
F = - k T \ln Z_{N} = - k T \left( N \ln V - N \ln v_{Q} - \ln N!\right)
$$

In particular, the ideal gas law:

$$
P = - \left(\frac{\partial F}{\partial V}\right)_{T,N} = \frac{N k T}{V}
$$

Also, using

$\ln v_{Q} = - \frac{3}{2} \ln k T = \frac{3}{2} \ln \beta$, we get the average energy

$$
U = - \partial_{\beta} \ln Z_{N} = \partial_{\beta} \left( \frac{3}{2} N \ln \beta \right) = \frac{3}{2} N k T
$$
