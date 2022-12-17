# Importando as bibliotecas em Python
import PyPDF2
import os

# Inicializando o merger
merger = PyPDF2.PdfFileMerger(strict=False)

# Percorrendo a pasta pdfs
lista_arquivos = os.listdir("./pdfs")

# Adicionando arquivos para serem mesclados
for arquivo in lista_arquivos:
    if '.pdf' in arquivo:
        merger.append(f'./pdfs/{arquivo}')

# Escrevendo o nome do arquivo final
try:
    merger.write('PDF_FINAL.pdf')
except Exception:
    print('Não foi possível salvar o arquivo PDF_FINAL.pdf')   
else:
    print('Arquivo PDF_FINAL.pdf foi salvo com sucesso!')
