#### Archimedes and pi

This project is all about Archimedes.  

Here we discuss his method for approximating the value of &pi;, the ratio of the circumference of a circle to its diameter.  The commonly cited result is 

> The ratio of the circumference of any circle to its diameter is less than 3 1/7 but greater than 3 10/71.

In decimal that is 

```3.140845.. < pi < 3.1428571```

The method uses paired inscribed and circumscribed polygons.

<img src="figs/fig1.png" style="width: 400px;" />

To focus on the bounds to some extent misses the main idea, that Archimedes described an iterative procedure which can be used to calculate the value of &pi; <i>to any desired accuracy</i>.

Although the idea is beautiful, his argument is somewhat unwieldy in detail.  We give his exact argument (I have not read the original, not even the Heath translation, but this is based on a trusted source).  We will also use modern trigonometry to achieve the same result more economically.  And to top it off, we will derive the same results by a different approach, from basic geometry.

Given the limitations of numerical calculation in Archimedes' time, it is amazing that he went as far as he did, calculating bounds for &pi; in terms of 96-sided polygons.


#### Proofs

As a preliminary, we have short write-ups for the various mathematical proofs required for the calculations in the first section.

- [sum of angles](Sum of angles.pdf)
- [double and half-angle formulas](Double angle.pdf)
- [angle bisector](Angle bisector.pdf)

[upcoming:  I will also have something to say about the various fractional manipulations and estimates for square roots.]

#### Outline

Here are the detailed calculations that retrace Archimedes' steps in computing upper and lower bounds on pi.

In the end, we will arrive at the famous expression:

```
3 10/71 < pi < 3 1/7 
```

The first write-up 

- [original](Archimedes orig.pdf)

follows the [web page](https://itech.fgcu.edu/faculty/clindsey/mhf4404/archimedes/archimedes.html) I found that showed me how.  

It uses classic labels for the triangle sides as line segments like ``AO``, and gives ``AO:AC`` as such, rather than as cot &theta; and csc &theta;.

A revised version uses single letters (like ``f``) for the sides, and de-emphasizes the geometry, showing how to reduce the steps to a mechanical series of calculations of cotangent and cosecant.

- [revised](Archimedes csc.pdf)

Next, the first of several modern approaches builds the argument for the sum of perimeters in terms of the sine and tangent of the half angle, i.e. the half-angle formulas.

- [Trigonometry](Archimedes trig.pdf)


#### More modern approaches

There are two other sets of formulas that reach this end, one based on perimeters, and one on areas.  These formulas are intriguing because they are so simple, it's not surprising that they are connected.  

For example, consider a circle of unit <i>diameter</i>, so that &pi; is equal to the perimeter.  If ``p`` and ``P`` are the inside and outside perimeters for polygons whose sectors have central angle &theta;, and the same symbols are used with primes for angle &theta;/2, then:

```
P' = 2pP/(p + P)
1/P' = 1/2(1/p + 1/P)

p' = sqrt(pP')
```

The corresponding formulas for inside ``a`` and outside ``A`` areas are (for a circle of unit radius)

```
A' = 2a'A/(a' + A)
a' = sqrt(aA)
```

However, these two very similar sets of formulas are subtly different.  

For example, to go from ``p`` and ``P`` to the primed version, we start with the first formula, while for area we must start with the square root.  

Part of our purpose in this material is to show that this works.

The perimeter gives the ratio to the diameter, since ``pi * d = C``, where the circumference ``C`` is also called the perimeter.

In the first write-up we go from the half-angle formulas to the perimeter formulas.

- [Perimeter](Perimeter.pdf)

The area is related to a circle of unit radius, since ``pi * r^2 = A``.

In the other write-up we go from the half-angle formulas to the areaa formulas.

- [Area](Area.pdf)

#### Geometry

In an alternative approach, we derive the formulas for perimeter and area from basic geometry.  The perimeter is first

- [Perimeter by geometry](Geometry1.pdf)

and then the area:

- [Area by geometry](Geometry2.pdf)

#### Calculations

Finally, here are some calculations to check the formulas obtained above.  The first script checks the perimeter and area formulas.

- [calculate1.py](src/calculate1.py)

<b>Output:</b>

```
> python calculate1.py
        perimeter
  0 2.828427  4.000000
  1 3.061467  3.313708
  2 3.121445  3.182598
  3 3.136548  3.151725
  4 3.140331  3.144118
  5 3.141277  3.142224

        area
  0 2.000000  4.000000
  1 2.828427  3.313708
  2 3.061467  3.182598
  3 3.121445  3.151725
  4 3.136548  3.144118
  5 3.140331  3.142224

>
```

It's curious that we get exactly the same values for ``P`` and ``A``.  Those for ``p`` and ``a`` match as well, except there is an offset of one row.

The second script tests the trig calculations.

- [calculate2.py](src/calculate2.py)

<b>Output:</b>

```
> python calculate2.py 
        trig
  4 2.828427  4.000000
  8 3.061467  3.313708
 16 3.121445  3.182598
 32 3.136548  3.151725
 64 3.140331  3.144118
128 3.141277  3.142224
>
```

It matches the perimeter calculation exactly!