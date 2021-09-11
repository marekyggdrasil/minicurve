# minicurve

A very simple library developed by [Marek Narozniak](https://mareknarozniak.com/) for visualizing finite field over elliptic curve. The idea of making this library originates in a cryptography-related tutorial series

1. [Elliptic Curve Cryptography and Diffie-Hellman Key Exchange](https://mareknarozniak.com/2020/11/30/ecdh/)
2. [Eliptic Curve Digital Signature Algorithm](https://mareknarozniak.com/2021/03/16/ecdsa/)
3. [Schnorr Signature](https://mareknarozniak.com/2021/05/25/schnorr-signature/)
4. [Pedersen Commitments and Confidential Transactions](https://mareknarozniak.com/2021/06/22/ct/)

Disclaimer. This library is NOT secure and NOT efficient. It is meant for purely educational purposes for visualizing tutorials. Do NOT use it for any cryptography applications!

## Installation

Super simple!

```
pip install minicurve
```

## Tutorial

Points addition is as simple as `R=P+Q`, you can visualize parent points using arrows as follows.

```python
from minicurve import MiniCurve as mc
from minicurve import Visualizer

# curve parameters
a = 1
b = 7
p = 13

P = mc(a, b, p, x=10, y=4, label='P', color='tab:orange')
Q = mc(a, b, p, x=9, y=11, label='Q', color='tab:orange')

# addition of curve points
R = P + Q
R.setColor('tab:red')
R.setLabel('R')

R.x_delta = -0.3
R.arrow_thickness = 0.01 # you can control the thickness of the arrow
R.arrow_head = 20 # and its head

# visualize the finite field
vis = Visualizer(a, b, p)
vis.makeField()
vis.points = [P, Q, R]
vis.generatePlot(title='points addition $P+Q=R$ using minicurve', addition=True)
# addition=True option will use arrows to visualize addition parents

vis.plot('images/example_add.png')
```

outputs

![output-addition](https://github.com/marekyggdrasil/minicurve/blob/main/images/example_add.png?raw=true)

Multiplication by scalar works in similar way as you can simply `P=4*G` and visualize the scalar using arrow path

```python
from minicurve import MiniCurve as mc
from minicurve import Visualizer

# curve parameters
a = 0
b = 5
p = 7

G = mc(a, b, p, x=3, y=2, label='G', color='tab:green', tracing=True)
# tracing=True option will enabling plotting the arrows indicating scalar multiplication

# private key
k = 4

# public key
P = k*G

P.setColor('tab:orange')
P.setLabel('P')
P.x_delta = 0.08 # you can control the label placement relative to the point

# visualize the finite field
vis = Visualizer(a, b, p)
vis.makeField()
vis.points = [G, P]
vis.generatePlot(title='scalar multiplication $k \cdot G=P, k=4$ using minicurve')
vis.plot('images/example_mul.png')
```

outputs

![output-multiplication](https://github.com/marekyggdrasil/minicurve/blob/main/images/example_mul.png?raw=true)

## FAQ

### What are the valid values of colors?

We are using [Matplotlib colors](https://matplotlib.org/stable/tutorials/colors/colors.html).

## Thanks!

Code for computing [quadratic residues](https://en.wikipedia.org/wiki/Quadratic_residue) from [this gist](https://gist.github.com/nakov/60d62bdf4067ea72b7832ce9f71ae079). Thanks to [Nakov](https://gist.github.com/nakov).
