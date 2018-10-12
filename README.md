#### Archimedes and pi

This project is all about Archimedes.  

Here we discuss his method for approximating the value of &pi;, the ratio of the circumference of a circle to its diameter.  The commonly cited result is 

> The ratio of the circumference of any circle to its diameter is less than 3 1/7 but greater than 3 10/71.

In decimal that is 

```3.140845.. < pi < 3.1428571```

The method uses paired inscribed and circumscribed polygons.

<img src="figs/fig1.png" style="width: 400px;" />

However, the focus on the bounds to some extent misses the main idea, that Archimedes described an iterative procedure which can be used to calculate the value of &pi; <i>to any desired accuracy</i>.

Although the idea is beautiful, his argument is somewhat unwieldy in detail.  We give his exact argument (based on a trusted source), but we will also use modern trigonometry to achieve the same result more economically.  And to top it off, we will derive the same results by a different approach, from basic geometry.

Given the limitations of numerical calculation in Archimedes' time, it would be awkward to go much farther than he did, calculating bounds for &pi; in terms of 96-sided polygons.

#### Outline

In this first section, I have put the detailed calculations that retrace his steps in computing upper and lower bounds on pi.

In the end, we will arrive at the famous expression:

```
3 10/71 < pi < 3 1/7 
```

The first write-up 

- [original](Archimedes true.pdf)

follows the [web page](https://itech.fgcu.edu/faculty/clindsey/mhf4404/archimedes/archimedes.html) I found that showed me how.  

It uses classic labels for the triangle sides as line segments like ``AO``, and gives ``AO:AC`` as such, rather than as cot &theta;.

The next uses single letters (like ``f``) for the sides, and de-emphasizes the geometry, reducing the steps to a series of calculations of cotangent and cosecant.

- [revised](Archimedes csc.pdf)

#### Proofs

In this section, we have short write-ups for the various mathematical proofs required for the calculations in the first section.

- [sum of angles](Sum of angles.pdf)
- [double and half-angle formulas](Double angle.pdf)
- [angle bisector](Angle bisector.pdf)

I will also have something to say about the various fractional manipulations and estimates for square roots.

#### More modern approaches

The first of several modern approaches builds the argument for the sum of perimeters in terms of the sine and tangent of the half angle.

- [Trigonometry](Trigonometry.pdf)

There are two other sets of formulas that also reach this end, one based on perimeters, and the other on areas.  These formulas are intriguing because they are simple, and it is not surprising that they are connected.  

For example, consider a circle of unit <i>diameter</i>, so that &pi; is equal to the perimeter.  If ``p`` and ``P`` are the inside and outside perimeters for polygons whose sectors have central angle &theta;, and the same symbols are used with primes for angle &theta;/2, then:

```
P' = 2pP/(p + P)
1/P' = 1/2(1/p + 1/P)

p'^2 = pP'
```

The corresponding formulas for inside (``a``) and outside (``A``) areas are (for a circle of unit radius)

```
A' = 2a'A/(a' + A)
a'^2 = aA
```

Notice that these two similar sets of formulas are subtly different.  

For example, to go from ``p`` and ``P`` to the primed version, we start with the first formula, while for area we must start with the square root.  

Part of our purpose in this material is to show that this works.  (I must confess, I still do not have a simple explanation for why it is true).

The perimeter gives the ratio to the diameter, since ``pi * d = C``, where the circumference ``C`` is also called the perimeter.

- [Perimeter](Perimeter.pdf)

The area is related to a circle of unit radius, since ``pi * r^2 = A``.

- [Area](Area.pdf)

#### Geometry

In an alternative approach, we analyze the basic geometry to derive all the formulas in a different way.

- [Geometry](Geometry.pdf)

Finally, we run some calculations to check the formulas obtained above.

- [Calculations](calculations.py)

