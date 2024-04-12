# Pandas: Get the Business Days between two Dates

import pandas as pd

date1 = '2023-08-16'
date2 = '2023-08-21'

business_days = pd.bdate_range(start=date1, end=date2)

# DatetimeIndex(['2023-08-16', '2023-08-17', '2023-08-18', '2023-08-21'], dtype='datetime64[ns]', freq='B')
print(business_days)

print(len(business_days))  # 👉️ 4