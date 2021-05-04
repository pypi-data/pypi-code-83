import os
import pickle
class Examen:
    def __init__(self):
        self.puntos =0
        self.preguntas=[]
        self.num_preguntas=0

    def cargarPreguntas(self, fichero):
        try:
            f = open(fichero, "r")

            contenido=os.stat(fichero).st_size == 0
            if contenido:
                print("El archivo introducido esta vacio")
            else:
                print("El archivo se ha cargado, puedes realizar el test")
                lines = f.readlines()
                pregunta_encontrada=False
                respuesta_encontrada=False
                puntos_encontrada=False
                opciones =[]
                try:
                    for line in lines:
                        if line.startswith(";P;"):
                            self.num_preguntas=+1
                            pregunta_txt=line[3:]
                            pregunta_encontrada=True

                        elif pregunta_encontrada & line.startswith(";R;"):
                            respuesta = int(line[3:])
                            respuesta_encontrada=True

                        elif respuesta_encontrada:
                            puntos =int(line)
                            puntos_encontrada =True
                        elif pregunta_encontrada:
                            opciones.append(line)
                            if len(opciones)>4:
                               raise Exception("El documento contiene una pregunta con más de 4 respuestas")
                        if pregunta_encontrada & respuesta_encontrada & puntos_encontrada & (len(opciones)>2 & len(opciones)<4):
                            pregunta = Pregunta(pregunta_txt,opciones,respuesta,puntos)

                            self.preguntas.append(pregunta)
                            pregunta_encontrada =False
                            respuesta_encontrada=False
                            puntos_encontrada=False
                            opciones.clear()
                except Exception as e:
                    print(e)
        except IOError:
            print("El archvio introducido no existe")



    def siguientePregunta(self):
        preguntas_existen=False
        for pregunta in self.preguntas:
            preguntas_existen=True
            pregunta.mostrarPregunta()
            respuestaUsuario=self.escoger_valores_int("Introduce tu respuesta:\n",int)
            punto = pregunta.comprobarRespuesta(respuestaUsuario)
            self.puntos=self.puntos+punto
        if preguntas_existen:
            print("Has sacado un: "+str(self.puntos))


    def reiniciarTest(self):
        self.puntos=0
        self.preguntas.clear()
        print("El test ha sido reiniciado, carga de nuevo el test para poder realizarlo")
    def realizarTest(self):
        self.siguientePregunta()


    def escoger_valores_int(self, string, type):
        while True:
            input_usuario=input(string)
            try:
                input_usuario = self.validate_numeric(input_usuario, type)
            except ValueError:
                print('Intenta de nuevo solo de acceptan valor ' + str(type) + '\n')
                continue
            except Exception as e:
                print(e)
                continue
            else:
                return input_usuario

    def validate_numeric(self, value_string, numeric_type):
        """Validate a string as being a numeric_type"""
        try:
            if(int(value_string)<1 or int(value_string)>4):
                raise Exception("La respuesta tiene que estar entre 1 y 4.")
            return numeric_type(value_string)
        except ValueError:
            raise

    def guardar_resultado(self, test):
        nombre_alumno=input("Introduce el nombre del alumno:\n")
        pickle.dump( test, open( str(nombre_alumno), "wb" ))
        print("Archivo guardado")

    def leer_resultados(self):
        archivo=input("Introduce el nombre del archivo que contiene los resultados que quieres ver:\n")
        resultados = pickle.load( open( archivo, "rb" ) )

        print(resultados)
        print("Resultado impimidos")
    def __str__ (self):
        for p in self.preguntas:
            print(p)
        return '\nPuntos total de examen:{} '.format( self.puntos)

class Pregunta:

    def __init__(self, pregunta, opciones, respuesta, puntos):
        self.pregunta = pregunta
        self.opciones = []
        for o in opciones:
            self.opciones.append(o)
        self.respuesta = respuesta
        self.puntos = puntos

    def mostrarPregunta(self):
        print(self.pregunta)
        for opcion in self.opciones:
            print(opcion)

    def comprobarRespuesta(self, respuestaUsuario):

        if respuestaUsuario == self.getRepuesta():
            return self.getPuntos()
        else:
            return 0

    def getPuntos(self):
        return int(self.puntos)
    def getPregunta(self):
        return str(self.pregunta)
    def getOpciones(self):
        return self.opciones
    def getRepuesta(self):
        return int(self.respuesta)

    def __str__ (self):
        print("\n"+self.pregunta)
        for o in self.opciones:
            print(o)
        return '\n Respuesta:{}\n Puntos:{}\n\n'.format( self.respuesta, self.puntos)
