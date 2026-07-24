import pandas as pd
import seaborn as sb

# Robust CSV parsing: this dataset stores each row as a quoted string
# containing tab-separated fields (and a trailing comma). We'll try
# a normal read first, then fall back to manual parsing.
try:
	df = pd.read_csv('titanic.csv')
except Exception:
	df = None

if df is None or 'Survived' not in df.columns:
	rows = []
	with open('titanic.csv', 'r', encoding='utf-8') as f:
		for line in f:
			line = line.strip()
			if not line:
				continue
			# remove trailing comma if present
			if line.endswith(','):
				line = line[:-1]
			# remove surrounding quotes
			if line.startswith('"') and line.endswith('"'):
				line = line[1:-1]
			parts = [p.strip() for p in line.split('\t')]
			rows.append(parts)
	header = rows[0]
	data = rows[1:]
	df = pd.DataFrame(data, columns=header)

print('[*] Read Dataframe')
print('Columns:', list(df.columns))
print(df.isnull().sum())

if 'Survived' not in df.columns:
	raise KeyError("'Survived' column not found after parsing; check file format")

# Coerce Survived to numeric (handles stray whitespace/quotes)
survival_col = pd.to_numeric(df['Survived'], errors='coerce')
print(f'Survived:\n{survival_col.head()}')

died = []
survived = []
for i in survival_col:
	if i==0:
		died.append(i)
	elif i==1:
		survived.append(i)
	else:
		print('\n[UNIQUE] Column Survived has value not equal to 1 or 0')
		
print(f'[INFO] {died}\n[INFO] {survived}')