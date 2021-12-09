from IPython.core.display import display, HTML
import re

texto = input('Insira texto para analise: ')
texto = re.sub('[\W+]',' ', texto)
texto = texto.lower()
lista_palavras = texto.split()

palavras_isoladas = []
qtd_palavras_isoladas = []
for palavra in lista_palavras:
    if palavra not in palavras_isoladas:
        palavras_isoladas.append(palavra)
for palavra in palavras_isoladas:
    qtd_palavras_isoladas.append(lista_palavras.count(palavra))

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
print(lst_limpa_qtd_palavras)

fM = int(input('Insira a frequencia que mais se aproxima de retirar as palavras não relevantes da analise: '))
for i, p in enumerate(lst_limpa_qtd_palavras):
    if p == fM:
        stop_words = lst_limpa_qtd_palavras[:i]
for palavra in stop_words:
    if type(palavra) == int:
        stop_words.remove(palavra)

fm = int(input('Insira a frequência mais baixa, se necessário, ou 0 para ignirar: '))
for i, p in enumerate(lst_limpa_qtd_palavras):
    if p == fm:
        frequencia_minima = lst_limpa_qtd_palavras[i:]
    elif p == 0:
        frequencia_minima = []
for palavra in frequencia_minima:
    if type(palavra) == int:
        frequencia_minima.remove(palavra)

for i, palavra in enumerate(palavras_isoladas):
    if palavra in stop_words:
        palavras_isoladas.pop(i)
        qtd_palavras_isoladas.pop(i)
    elif palavra in frequencia_minima:
        palavras_isoladas.pop(i)
        qtd_palavras_isoladas.pop(i)

elemento = '<li><a data-weight="{}">{}</a></li>'

lista_elementos = ''
for i in range(len(palavras_isoladas)):
    lista_elementos = lista_elementos + elemento.format(qtd_palavras_isoladas[i], palavras_isoladas[i])

dados = f'''
<ul class="cloud">
{lista_elementos}
</ul>
'''

%%html 
<style> 
ul.cloud {
  list-style: none;
  padding-left: 0;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
  line-height: 2.75rem;
  width: 600px;
}

ul.cloud a {
  --size: 4;
  --color: #a33;
  color: var(--color);
  font-size: calc(var(--size) * 0.25rem + 0.5rem);
  display: block;
  padding: 0.125rem 0.25rem;
  position: relative;
  text-decoration: none;
}

ul.cloud a[data-weight="1"] { --size: 1; }
ul.cloud a[data-weight="2"] { --size: 2; }
ul.cloud a[data-weight="3"] { --size: 3; }
ul.cloud a[data-weight="4"] { --size: 4; }
ul.cloud a[data-weight="5"] { --size: 6; }
ul.cloud a[data-weight="6"] { --size: 8; }
ul.cloud a[data-weight="7"] { --size: 10; }
ul.cloud a[data-weight="8"] { --size: 13; }
ul.cloud a[data-weight="9"] { --size: 16; }

ul[data-show-value] a::after {
  content: " (" attr(data-weight) ")";
  font-size: 1rem;
}

ul.cloud li:nth-child(2n+1) a { --color: #181; }
ul.cloud li:nth-child(3n+1) a { --color: #33a; }
ul.cloud li:nth-child(4n+1) a { --color: #c38; }
</style>
