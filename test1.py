def levi(a,b):
    if a == "": return len(b)
    if b == "": return len(a)
    if a[0] == b[0]: return levi(a[1:],b[1:])
    return 1 + min(levi(a[1:],b), levi(a,b[1:]), levi(a[1:],b[1:]))

print(levi("bac a","abcd"))

# print(levi("Bachelor Party","Apache Parquet"))

# print(levi("ts = pd.Series(np.random.lognormal(mean=10, size=1000))","ts = pd.Series(np.random.poisson(lam=10, size=5))"))