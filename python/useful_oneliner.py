import pandas as pd
import re

df['registration_date'] = df['registration_date'].map(lambda x: "20{year:02}-{month:02}-{day:02}".format(year=int(x[-2:]),month=int(re.search('(?<=/)\d+(?=/)',x).group(0)),day=int(re.search('(?<=^)\d+(?=/)',x).group(0))))
