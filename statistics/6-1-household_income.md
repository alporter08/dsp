[Think Stats Chapter 6 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2007.html#toc60) (household income)

For a default value of ```python log_upper = 6.0```, we obtain the following values:
Median = 4.71
Mean = 4.65
Skewness = -0.64
Pearson = -0.34

The fraction of households that report a taxable income below the mean is ~45%.  Assuming a higher upper bound (e.g. 10e8) results in positive skewness.

Code sample from hinc2.py:

```python
def main():
    df = hinc.ReadData()
    log_sample = InterpolateSample(df, log_upper=8.0)
    log_cdf = thinkstats2.Cdf(log_sample)
    median = log_cdf.Percentile(50)
    mean = log_cdf.Mean()
    skewness = thinkstats2.Skewness(log_cdf.Values())
    pearson = thinkstats2.PearsonMedianSkewness(log_cdf.Values())
    thinkplot.Cdf(log_cdf)
    thinkplot.Show(xlabel='household income',
                   ylabel='CDF')
    return median, mean, skewness, pearson, log_cdf.Prob(mean)
```
