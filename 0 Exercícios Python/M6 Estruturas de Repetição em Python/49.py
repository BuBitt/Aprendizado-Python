"""
49. O funcionário chamado Carlos tem um colega chamado João que recebe um salário que
    equivale a um terço do seu salário. Carlos gosta de fazer aplicações na caderneta de
    poupança e vai aplicar seu salário integralmente nela, pois está rendendo 2% ao mês.
    João aplicará seu salário integralmente no fundo de renda fixa, que está rendendo 5%
    ao mês. Construa um programa que deverá calcular e mostrar a quantidade de meses
    necessários para que o valor pertencente a João iguale ou ultrapasse o valor pertencente
    a Carlos. Teste com outros valores para as taxas.
"""
s_c = 3
s_j = 1
mes = 0

while s_c > s_j:
    mes += 1
    s_c = 3 * (1 + 0.02) ** mes
    s_j = (1 + 0.05) ** mes
print(mes)
