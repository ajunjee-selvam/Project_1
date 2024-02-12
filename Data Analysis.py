import pandas as pd
from pathlib import Path

file = Path('Resources/Cannabis_Market_Data.csv')
df = pd.read_csv(file, encoding="ISO-8859-1")
df.head()