1. Use `df.itertuples()` instead of `df.iterrows()` for speed. To make it even faster use `df.itertuples(name=None)`. `itertuples` returns a namedTuple while `iterrows` returns a pandas.Series object.

2. 