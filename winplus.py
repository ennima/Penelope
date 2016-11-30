import os,sys, datetime, json

##################### External configs
logPath = "C:\\Users\\enrique.nieto\\Documents\\develops\\Prompter\\"
pautasPath = "C:\\Users\\enrique.nieto\\Documents\\develops\\Prompter\\"

##################### System functions
def addToLog(logFolder,errorType,message):
	momento = str(datetime.datetime.now())
	logString = momento+"   "+errorType+": "+message
	print("LOG: ",logString)
	logFile = open(logFolder+"log.txt","a+")
	logFile.write(logString+"\n")

	logFile.close()

##################### All about pautas
class Pauta:
	_id = ""
	nombre = ""
	inicio = ""
	final = ""
	status = "offline"
	noNotas = 0
	notas = []
	notasReady = 0
	notasNotReady = 0

def readPauta(PathPauta,logPath):
	print("#### Pauta: ",PathPauta)
	contenido =""
	tmpPauta = Pauta()
	#pathPromter = 
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
				print("Content:",lineaSplited)
				#print(os.path.dirname(PathPauta))
				pathNota = os.path.dirname(PathPauta)+"\\"+ lineaSplited[0]
				print("######### pathNota: ",pathNota)
				statusMos = ""
				
				if(os.path.exists(pathNota)):
					#print("READY")
					statusMos = "TEXT"
					notasReady += 1
				else:
					#print("NOT READY")
					statusMos = "EMPTY"
					notasNotReady += 1
				print("################## Array Length:",len(lineaSplited))
				if(len(lineaSplited)>3):
					tmpPauta.notas.append({"id":lineaSplited[0],"num":lineaSplited[2],"titulo":lineaSplited[3],"status":statusMos})
				else:
					print("Nota sin nombre")
					addToLog(logPath,"PautaError: ","Nota sin nombre - "+PathPauta+"\\"+lineaSplited[0])
					tmpPauta.notas.append({"id":lineaSplited[0],"num":lineaSplited[2],"titulo":"NoTitle","status":"EMPTY"})
				count += 1
		tmpPauta.notasReady = notasReady
		tmpPauta.notasNotReady = notasNotReady

	else:
		print("No se encontró la pauta: ",PathPauta)
		

	###########  Read Index of Pauta ########
	return tmpPauta
	#print(tmpPauta.notas[0])
	#print("READY: ", tmpPauta.notasReady, " notasNotReady: ", tmpPauta.notasNotReady)




def listPautasSaveJson(ListPautas,pathPautas):
	jsonNew = "["
	countPauta = 0
	#print("Len: ",len(ListPautas))
	for pauta in ListPautas:
		sPauta = str(json.dumps(pauta.__dict__))
		index = sPauta.find("}")
		out_row = sPauta[:index] + ", 'notas':" + str(pauta.notas) + sPauta[index:]
		aceptable_json = out_row.replace("'","\"")
		#print("##:\n",aceptable_json)
		#pass
		#print(sPauta," -- Count: ",countPauta)
		if(countPauta<(len(ListPautas)-1)):
			#jsonNew += sPauta+","
			jsonNew += aceptable_json+","
		else:
			#jsonNew += sPauta
			jsonNew += aceptable_json
		countPauta += 1
	jsonNew += "]"
	print(jsonNew)
	#f = open("pautas.json","w")
	#f.write(jsonNew)
	#f.close()



winplusPath = "T:\\"
NoPautas = 0
pautaList = []

if(os.path.exists(winplusPath)):
	print("Leer Pautas en: ", winplusPath)
	pautaFiles = os.listdir(winplusPath)
	for item in pautaFiles:
		#print("->",item)
		if (".DAT" in item):
			print("----->",item)
			pautaList.append(readPauta(winplusPath+item,logPath))

			NoPautas += 1
else:
	print("No existe el directorio: ",winplusPath)

#print("NoPautas: ",NoPautas)
#print(pautaList[0].nombre)


listPautasSaveJson(pautaList,pautasPath)
print("Notas ",pautaList[0].notas)
