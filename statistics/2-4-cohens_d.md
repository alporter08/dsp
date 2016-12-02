[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

It appears that first babies are less heavy than others.  The mean weight is ~7.20 lbs for firsts vs. ~7.33 lbs for others.  However, upon calculating Cohen's d, the difference in means is only 0.09 standard deviations, which is small.  The difference in means for weights is approximately 3 times larger than the difference in means for pregnancy lengths.

These values were calculated using the below code:

```python

def weights():
    live, firsts, others = first.MakeFrames()
    firsts_mean = firsts.totalwgt_lb.mean()
    others_mean = others.totalwgt_lb.mean()

    Cohens_d_ex = Cohens_d(firsts.totalwgt_lb, others.totalwgt_lb)


    return firsts_mean, others_mean, Cohens_d_ex

def Cohens_d(group1, group2):
    mean1 = group1.mean()
    mean2 = group2.mean()

    var1 = group1.var()
    var2 = group2.var()

    n1 = len(group1)
    n2 = len(group2)

    Cohens_d = (mean1 - mean2)/math.sqrt((n1 * var1 + n2 * var2)/(n1 + n2))

    return Cohens_d
```
