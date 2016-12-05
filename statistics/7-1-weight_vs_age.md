[Think Stats Chapter 7 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2008.html#toc70) (weight vs. age)

The correlation between totalwgt_lb and agepreg is very slightly positive based on Pearson and Spearman correlation (~0.07 and ~0.09 respectively).  We can conclude that there is no real link between these two variables.

Code below:

```python
from __future__ import print_function

import sys
import numpy as np
import math

import first
import thinkplot
import thinkstats2

def ScatterPlot(age, weight, alpha=1.0):
    thinkplot.Scatter(age, weight, alpha=0.2)
    thinkplot.Show(xlabel='mother\'s age', ylabel='birth weight')

def BinnedPercentiles(df):
    bins = np.arange(10, 65, 5)
    indices = np.digitize(df.agepreg, bins)
    groups = df.groupby(indices)

    ages = [group.agepreg.mean() for i, group in groups]
    cdfs = [thinkstats2.Cdf(group.totalwgt_lb) for i, group in groups]

    for percent in [75, 50, 25]:
        weights = [cdf.Percentile(percent) for cdf in cdfs]
        label = '%dth' % percent
        thinkplot.Plot(ages, weights, label=label)

    thinkplot.Save(root='chap07scatter3',
                   formats=['jpg'],
                   xlabel="mother's age (years)",
                   ylabel='birth weight (lbs)')


def main(script):
    live, firsts, others = first.MakeFrames()
    live = live.dropna(subset=['agepreg', 'totalwgt_lb'])
    BinnedPercentiles(live)
    ages = live.agepreg
    weights = live.totalwgt_lb
    print('thinkstats2 Corr', thinkstats2.Corr(ages, weights))
    print('thinkstats2 SpearmanCorr',
          thinkstats2.SpearmanCorr(ages, weights))
    ScatterPlot(ages, weights, alpha=0.1)
    thinkplot.Save(root='chap07scatter1',
                   legend=False,
                   formats=['jpg'])


if __name__ == '__main__':
    main(*sys.argv)
```
