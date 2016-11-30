package main

import (
	"fmt"
	"io/ioutil"
	"path"
	"strings"
	"os"
	//"time"
	"log"
)

/////////////// External Configs
var logPath string = "C:\\Users\\enrique.nieto\\Documents\\develops\\Prompter\\"
var pautasPath string = "C:\\Users\\enrique.nieto\\Documents\\develops\\Prompter\\"


////////////// System Functions
type LogItem struct{
	moment string
	errorType string
	message string
	app string
}

func addToLog(logFolder string,errorType string ,message string){
	/*t := time.Now()
	momento:=t.Format("2006-01-02 15:04:05")
	logString := momento + "   " + errorType + ": " + message

	fmt.Println(logString)*/

	// Salida a un archivo
	logString := errorType + ": " + message
	f, err := os.OpenFile(logFolder+"log", os.O_RDWR | os.O_CREATE | os.O_APPEND, 0666)
	if err != nil {
	    //t.Fatalf("error opening file: %v", err)
	    fmt.Println("error opening file: %v", err)
			
	}
	defer f.Close()

	log.SetOutput(f)
	log.Println(logString)
}
///////////// All about pautas
type Nota struct{
	enps_id string
	numero string
	nombre string
}

type Pauta struct{
	enps_id string
	nombre string
	inicio string
	final string
	status string
	numNotas int
	notasReady int
	notasNotReady int
	notas []Nota

}


func readPauta(pautaPath string) Pauta{
	var pautaReturn Pauta
	var notaDir string

	if _, err := os.Stat(pautaPath); err == nil {

		// Obtenemos el enps_id de la pauta

		dat, err := ioutil.ReadFile(pautaPath)
		check(err)
		pautaName := strings.Split(path.Base(pautaPath),".")
		filename:= pautaName[0]
		pautaReturn.enps_id = filename
		notaDir = path.Dir(pautaPath)+"/"+filename

		// Obtenemos los datos del encabezado
		pauta:= string(dat)

		// Arreglo con todo el contenido de la pauta
		pautaList := strings.Split(pauta, "\n")

		header1 := strings.Split(pautaList[0], "	")
		pautaReturn.nombre = header1[0]
		pautaReturn.inicio = header1[1]
		pautaReturn.final = header1[2]
		pautaReturn.status = "online"

		pautaReturn.numNotas = len(pautaList)-2

		for i:=1; i < pautaReturn.numNotas+1; i++{
			fmt.Println("Nota",i,pautaList[i])
			if _, err := os.Stat(notaDir); err == nil {
				//fmt.Println("Existe: ",notaDir)
				pautaReturn.notasReady += 1
			}else{
				fmt.Println("No Existe: ",notaDir)
				addToLog(logPath, "NotaError: ", "No Existe: "+notaDir)
				pautaReturn.notasNotReady += 1
			}
		}

	}else{
		fmt.Println("No existe: ",pautaPath)
		addToLog(logPath, "PautaError: ", "No Existe: "+pautaPath)
	}

	return pautaReturn
}

func check(e error) {
	if e != nil {
		fmt.Println("No se encuentra el archivo")
		panic(e)
	}
}

func main() {
	readedPauta:=readPauta("T:/48DBF533-7428-4EF0-A2E19F320B4B615C.DAT")
	fmt.Println(readedPauta)


}
