---
title: "Lecture 1"
---

### Quiz: 
Math:
Find
$$
I(a) = \int_{-\infty}^{\infty} dx \, e^{ - a x^{2}}
$$
given $I(1) = \sqrt{\pi}$

Physics:
What is entropy?



Welcome to thermodynamics and statistical mechanics! I wonder what you expect to learn in this course? 

I will try to have class be a combination of lectures and problem solving. Since everything I can possibly do in class, you can probably access somewhere else (via AI, online lectures, peers, solution sets, etc.), I think it will be most useful if you come to class with questions. For this, it makes most sense to read the book beforehand. I understand this isn't always possible as the semester charges forth leaving you behind. But 


Thermodynamics is a very old topic. It concerns the flow of heat, and the conversion of heat to work. It is important for engineering. If you want to build electronic circuits, you'll need to understand heat flow and heat exchange. Probably anyone with a heavy duty computer understands that their machine will heat up, and it needs some mechanism to cool down. Thermodynamics is a very practical topic. However, it was by studying the practical problems of steam engines that a french civil servant, Sadi Carnot, discovered a fundamental law limiting the efficiency of steam engines. He did this by abstracting the problem away from the particular substance or device, and found that the maximum efficiency achievable by a engine operating between two reservoirs is

$\eta_{max} = 1 - \frac{T_{cold}}{T_{hot}}$

 In fact, as we'll see later, this was an incarnation of the second law of thermodynamics, one of the most fundamental, fascinating, and mysterious laws in physics. Some might have seen it in this form
$$
\Delta S_{universe} \ge  0
$$
which says that the entropy of the universe never decreases. We'll learn what entropy means in this course, and we'll learn about the second law of thermodynamics. And ultimately we'll see how Carnot's result is connected to the second law. 

These join other fundamental laws you might already be familiar with: newton's laws of motion, maxwell's equations for electrodynamics. What else? Plenty of other laws. the undergraduate physics curriculum is like law school. Once you're with it long enough though, you realize it's more anarchistic. 

Thermodynamics is the source of a fundamental law of physics, and yet it deals with quantities which do not seem fundamental. For example, what is heat? what is temperature? what is pressure? We like to think that the fundamental stuff is particles, perhaps atoms. Water consists of molecules of H20, air has a mixture of diatomic molecules. A molecule is not hot, a molecule does not have a temperature, a molecule does not exert a pressure. 

The gap i'm point out here is between microscopic (fundamental seeming) physics (like particles moving according to newton's laws), and macroscopic variables like temperature, pressure, chemical potential. 

This gap is bridged by statistical mechanics. Statistical mechanics a theory which tells us how to predict macroscopic variables from microscopic configurations of particles. 

The thing is, thermodynamics can actually be made logically self-contained and consistent, a theory in its own right. In this course, we prefer to think about statistical mechanics as the fundamental theory and thermodynamics as a consequence. 



### Pedagogical Example:
For example, let's say I have a room full of $10^{23}$ molecules bouncing off the walls, and I suddenly double the size of the room. What will happen? There are two levels of description for this system

### Microscopic:
Write down the position and velocity (or momentum) $({\bf r}_{i}, {\bf v}_{i})$ of every single particle. They all interact $V({\bf r}_{i}, {\bf r}_{j}) = 1/| {\bf r}_{i} - {\bf r}_{j}|$ Their acceleration is $d {\bf v}_{i}/dt = F_{net}/m_{i}$ Now solve this. If you have the initial conditions, you can integrate this and find all future configurations of the particles. Does that help you?

### Macroscopic:
Measure the temperature, pressure, volume, and use the ideal gas law

$$
P V = N k T
$$


In the macroscopic view, you lose a lot of information. But you are dealing with variables you can 1) measure and 2) predict .


Therefore, by coarse graining, you lose some information but you gain predictability. The goal of the course will be to understand where these macroscopic variables come. 



### Equilibrium

To begin thinking about thermodynamics, we need to understand equilibrium. I think it's a more or less intuitive concept, which it is possible to make precise. 


Throw an ice pack into a bucket of water. Sketch the temperature of the ice vs time, and the temperature of the water as a function of time. 





Both objects will asymptotically reach the same temperature. After this, there is no more change. Equilibrium is a state in which there no change. That means time derivatives are zero. But it's important to specify which quantities stop changing. For a thermodynamic system like a gas of many many particles, the quantities which change are things like pressure, temperature. Therefore, when we say thermodynamic equilibrium, we meet that these quantities are no longer changing in time. For the purposes of this class, it also means they are not changing in space. For a particular system, enclosed in a volume, equilibrium means there is a well-defined temperature everywhere in the system that is not changing with time. 


Temperature can be posited axiomatically. This is the content of the zeroth law. 

The **zeroth law of thermodynamics** was formulated as an axiom which allows us to define an equivalence relation between thermodynamic systems according to their temperature. 

Temperature can also be defined via statistical mechanics. Soon you will understand the following formula for temperature

$$
\frac{1}{T} = \frac{\partial S}{\partial E}, \quad S = \ln \Omega(E)
$$
where the entropy is the logarithm of the number of microstates at energy $E$. Under this picture, temperature is measuring how many configurations are available to a system. 


There is a smallest temperature for macroscopic many-particle systems. The ideal gas law

$$
PV = N k T
$$
Let's fix volume and measure pressure as we heat up a container of air. We'll see the following behavior, which extrapolates to zero pressure at something like - 273.15 C. This is the lowest possible temperature. Absolute zero makes sense when you realize that temperature is connected to counting of microstates.
