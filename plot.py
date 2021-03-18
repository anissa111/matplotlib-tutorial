import matplotlib.pyplot as plt
import numpy as np
import xarray as xr
import geocat.datafiles as gdf

ds = xr.open_dataset(gdf.get("netcdf_files/soi.nc"))
print(ds)

dsoik = ds.DSOI_KET
dsoid = ds.DSOI_DEC
date = ds.date
num_months = np.shape(date)[0]

# Dates in the file are represented by year and month (YYYYMM)
# representing them fractionally will make ploting the data easier
date_frac = np.empty_like(date)
for n in np.arange(0, num_months, 1):
    yyyy = int(date[n] / 100)
    mon = (date[n] / 100 - yyyy) * 100
    date_frac[n] = yyyy + (mon - 1) / 12

    
plt.figure()
ax = plt.gca()

ax.plot(date_frac, dsoik, color='black', linewidth=0.5)
ax.plot(date_frac, dsoid, color='black')

plt.show()