import requests,json


class ConsultaRuc:
    def search_by_document(self, usu,pw,key,tipo,ruc,bloque):
        try:

            self.usuario_enc = usu
            self.password_enc = pw
            self.public_key = key
            self.tipo_doc = tipo
            self.ruc = ruc
            self.bloque = bloque

            payload = {
                
                "Gx_UsuEnc":self.usuario_enc,
                "Gx_PasEnc":self.password_enc,
                "Gx_Key": self.public_key,
                "TipoDoc":self.tipo_doc,
                "NroDoc": self.ruc,
                "BloquesDevolver": self.bloque

            }            
            print(payload)
            head = {
                "Content-Type" : "application/json"
            }
                        
            peticion = requests.post("https://www2.sentinelperu.com/wsrest/rest/reststandardwsv3",  headers=head, data=json.dumps(payload))
            if peticion.status_code != 200:

                error = {
                    "status": "400",
                    "descripcion":"Ha ocurrido un error en la consulta"
                 }
                return error
            else:

                respuesta = peticion.json()
              
                # info1 = respuesta
                info1 = respuesta['soafullsabiooutput']['InfBas']
                # info1 = respuesta['soafullsabiooutput']['InfBas']
                # info2 = respuesta['soafullsabiooutput']['InfGen']
              
                retorno = {

                    "informacion_basica":info1
                    # "informacion_general":info2
                                      
                }

                return retorno

        except Exception as e:
            error= {
                "status": "400",
                "descripcion":f"Ha ocurrido un error en la funcion recuperardatos {e}"
                }

            return error
            