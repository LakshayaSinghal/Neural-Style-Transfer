# Linear Algebra

[Linear Algebra by 3B1B](https://youtube.com/playlist?list=PL0-GT3co4r2y2YErbmuJw2L5tW4Ew2O5B)


**Vector**

Physics Perspective - _Arrow with Direction and Length_

CS Perspective - _List of Numbers_

Maths Perspective - _Anything with a sensible notion_

The numbers that define a vector give the location of the head of the arrow x,y,z

Addition of vectors gives a vector that gives the same final postion as the two vectors performed one after the other.

Multiplying a vector by a scalar changes the magnitude.

Vectors have geometrical and mathematical reresentation which are interchangeable.

![Vector representation](/Linear%20Algebra%20(3B1B)/assets/Vector%20Representation.png)


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

Grid lines remain parallel and evenly spaced.

![Linear Transformation](/Linear%20Algebra%20(3B1B)/assets/Linear%20Transformation%20.png "Linear Transfoormation")




To explain this numerically, we only need to know and define the transformation of i^ and j^ (and k^ depending upon number of dimensions)

Since all vectors in a space can be representesd by i^ and j^, we need to replace i^ and j^ by transformed i^ and j^ in the representation of and vector.

![Numerical Transformation](/Linear%20Algebra%20(3B1B)/assets/Linear%20Transformation%20Numerically.png "Numerical Transformation")

Example:

![Example](/Linear%20Algebra%20(3B1B)/assets/Transformation%20Example.png "Example")

The next example shows a generalized transformation. It also shows the represenation used where the given 2x2 matrix gives the transformed position of the basis vectors and x,y and the positions of a random vector.

The first column in 2x2 matrix is the transformed postion of first basis vector and second column is the transformed postion of 2x2 matrix.

![Generalized](/Linear%20Algebra%20(3B1B)/assets/Generalized%20example%20with%20representation.png "Generalized")


Assume multiple transformations happen in a sequence, then the single transformation that has the same effect as the multiple transformations is called a **composition**.

For eg, a rotation then a shear happens:

![Composition](/Linear%20Algebra%20(3B1B)/assets/composition.png "Compposition")

The composition is the product of the 2 matrices.
The transformation are read right to left, meaning the leftest most transformation happens first.

General Method for Matrix multiplication to obtain a composition:

This follows from Linear transformation since a composition is a sequence of linear transformations.

![Step 1](/Linear%20Algebra%20(3B1B)/assets/composition%201.png "step 1")

The first column in M1 gives the location i^ after first transformation.

![Step 2](/Linear%20Algebra%20(3B1B)/assets/composition%202.png "step 2")

Similarly, the second column in M1 gives the location of j^ after first transformation.

![Step 3](/Linear%20Algebra%20(3B1B)/assets/composition%203.png "step 3")

![Step 4](/Linear%20Algebra%20(3B1B)/assets/composition%204.png "step 4")



**Does order of M1 and M2 matter?**
**Yes**, since the second transformation happens wrt the first transformation. The order of transformation hence changes the composition.

Matrices follow Associativity where (AB)C = A(BC) but this is intuitive since in both cases, the order of transformation doesn't change.


All the above concepts translate easily to higher dimensions.

The three basis vectors used are _i^_ (x-axis) , _j^(y-axis)_ and _k^(z-axis)_.

Linear transformation in 3d:

!["Linear transformation in 3d"](/Linear%20Algebra%20(3B1B)/assets/3d%20transformation.png "Linear transformation in 3d")

Composition in 3d:

!["Composition in 3d"](/Linear%20Algebra%20(3B1B)/assets/3d%20compositon.png "Composition in 3d")


## Determinants

Determinants represent the factor by which the area or volume of a given space changes when undergoing linear transformation.

For eg, in a 2d space, if the area of a unit area A becomes 2A after transformation, the determinant of the transformation is 2.
If the determinant is negative, it means the area was flipped.
If the determinant is 0, it means the transformation converted the space to a line or a dot.


In 3d space, the determinant gives us factor of change of volume.
For a positive real number, the determinant is the factor of change of volume.
For a negative real number, the determinant shows that the the directions of any 2 basis vectors were swapped.
For 0, the determinant shows that the transformation converted the space into a plane, a line or a dot.

Also, det(M1M2) = det(M1)det(M2)


## Matrcies and vaectors uses

Matrices can be used to solve a linear system of equations.

A set of linear equations can be converted to a set of matrices or vectors as follows

![Linear system of equations](/Linear%20Algebra%20(3B1B)/assets/linear%20system%20of%20eqn%20using%20matrix.png "Linear system of equations")

A shown above, the vectors can be visualized as an x,y,z vector undergoing a transformation A to give -3,0,2 vector

To solve this we will use the concept of **Inverse Matrices**

To think of it in geometric representation, an inverse matrix A<sup>-1</sup> is a matrix that reverses the transformation produced by the matrix A.

Hence, the matrix v when transformed by A<sup>-1</sup> gives matrix x,y,z.

When a matrix is multipled by its inverse, it gives an identity matrix which in the world of matrix and vectors basically means 1 and the transformation produced by it is the matrix itself.

![Inverse matrix](/Linear%20Algebra%20(3B1B)/assets/INverse%20matrix.png "Inverse Matrix")

![Inverse matrix 1](/Linear%20Algebra%20(3B1B)/assets/inverse%20matrix%201.png "Inverse matrix 1")


In case the determinant of A is 0, this means that A transformed a plane to a line. Therefore, the transformation of A<sup>-1</sup> is to comvert this line into a plane. Similar logic goes for 3d, where A inverse will have to convert a plane or a line into 3d space. Therefore, no Inverse exists.

A solution is possible if the vector after transformation A lies on the line.

This is also used to define **Rank**

Rank is the number of dimensions in the output after transformation by a matrix A.

For a 2d matrix, the highest rank can be 2.
For a 3d matrix, the highest rank can be 3. 

If the rank is lesser than the the number of dimensions before transformation, it means the transformation collapses the space to the number of dimension equal to the rank.

The set of all possibles output of a matrix transformation is called the columnspace.

The number of columns in the transformation matrix gives us the location of each basis vector after transformation which is turn gives us the span.
The span gives us all the possible outputs.

Therefore, the column space is the span of the columns of the matrix.

So if the rank of matrix is the same as the column of a matrix, its called as full rank.

We know that the origin is always at the same place in linear transformation. So, when a space is squished by a transformation, say, a plane squieshed down to a line, there is a whole set of vectors passing through origin that is squished to the origin.

![null space](/Linear%20Algebra%20(3B1B)/assets/null1.png "null space")
![null space](/Linear%20Algebra%20(3B1B)/assets/null2.png "null space")
![null space](/Linear%20Algebra%20(3B1B)/assets/null3.png "null space")

Similarly, for a 3d vector, a whole line of vectors gets squished to origin when the space is transforned to a plane and a whole plan of vectors gets squished to the origin when the space is transformed into a line.

This set of vectors is called as **null space** or **kernel**


## Dot Product

Imagine projecting a vector _a_ onto a vector _b_, then the multiplication of length of _b_ and length of projection of _a_ gives us the dot product of _a_ and _b_. We can also take projection of _b_ on _a_.
It is a useful tool for understanding projection and for testing whether or not vectors tend to point in the same direction.

## Cross Product

The cross product of 2 products gives us the area of parallelogram formed by the vectors
. The sign of the cross product depends upon the orientation of the vectors, which can be found using right hand thumb screw rule.

Since a matrix of a vector represents the transformation of i^ and j^ to that vector, a determinant of any 2 vectors, gives us the are between them.

In a true sense, cross product of any 2 vectors gives us a new 3d vector perpendicular to both the vectors. The direction of the cross product can be found using right hand thumb screw rule.


## Eigenvectors and Eigenvalues

Consider a linear transformation, usually the direction of vectors changes. But there are some vectors whose direction does not change. Such vectors are called **Eigenvectors**. Due to linearity, there is a line of all such vectors, each having the same direction. The factor by which the vectors get squished or stretched by the transformation is called **Eigenvalues**

For roation in 3d space, the rotation happens around an axis, this axis doesnt change position and direction and hence it is an eigenvector. Also there is no stretching or squishing, hence the eigen value is 1.

For explanation for computation of eigenvectors and eigen values refer this video - [Eigenvectors and Eigenvalues](https://www.youtube.com/watch?v=PFDu9oVAE-g&list=PL0-GT3co4r2y2YErbmuJw2L5tW4Ew2O5B&index=14 "Eigen vectors and Eigenvalues")

