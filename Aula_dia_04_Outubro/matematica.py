import pandas as pd
import numpy as np

# Defina as classes e frequências
classes = ["15-25", "25-35", "35-45", "45-55", "55-65"]
frequencias = [16, 30, 41, 28, 15]

# Crie um DataFrame com as classes e frequências
tabela_frequencia = pd.DataFrame({"Classe": classes, "Frequência": frequencias})

# Crie uma tabela formatada
linha_superior = "+" + "-" * 20 + "+" + "-" * 12 + "+" + "-" * 17 + "+" + "-" * 15 + "+"
linha_titulo = "| {:^20} | {:^12} | {:^17} | {:^15} |".format("Classe", "Frequência", "Frequência Acum.", "Frequência Rel.")
linha_divisao = "+" + "=" * 20 + "+" + "=" * 12 + "+" + "=" * 17 + "+" + "=" * 15 + "+"

print(linha_superior)
print(linha_titulo)
print(linha_divisao)

total_frequencia = 0
frequencia_acumulativa = 0

for _, row in tabela_frequencia.iterrows():
    classe, frequencia = row['Classe'], row['Frequência']
    frequencia_acumulativa += frequencia
    frequencia_relativa = frequencia / sum(frequencias)
    linha = "| {:<20} | {:^12} | {:^17} | {:^15.4f} |".format(classe, frequencia, frequencia_acumulativa, frequencia_relativa)
    print(linha)
    total_frequencia += frequencia

print(linha_divisao)
linha_total = "| {:<20} | {:^12} | {:^17} | {:^15} |".format("Total", total_frequencia, "", "")
print(linha_total)
print(linha_superior)

# Cálculo da média
media = np.average([int(classe.split('-')[0]) + 5 for classe in classes], weights=frequencias)
print("\nCálculo da Média:")
print(f"A média é calculada como a soma ponderada dos valores médios das classes:")
print(f"Média = Σ (Valor Médio da Classe * Frequência) / Total de Frequências")
print(f"Média = Σ ((({'+'.join([str(int(classe.split('-')[0]) + 5) for classe in classes])}) * {frequencias}) / {sum(frequencias)})")
print(f"Média ≈ {media:.2f}")

# Cálculo do desvio padrão
desvio_padrao = np.sqrt(np.average([(int(classe.split('-')[0]) + 5 - media) ** 2 for classe in classes], weights=frequencias))
print("\nCálculo do Desvio Padrão:")
print("O desvio padrão é uma medida de dispersão que indica o quão dispersos os valores estão em relação à média.")
print(f"Desvio Padrão = √(Σ ((Valor Médio da Classe - Média)² * Frequência) / Total de Frequências)")
print(f"Desvio Padrão = √(Σ (((({'+'.join([str(int(classe.split('-')[0]) + 5) for classe in classes])}) - {media})² * {frequencias}) / {sum(frequencias)}))")
print(f"Desvio Padrão ≈ {desvio_padrao:.2f}")
