import PyPDF2 as py2 #Importando biblioteca PyPDF2

pdf_file = open('lista.pdf','rb') #Abre o arquivo PDF

pdf_reader = py2.PdfFileReader(pdf_file) #Cria a instancia que fará a leitura do PDF

n = pdf_reader.numPages #Obtém o número de páginas

for i in range(0,n): #Faça de 0 até n
    print('Página {}'.format(i+1)) #Imprime o número da página
    page = pdf_reader.getPage(i) #Carrega a primeira página
    print(page.extractText()) #Imprime a página carregada
    print() #Imprime linha em brancojava 