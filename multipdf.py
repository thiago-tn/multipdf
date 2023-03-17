import os
from PIL import Image
from PyPDF2 import PdfFileMerger, PdfFileReader

print("""/
  ,_     _
 |\\_,-~/
 / _  _ |    ,--.
(  @  @ )   / ,-'
 \  _T_/-._( (
 /         `. \
|         _  \ |
 \ \ ,  /      |
  || |-_\__   /
 ((_/`(____,-'
    Editor de PDF 
  by Theago
               """)

print("E d i t o r   d e   P  D  F ")

def list_pdfs_in_folder(folder_path):
    pdfs = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            pdfs.append(os.path.join(folder_path, filename))
    return pdfs

def extract_image_from_pdf(pdf_path, output_path):
    # implementar função de extração de imagem aqui
    pass

def extract_text_from_pdf(pdf_path):
    # implementar função de extração de texto aqui
    pass

def merge_pdfs(pdf1_path, pdf2_path, output_path):
    merger = PdfFileMerger()
    merger.append(open(pdf1_path, 'rb'))
    merger.append(open(pdf2_path, 'rb'))
    with open(output_path, 'wb') as f:
        merger.write(f)

options = ["(1) Lista de Arquivos PDF", "(2) Extrair Imagem", "(3) Extrair Texto", "(4) Juntar Arquivos PDF"]
for option in options:
    print(option)

entrada = input("Selecione uma Opção de 1 a 4: ")
if entrada == '1':
    folder_path = input("Caminho da pasta: ")
    pdfs = list_pdfs_in_folder(folder_path)
    print("Arquivos PDF na pasta:")
    for pdf in pdfs:
        print(pdf)
elif entrada == '2':
    pdf_path = input("Caminho do arquivo PDF: ")
    output_path = input("Caminho de saída da imagem: ")
    extract_image_from_pdf(pdf_path, output_path)
    print("Imagem extraída com sucesso.")
elif entrada == '3':
    pdf_path = input("Digite o caminho do arquivo PDF: ")
    text = extract_text_from_pdf(pdf_path)
    print("Texto extraído do PDF:")
    print(text)
elif entrada == '4':
    pdf1_path = input("Caminho do primeiro arquivo PDF: ")
    pdf2_path = input("Caminho do segundo arquivo PDF: ")
    output_path = input("Caminho de saída do arquivo PDF mesclado: ")
    merge_pdfs(pdf1_path, pdf2_path, output_path)
    print("PDFs mesclados com sucesso.")
else:
    print("Opção Não Encontrada.")