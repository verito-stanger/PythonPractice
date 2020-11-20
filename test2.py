import pytest
from cuil import Cuil 

cuil = Cuil()

elYeison= cuil.openJson("testing")
print(elYeison["frame"]["GetFieldBy"]) 
message = elYeison["frame"]["GetFieldBy"]

assert elYeison["frame"]["GetFieldBy"] == "id", f" El valor no coincide, el valor es:{message}"

assert cuil.openJson("testing2") is None , "El archivo no tiene un coño"

#pytest.skip(u"get_json_file: No se encontro el Archivo " + json_path)




#assert True == True, "True no es igual a False"

#assert False == False, "False no es igual a True"

#assert True != False, "False no es distinto de True"






