'''
Após usar o fcrackzip descobri que o nome do arquivo era a senha, foi um jeito pratico e facil para descompactar 1.000 arquivos zipado um dentro do outro
'''
import zipfile
import os

filename = 'file.zip'
count = 0

while count < 999:
	zip = zipfile.ZipFile(filename)
	lst = zip.namelist()
	for file in lst:
		proxextract = file
		password = file.split('.', 1)[0]
	zip.extract(proxextract, pwd=password)
	if filename.endswith('.zip'):
		os.remove(filename)
	filename = proxextract
	count = count + 1
