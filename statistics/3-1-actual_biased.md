[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

Using the data from the NSFG for the number of children in the household (numkdhh), we are able to illustrate the class size paradox. The output from the below code snippets shows that the biased mean reported is over 100% higher than the actual mean (~2.4 vs ~1.02 respectively).

```python
import thinkstats2
numkdhh_pmf = thinkstats2.Pmf(resp.numkdhh, label='actual')

import thinkplot
thinkplot.Hist(numkdhh_pmf)
thinkplot.Show(xlabel='Number of children in household', ylabel='PMF')

def BiasPmf(pmf, label=''):
    """Returns the Pmf with oversampling proportional to value.

    If pmf is the distribution of true values, the result is the
    distribution that would be seen if values are oversampled in
    proportion to their values; for example, if you ask students
    how big their classes are, large classes are oversampled in
    proportion to their size.

    Args:
      pmf: Pmf object.
      label: string label for the new Pmf.

     Returns:
       Pmf object
    """
    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, x)

    new_pmf.Normalize()
    return new_pmf

numkdhh_biased_pmf = BiasPmf(numkdhh_pmf, label='observed')

thinkplot.PrePlot(2)
thinkplot.Pmfs([numkdhh_pmf, numkdhh_biased_pmf])
thinkplot.Show(xlabel='Number of children in household', ylabel='PMF')

mean_numkdhh = numkdhh_pmf.Mean()
mean_numkdhh_biased = numkdhh_biased_pmf.Mean()
print mean_numkdhh, mean_numkdhh_biased
```
