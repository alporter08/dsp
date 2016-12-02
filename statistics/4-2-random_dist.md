[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

The distribution is uniform, which can be seen in the graphical representation of the cdf, which is approximately a straight line.

```python
import random
random_vals = [random.random() for x in range(1000)]
pmf = thinkstats2.Pmf(random_vals)
thinkplot.Pmf(pmf)

cdf = thinkstats2.Cdf(random_vals)
thinkplot.Cdf(cdf)
thinkplot.Show()
```
