import sqlite3
import pandas as pd
import glob


# csv_files = glob.glob('dane/*.csv')
# df_list = []  # Lista na pojedyncze DataFrame'y
# for file in csv_files:
#     df = pd.read_csv(file)
#     df_list.append(df)
# # print(df_list)
# # Połącz wszystkie DataFrame w jeden
# combined_df = pd.concat(df_list, ignore_index=True)
# # print(combined_df)
# # # Jeśli chcesz zapisać wynik do nowego pliku CSV:
# combined_df.to_csv('combined_data.csv', index=False)
# df1 = pd.read_csv('combined_data.csv')
# print(df1.head())
# grouped = df1.groupby('Date/Time').size()
# print(grouped)


# Wczytaj plik CSV
# df = pd.read_csv('combined_data.csv')
# # Grupowanie po 'Date/Time' i łączenie wartości
# grouped = df.groupby('Date/Time').agg('first').reset_index()
# # Zapisz naprawiony plik
# grouped.to_csv('combined_data_fixed.csv', index=False)
# print("Dane zostały poprawnie zgrupowane!")


# # === 1. Wczytaj plik CSV ===
# df = pd.read_csv('combined_data.csv')
# # === 2. Konwertuj Date/Time na datetime, jeśli jeszcze nie jest ===
# df['Date/Time'] = pd.to_datetime(df['Date/Time'])
# # === 3. Tworzymy nową kolumnę tylko z datą (rok-miesiąc-dzień) ===
# df['Date'] = df['Date/Time'].dt.date
# # === 4. Usuwamy kolumnę Date/Time, aby jej nie było w dalszych obliczeniach ===
# df = df.drop(columns=['Date/Time'])
# # === 5. Grupuj po dacie i licz średnią ===
# daily_avg = df.groupby('Date').mean().reset_index()
# # === 6. Zapisz wynik do nowego pliku CSV ===
# daily_avg.to_csv('daily_averages.csv', index=False)
# print("✅ Nowy plik 'daily_averages.csv' został wygenerowany bez kolumny 'Date/Time'")


# # === 1. Wczytaj dane z pliku CSV ===
# df = pd.read_csv('daily_averages.csv')
# # === 2. Połącz się z bazą danych SQLite (utworzy plik 'weather_data.db' jeśli nie istnieje) ===
# conn = sqlite3.connect('temp.db')
# # === 3. Zapisz dane do nowej tabeli np. 'daily_averages' ===
# df.to_sql('daily_averages', conn, if_exists='replace', index=False)
# # === 4. Zamknij połączenie ===
# conn.close()
# print("✅ Dane zostały zapisane do bazy danych 'weather_data.db' w tabeli 'daily_averages'")


# 1. Wczytaj dane z pliku .csv
# Zakładam, że plik nazywa się "dane.csv" i jest w tym samym folderze co skrypt
df = pd.read_csv('daily_averages.csv', index_col=0)

# 3. Oblicz średnią dla każdego wiersza
srednie_dobowe = df.mean(axis=1)

# 4. Od każdej średniej odejmij np. 21
cdd = srednie_dobowe - 21

# 5. Wybierz tylko dodatnie wyniki i policz ich sumę
suma_dodatnich = cdd[cdd > 0].sum()

# 6. Wyświetl wynik
print(f'Suma liczb dodatnich: {suma_dodatnich}')