import os

class Pauta:
	_id = ""
	nombre = ""
	inicio = ""
	final = ""
	status = "offline"
	noNotas = ""
	notas = []
	notasReady = 0
	notasNotReady = 0

def readPautaIndex(PathPauta):
	contenido =""
	tmpPauta = Pauta()

	#print(os.path.basename(PathPauta))
	filename,extension = os.path.basename(PathPauta).split(".")
	tmpPauta._id = filename
	###########  Read Index of Pauta ########
	if(os.path.exists(PathPauta)):
		#print("Leer Paua")
		pautaReaded = open (PathPauta)
		contenido = pautaReaded.read()
		pautaReaded.close()

		#print(type(contenido))
		pautaLines = contenido.strip().split("\n")
		#print("Notas: ",str(len(pautaLines)-1))
		count = 0
		notasReady = 0
		notasNotReady = 0
		for linea in pautaLines:
			if(count == 0):
				lineaSplited = linea.split("	")
				#print("Header: ",lineaSplited)
				tmpPauta.nombre = lineaSplited[0]
				tmpPauta.inicio = lineaSplited[1]
				tmpPauta.final = lineaSplited[2]
				count += 1
			elif(count > 0):
				lineaSplited = linea.split("	")
				#print("Content:",lineaSplited)
				pathNota = pathPromter+filename+"\\"+ lineaSplited[0]
				statusMos = ""
				if(os.path.exists(pathNota)):
					#print("READY")
					statusMos = "TEXT"
					notasReady += 1
				else:
					#print("NOT READY")
					statusMos = "EMPTY"
					notasNotReady += 1

				tmpPauta.notas.append({"id":lineaSplited[0],"num":lineaSplited[2],"titulo":lineaSplited[3],"status":statusMos})
				count += 1
		tmpPauta.notasReady = notasReady
		tmpPauta.notasNotReady = notasNotReady

	else:
		print("No se encontró la pauta: ",PathPauta)

	###########  Read Index of Pauta ########
	return tmpPauta
	#print(tmpPauta.notas[0])
	#print("READY: ", tmpPauta.notasReady, " notasNotReady: ", tmpPauta.notasNotReady)


pathPromter = "map\\"
PathPauta = pathPromter+"CC531625-04E5-448A-9201ECD8DE30410B.DAT"


thisPauta = readPautaIndex(PathPauta)
print(thisPauta._id)
print(thisPauta.status)

pautas = []
myPauta = Pauta()
myPauta.nombre = "Pauta 1"
pautas.append(myPauta)
myPauta2 = Pauta()
myPauta2.nombre = "Pauta 2"
pautas.append(myPauta2)

print(pautas[1].nombre)