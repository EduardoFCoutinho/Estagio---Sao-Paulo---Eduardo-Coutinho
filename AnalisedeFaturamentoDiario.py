import json

with open('faturamento.json', 'r') as f:
    faturamento_diario = json.load(f)

# Calculando o menor e maior valor, e a média (ignorando zeros)
menor_valor = min(faturamento for faturamento in faturamento_diario if faturamento > 0)
maior_valor = max(faturamento_diario)
media = sum(faturamento for faturamento in faturamento_diario if faturamento > 0) / len([faturamento for faturamento in faturamento_diario if faturamento > 0])

# Contando os dias com faturamento acima da média
dias_acima_media = sum(1 for faturamento in faturamento_diario if faturamento > media)

print(f"Menor valor: {menor_valor}")
print(f"Maior valor: {maior_valor}")
print(f"Dias acima da média: {dias_acima_media}")
