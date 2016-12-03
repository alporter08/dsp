[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

Based on the fact that the distribution of heights is approximately normal, the percentage of the male population that falls within the height requirements of the Blue Man Group is around 34%.

```python
min_hgt_cm = 177.8 # 5'10"
max_hgt_cm = 185.42 # 6'1"
dist.cdf(max_hgt_cm) - dist.cdf(min_hgt_cm)
```
