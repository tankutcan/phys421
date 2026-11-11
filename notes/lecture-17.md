---
title: "Lecture 17"
---

# Equipartition Theorem

The Boltzmann distribution is plug and play. There are just two ingredients:

1) What are the energies of each configuration/state.
2) How do we count configurations

In certain examples with discrete variables, it is not ambiguous. Each configuration has an energy, and we just sum over all possible configurations

$$
Z = \sum_{s} e^{ - \beta E(s)}
$$

This is in fact all there is in a fully quantum treatment. In that case, each configuration is called a quantum state, and it is a discrete sum because energy is quantized. 

But we still get a lot from classical mechanics. Basically all that we learned about kinetic theory will come from classical thinking. 

Let's apply the Boltzmann distribution to a particle moving in space. The energy, which we know from classical mechanics, is kinetic plus potential:

$$
E = \frac{1}{2} m |{\bf v}|^{2} + U({\bf r}) = \frac{1}{2m} | {\bf p}|^{2} + U({\bf r})
$$
which can be expressed here in terms of momentum or velocity. 

We can define the partition function for this as well:

$$ Z = \sum_{{\bf r}, {\bf p}} e^{ - \beta E({\bf r}, {\bf p})}
$$
But obviously there is an issue with the sum - it is not discrete! Rather, we must replace the sum over configurations with an integral over the configuration, which in this case are the 3D (real-valued) position and momentum $({\bf r}, {\bf p})$. Therefore, the partition function should be written

$$
Z = \int d^{D} {\bf p} \, d^{D} {\bf r} e^{ - \beta E({\bf r}, {\bf p})}
$$
Next, we need to make this dimensionless, because the partition function is not supposed to have any dimensions. But each component of the integration measure $dp_{x} dr_{x}$ has units $[{\rm mass}] \times [ {\rm meters} ^{2}] / [ {\rm second}]$, which is incidentally the units of angular momentum, or what is called the action in classical mechanics (and path integral formulations of quantum mechanics). Therefore, we have to introduce a constant which has these units. The right choice turns out to be the Planck constant $h$. We couldn't have known this ahead of time, but comparing it with the fully quantum calculation (which is more complicated) confirms that this is the right choice. Since the integral is $D$ dimensional, we thus need a normalizing factor of $h^{D}$ to make this dimensionless. 


### Free Particle in a Box:


Let's start with the free particle in a box. $U = 0$ within a finite volume, and $U = \infty$ outside this volume. This will make the partition function


$$
Z =\frac{1}{h^{D}}\left( \int d^{D} {\bf x} \right) \left( \int d^{D} {\bf p} e^{ - \beta |{\bf p}|^{2}/2m}\right)
$$

The first term becomes just the volume $V$: $\int d^{D} {\bf x} = V$


The second term is more complicated, so let's spend some more time on it. The first thing to do is to rescale variables so that we make the $\beta$ and $m$ dependence completely explicit. This is accomplished by defining

$$
{\bf u} = \sqrt{\frac{\beta}{2m}} {\bf p}
$$
or in components

$$
u_{1} = \sqrt{\frac{\beta}{2m}} p_{1}, \quad u_{2} = \sqrt{\frac{\beta}{2m}} p_{2}, ...., u_{D} = \sqrt{\frac{\beta}{2m}} p_{D}
$$
(if it helps, just assume $D = 3$, consistent with your reality).

Then the integration measure becomes

$$
d^{D}{\bf p} = dp_{1} dp_{2}..., dp_{D} = \left( \sqrt{ \frac{2 m}{\beta}} du_{1}\right) ...\left( \sqrt{ \frac{2 m}{\beta}} du_{D}\right)  = \left( \frac{2m}{\beta}\right)^{D/2} d^{D}{\bf u}
$$

Using the result for the spatial integral, and using this change of variables, the partition function becomes


$$
Z = \frac{V}{h^{D}} \left( \frac{2 m}{\beta}\right)^{D/2} \left(\int d^{D}{\bf u} e^{ - | {\bf u}|^{2}}\right)
$$

The important thing to note here is that the integral in parentheses does not depend on any important physical variables - it is just a number! And in this particular instance, it is possible to evaluate, since it is a product of $D$ gaussian integrals:

$$
\int d^{D}{\bf u} e^{ - | {\bf u}|^{2}} = \int du_{1} e^{ - u_{1}^{2}} \int du_{2} e^{ - u_{2}^{2}} ... \int du_{D} e^{ - u_{D}^{2}} = \pi^{D/2}
$$
Since $\int_{-\infty}^{\infty} du e^{ - u^{2}} = \sqrt{\pi}$. 

So the single-particle partition function of a free particle in a box of volume $V$ is


$$
Z = \frac{V}{h^{D}} \left( \frac{2 m \pi}{\beta}\right)^{D/2} 
$$


From this, we are able to get the average energy of a single particle:

$$
\langle E \rangle = - \frac{\partial}{\partial \beta} \ln Z = \frac{D}{2} \frac{1}{\beta} = \frac{D}{2} k T
$$

Thus the particle has an average energy of $kT/2$ per dimension, which are the translational degrees of freedom. 


## Exercises:
### Particle in a Gravitational Field:
Consider the case of a particle confined to a box in the $x$ and $y$ directions, so that $0 \le x \le L$ and $0 \le y \le L$, but confined by a gravitational field in the $z$ direction. The gravitational potential energy is then $U =  m g z$, and $0 \le z \le \infty$. Let us find the average thermal energy of the particle in such a field. 

The partition function will factorize into separate spatial and momentum parts. Let's write this:

$$
Z(\beta) = Z_{p}(\beta) Z_{x}(\beta)
$$
Where

$$
Z_{x}(\beta) =\int dx dy dz e^{ - \beta m g z} = L^{2}\int_{0}^{\infty} dz e^{ - \beta m g z}
$$
I will rescale the integral (though I could also just evaluate it) to find the $\beta$ dependence. That is, after all, all I need to know to compute the average energy. Define $u = \beta m g z$. then $dz = du/(\beta m g)$, and 

$$
Z_{x}(\beta) = L^{2} \frac{1}{\beta m g} \int_{0}^{\infty} e^{ - u} du = \frac{1}{\beta} Z_{x}(1)
$$
If you didn't know how to evaluate this integral, it wouldn't matter. It is captured in the term $Z_{x}(1)$.  
Next, for the momentum part, we have from before

$$
Z_{p}(\beta) = \frac{1}{\beta^{D/2}} Z_{p}(1)
$$

Therefore combining these, we can write the partition function as

$$
Z(\beta) = \frac{1}{\beta^{D/2 + 1}} Z(1)
$$

and

$$
\ln Z(\beta) = - \left( \frac{D}{2} + 1\right) \ln \beta  + \ln Z(1)
$$

The average energy is

$$
\langle E \rangle = - \frac{\partial}{\partial \beta} \ln Z(\beta) = \left( \frac{D}{2} + 1\right) \frac{1}{\beta} = \left( \frac{D}{2} + 1\right) k T
$$


### Particle in Polynomial Potential (Anharmonic oscillator):
Consider now a 1D particle trapped in a potential $U(x) = a x^{n}$. What is the average thermal energy?


The partition function now is

$$
Z = \int \frac{d x dp}{h}  \exp \left( - \beta \left( \frac{p^{2}}{2m} + a x^{n}\right) \right) = \frac{1}{h} Z_{x}(\beta) Z_{p}(\beta)
$$
where

$$
Z_{x}(\beta) = \int_{-\infty}^{\infty} dx  \exp \left( - \beta a x^{n} \right), \quad Z_{p}(\beta) = \int_{-\infty}^{\infty} dp  \exp \left( - \beta \frac{p^{2}}{2m} \right)
$$

To extract the $\beta$ dependence of $Z_{x}$, we must define a new variable $X^{n} = \beta a x^{n}$, or $X = ( \beta a)^{1/n} x$, then $dx = \left( \beta a \right)^{-1/n} dX$ and 

$$
Z_{x}(\beta) = \int \frac{dX}{(\beta a)^{1/n}} e^{ - X^{n}} = \frac{1}{\beta^{1/n}} Z_{x}(1)
$$
It's anyone's guess how to evaluate this integral, but we know the important part, which is how it scales with $\beta$. Putting it together, I get


$$
Z(\beta) =  \frac{1}{\beta^{1/n + 1/2}} Z(1)
$$

And the average energy is

$$
\langle E \rangle = \left(\frac{1}{2} + \frac{1}{n} \right) k T
$$

Notice that we recover the equipartition result for quadratic degrees of freedom when $n = 2$. 


### Ultra-relativistic gas
If we have a relativistic dispersion in $D$ dimensions:

$$
E= c | {\bf p}|
$$
Find the equation of state in the form of a relation between pressure, volume, and total internal energy.

The partition function is


$$
Z = \int \frac{d^{D}{\bf p} d^{D} {\bf x}}{h^{D}} \exp \left( - \beta c p\right) = V \int \Omega(D) p^{D-1} dp e^{ - \beta c p} = V \Omega(D) \frac{1}{(\beta c)^{D}} \int du \, u^{D-1} e^{ - u}
$$

Which means
$$
Z_{1}(\beta) = \frac{1}{\beta^{D}} Z_{1}(1)
$$
and $Z_{N}(\beta) = \beta^{ - N D} Z_{N}(1)$

The average energy $U = \langle E \rangle$ is 

$$
U = - \partial_{\beta} \ln Z = - \partial_{\beta} \left( - DN \ln (\beta)\right) = DN k T
$$
Next, defining
$$
F = - k T \ln Z_{N}
$$

We get the pressure from 

$$
P = - \frac{\partial}{\partial V} F = \frac{Nk T}{V}
$$
So that 

$$
PV = N k T
$$
But we also know that $N k T = U/D$, so putting this together


$$
PV = \frac{1}{D} U
$$

The familiar result for an ultrarelativistic gas comes from setting $D = 3$.
