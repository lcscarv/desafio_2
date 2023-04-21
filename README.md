# Site Checker

Esse script tem como objetivo avaliar se um site está ativo ou não, recebendo uma ou mais URLs e retornando qual dos sites está disponível ou não.

Também pode receber um arquivo .csv contendo uma lista de sites que se deseja avaliar. O programa foi feito utilizando ambiente virtual e Python 3.9.16.
## Uso

Para rodar o código no caso de uma ou mais URLs, utiliza-se o comando:

python - m desafio_2 -u https://www.example.com https://www.google.com

Para utilizar um arquivo .csv, o código utilizado é:

python -m desafio_2 -f desafio_2/sites.csv

## Requirements
Esse programa requer Python 3 e as seguintes bibliotecas:

argparse

http.client

urllib.parse
