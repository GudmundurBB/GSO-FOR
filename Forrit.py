#GSO FORRIT
textfile = open('file.txt','w')
textfile.write('Python er ez')
textfile.close()
textfile = open('file.txt','a')
textfile.write(' \nTetta er fyrsta forritid mitt i python ')
textfile.write(' \nog tad var lett')
textfile.close()
textfile = open('file.txt','r')
print (textfile.read())
