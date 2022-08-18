# Linear Algebra

**Vector**

Physics Perspective - _Arrow with Direction and Length_

CS Perspective - _List of Numbers_

Maths Perspective - _Anything with a sensible notion_

The numbers that define a vector give the location of the head of the arrow x,y,z

Addition of vectors gives a vector that gives the same final postion as the two vectors performed one after the other.

Multiplying a vector by a scalar changes the magnitude.

Vectors have geometrical and mathematical reresentation which are interchangeable.

![Vector representation](/Notes/images/Vector%20Representaion.png "Vector")


**Basis Vectors**

These vectors when multiplied by scalars and added can give the location of all the vectors in space.

We use _i^_ (x-axis) , _j^(y-axis)_ and _k^(z-axis)_ as our bbases vectors

The _"span"_ of given vectors is the set of all their linear combinations, i.e all the vectors that can be representated by the given vectors
For 2 non co-linear vectors, the span is the entire 2d-space while for co-linear vectors the span is a line.

When we have a few vectors and we can remove one of them without changing the span, we call them **linearly dependent**. For eg, 2 co-linear vectors or 3 co-planar vectors.

When all the vectors are important for the span, the vectors are called **linearly independent**.


## Linear transformation

Transformation is basically a function but the key difference is that transformation suggests movement, specifically of one vector to another vector.

All vectors in a given space move to another vector.

Linear Transformation has 2 properties:
1. All lines must remain lines.
2. Origin must remain fixed in place

![Linear Transformation](/Notes/images/Linear%20Transformation%20.png "Linear Transfoormation")

Grid lines become parallel and evenly spaced.


To explain this numerically, we only need to know and define the transformation of i^ and j^ (and k^ depending upon number of dimensions)

Since all vectors in a space can be representesd by i^ and j^, we need to replace i^ and j^ by transformed i^ and j^ in the representation of and vector.

![Numerical Transformation](/Notes/images/Linear%20Transformation%20Numerically.png "Numerical Transformation")

Example:
![Example](/Notes/images/Transformation%20Example.png "Example")

The next example shows a generalized transformation. It also shows the represenation used where the given 2x2 matrix gives the transformed position of the basis vectors and x,y and the positions of a random vector.

The first column in 2x2 matrix is the transformed postion of first basis vector and second column is the transformed postion of 2x2 matrix.

![Generalized](/Notes/images/Generalized%20example%20with%20representation.png "Generalized")
