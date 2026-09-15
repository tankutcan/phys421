---
title: "Additional Problems"
---

# Chapters 1 - 3

### Problem 1

The black trajectory on the $P$–$V$ plane below shows a quasi-static thermodynamic cycle taken by an ideal gas. The arrows indicating the direction of the cycle are not included.

![](images/Exam%201%20Physics%20421%20-%20Figure%201.png)

**(a)** Draw arrows on the diagram indicating the direction in which the cycle must be taken for the gas to do net positive work.

**(b)** Find the net work done by the gas.

**(c)** Find the total amount of heat absorbed, $Q_{\mathrm{abs}}$, by the gas, and indicate the path or paths along which the gas absorbs this heat.

### Problem 2

A monatomic ideal gas expands to twice its initial volume through a quasi-static process in which the pressure is related to the volume by

$$
P = \alpha V^\alpha.
$$

What is the change in entropy of the gas during the process? You may assume that there are $N$ gas particles.

### Problem 3

An ideal gas is expanded from its initial state to a final volume $V$ without exchanging heat with its environment; the process is adiabatic. Consider two scenarios:

1. The gas undergoes free expansion.
2. The gas expands quasi-statically and reversibly.

Will the final pressure be different in these two scenarios? If so, after which process will the pressure be higher? Explain your reasoning. The answer does not depend on the details of the gas, such as whether it is monatomic or diatomic.


### Problem 4

A photon gas has the equation of state

$$
PV = \frac{1}{3}U
$$

and energy

$$
U = aVT^4.
$$

The entropy of the photon gas is given by

$$
S(V,T) = \gamma V^\alpha T^\beta.
$$

Find $\alpha$, $\beta$, and $\gamma$ using the thermodynamic identity and the fact that the chemical potential is zero.



### Problem 5

Consider a single particle in contact with a reservoir containing a very large number of particles. Two systems are placed in thermal contact:

**System A:** A collection of $N$ two-state particles. Each particle can occupy a state with energy $\epsilon_i \in \{0,1\}$. The macrostate is specified by the total energy $U$, and its multiplicity is $\Omega_A(U,N)$:

$$
U = \sum_{i=1}^N \epsilon_i,
\qquad
\Omega_A(U,N) = \binom{N}{U}.
$$

**System B:** A single two-state particle with energies $U_B \in \{-m,+m\}$, where $m$ is an integer.

**(a)** Both systems are prepared in isolation and then brought into thermal contact. System A initially has energy $U_A^{\mathrm{init}}=U_0$, while System B is initially in its ground state with energy $U_B^{\mathrm{init}}=-m$. The composite system has two possible macrostates, corresponding to the two states of System B. Specify $(U_A,U_B)$ for each macrostate and write down its multiplicity. Give exact answers without approximations.

**(b)** Show that, in the limit in which $U$ and $N$ are very large but $U/N \ll 1$, the logarithm of the multiplicity has the leading-order form

$$
\ln \Omega_A(U,N) \approx -U\ln\left(\frac{U}{N}\right).
$$

**(c)** The fundamental assumption of statistical mechanics states that all accessible microstates have equal probability. Therefore, the probability of each macrostate from Part (a) is proportional to its multiplicity. Using your answer from Part (a), the approximation from Part (b), and the assumption $m \ll U_0$, show that

$$
\frac{P_+}{P_-} = e^{\beta\Delta},
\qquad
\beta = \ln\left(\frac{U_0}{N}\right),
\qquad
\Delta = 2m,
$$

where the probabilities are labeled by the value of $U_B$. Which state of System B is more likely in this limit?

**(d)** What is the expected value of the energy of System B? Express the result in terms of $U_0$, $N$, and $m$. Sketch it as a function of $U_0$, the initial energy of System A. Use

$$
\langle U_B\rangle
= \sum_{(U_A,U_B)} U_B P(U_A,U_B)
= -mP_- + mP_+.
$$

**(e)** The preceding results are valid for $U_0/N \ll 1$. Now consider cases in which $U_0/N$ is not small, using the exact result from Part (a). For what value of $U_0$ is $\langle U_B\rangle$ exactly zero? Find $\langle U_B\rangle$ at $U_0=N$ in the limit of very large $N$.
