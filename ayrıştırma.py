import pandas as pd
x=pd.read_json("jobsfinal.json")
x.JOBCREATEDATE=x.JOBCREATEDATE.str[:23]
x.JOBDATE=x.JOBDATE.str[:23]
x.LOCATION=x.LOCATION.str[4:]
x.SERVICENAME=x.SERVICENAME.str[8:]
x.REVENUE=x.REVENUE.astype(int)
x.JOBSTATUS=x.JOBSTATUS.replace(["NO SUCCESS","SUCCESS"],["0","1"])
x.to_json("hedef.json")