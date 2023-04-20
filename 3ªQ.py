'''
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;
'''

import json

with open('faturamento.json') as f:
  faturamento = json.load(f)

# Encontrar menor valor de faturamento
menor_valor = min(faturamento)

# Encontrar maior valor de faturamento
maior_valor = max(faturamento)

# Calcular média mensal de faturamento, ignorando dias sem faturamento
dias_com_faturamento = [f for f in faturamento if f > 0]
media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)

# Encontrar número de dias no mês em que o valor de faturamento diário foi superior à média mensal
dias_acima_da_media = sum(1 for f in dias_com_faturamento if f > media_mensal)

print(f"Menor valor de faturamento: R${menor_valor:.2f}")
print(f"Maior valor de faturamento: R${maior_valor:.2f}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_da_media}")
