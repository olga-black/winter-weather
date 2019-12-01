"""
Visualizing winter temperatures in Krakow and Kyiv
Data source: https://pl.climate-data.org/
"""

import matplotlib.pyplot as plt
import pandas as pd

months = ["Grudzień","Styczeń", "Luty","Marsz",]


krk = pd.read_csv('Krakow_temp.csv')[months]
iev = pd.read_csv('Kyiv_temp.csv')[months]

mean_krk = krk.iloc[0]
mean_iev = iev.iloc[0]


min_krk = krk.iloc[1]
min_iev = iev.iloc[1]

print(plt.style.available)
plt.style.use('Solarize_Light2')

plt.plot(months, mean_krk, label="Mean in Krakow", color='red')
plt.plot(months, mean_iev, label="Mean in Kyiv", color='red', linestyle='--')

plt.plot(months, min_krk, label="Min in Krakow", color='navy')
plt.plot(months, min_iev, label="Min in Kyiv", color='navy', linestyle='--')

plt.ylim(-10, 6)
plt.ylabel("Temperature, °C")
plt.title('Winter temperature in KRK and IEV')
plt.legend()
plt.tight_layout()
plt.show()

