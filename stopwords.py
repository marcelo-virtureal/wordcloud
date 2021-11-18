import re
texto = input('Insira o texto a ser analisado: ')
texto = re.sub('[\W+]',' ', texto)
lista_de_palavras = texto.split()
palavras_isoladas = []
qtd_palavras_isoladas = []
for palavra in lista_de_palavras:
    if palavra not in palavras_isoladas:
        palavras_isoladas.append(palavra)
validador = len(lista_de_palavras) - len(palavras_isoladas)
if validador < 50:
    print('O texto precisa ser maior para a aplicacao retornar um resultado relevante.')
for palavra in palavras_isoladas:
    qtd_palavras_isoladas.append(lista_de_palavras.count(palavra))
qtd_palav_isol = []
for q in qtd_palavras_isoladas:
    if q not in qtd_palav_isol:
        qtd_palav_isol.append(q)
qtd_palav_isol_ord = sorted(qtd_palav_isol, reverse=True)
lst_qtd_palavras = []
for q in qtd_palav_isol_ord:
    for i, j in enumerate(qtd_palavras_isoladas):
        if j == q:
            lst_qtd_palavras.append(q)
            lst_qtd_palavras.append(palavras_isoladas[i])
lst_limpa_qtd_palavras = []
for p in lst_qtd_palavras:
    if p not in lst_limpa_qtd_palavras:
        lst_limpa_qtd_palavras.append(p)
for i, p in enumerate(lst_limpa_qtd_palavras):
    if p == 5:
        stop_words = lst_limpa_qtd_palavras[:i]
for palavra in stop_words:
    if type(palavra) == int:
        lst_limpa_qtd_palavras.remove(palavra)
print(stop_words)