import camelot
import pandas as pd

# Baca semua table dari semua halaman PDF
tables = camelot.read_pdf('JADUAL-WAKTU-SOLAT-WPKLPTJ-2025.pdf', pages='all')

# Buat senarai DataFrame dari semua table
dfs = [table.df for table in tables]

# Gabungkan semua DataFrame menjadi satu
full_df = pd.concat(dfs, ignore_index=True)

# Simpan ke CSV
full_df.to_csv('solat_2025_kl.csv', index=False)

print(f"Berjaya extract {len(full_df)} baris ke solat_2025_kl.csv")
