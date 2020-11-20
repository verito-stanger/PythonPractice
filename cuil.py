import re
import pytest
import json

class Cuil:
    def validar_cuit(self, cuit):
        
        self.msj = ""
        # validaciones minimas
        if len(cuit) != 13:
            self.msj = "El cuit esta incompleto"
            return False
        elif cuit[2] != "-" or cuit[11] != "-":
            self.msj = "El formato del cuil es invalido"
            return False

        base = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]

        cuit = cuit.replace("-", "") # remuevo las barras

        #calculo el digito verificador:
        aux = 0
        for i in range(10):
            aux += int(cuit[i]) * base[i]

        aux = 11 - (aux - (int(aux / 11) * 11))

        if aux == 11:
            aux = 0
        if aux == 10:
            aux = 9

        Validacion = (aux == int(cuit[10]))

        if Validacion:
            return True
        else:
            self.msj = "El validador del cuil es invalido"
            return False

    def validar_cuit2(self, cuit):
        cuit = re.sub('[^0-9]','', cuit)
        base = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]
        aux = 0

        self.msj = ""
        # validaciones minimas
        if len(cuit) != 11:
            self.msj = "El formato cuit es invalido"
            return False

        for i in range(10):
            aux += int(cuit[i]) * base[i]

        aux = 11 - (aux - (int(aux / 11) * 11))

        if aux == 11:
            aux = 0
        if aux == 10:
            aux = 9

        Validacion = (aux == int(cuit[10]))

        if Validacion:
            return True
        else:
            self.msj = f"El validador del cuil es invalido, el numero validador debe ser {aux}"
            return False
        

    def openJson(self, file):
        json_path = "C:\\Users\\v.a.serrano.diaz\\Desktop\\PythonPractice"+ "\\" + file + '.json'
        try:
            with open(json_path, encoding='utf-8') as read_file:
                self.json_strings = json.loads(read_file.read())
                print ("openJson: "+ json_path)
                return self.json_strings
        except FileNotFoundError:
            return None
        except ValueError:
            return None 

        
