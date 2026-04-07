import  pandas as pd

mydataset={
    "cars":["BMW","FORD","SUBARU"],
    "drivers":["brian","victor","mugatsia"]
}

myvar =pd.Series(mydataset, index=["a","b","c"])

print(myvar["c"])