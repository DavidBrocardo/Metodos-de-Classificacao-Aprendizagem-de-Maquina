
import pandas as pd

# Carregar o arquivo CSV
df = pd.read_csv('ObesityDataSet_raw_and_data_sinthetic.csv')

# Dicionários de mapeamento para cada coluna
gender_map = {'Female': 0, 'Male': 1}
family_history_map = {'no': 0, 'yes': 1}
favc_map = {'no': 0, 'yes': 1}
caec_map = {'no': 0, 'Sometimes': 1, 'Frequently': 2, 'Always': 3}
smoke_map = {'no': 0, 'yes': 1}
scc_map = {'no': 0, 'yes': 1}
calc_map = {'no': 0, 'Sometimes': 1, 'Frequently': 2, 'Always': 3}
mtrans_map = {'Walking': 0, 'Public_Transportation': 1, 'Automobile': 2, 'Motorbike': 3, 'Bike' : 4}
nobeyesdad_map = {
    'Insufficient_Weight': 0, 
    'Normal_Weight': 1, 
    'Overweight_Level_I': 2, 
    'Overweight_Level_II': 3, 
    'Obesity_Type_I': 4, 
    'Obesity_Type_II': 5, 
    'Obesity_Type_III': 6
}

# Aplicar o mapeamento para cada coluna relevante
df['Gender'] = df['Gender'].map(gender_map)
df['family_history_with_overweight'] = df['family_history_with_overweight'].map(family_history_map)
df['FAVC'] = df['FAVC'].map(favc_map)
df['CAEC'] = df['CAEC'].map(caec_map)
df['SMOKE'] = df['SMOKE'].map(smoke_map)
df['SCC'] = df['SCC'].map(scc_map)
df['CALC'] = df['CALC'].map(calc_map)
df['MTRANS'] = df['MTRANS'].map(mtrans_map)
df['NObeyesdad'] = df['NObeyesdad'].map(nobeyesdad_map)

# Salvar as alterações em um novo arquivo CSV ou sobrescrever o existente
df.to_csv('ObesityDataSet_Alterada.csv', index=False)
