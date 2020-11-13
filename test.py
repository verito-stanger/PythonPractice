from cuil import Cuil

cuil = Cuil()

#assert cuil.validar_cuit('95644') == False, cuil.msj

#assert cuil.validar_cuit('20-95625072*3') == False, cuil.msj

#assert cuil.validar_cuit('20-95625072-8') == False, cuil.msj

assert cuil.validar_cuit2('20956250723') == True, cuil.msj

assert cuil.validar_cuit2('209562507sdgsd2323') == False, cuil.msj

assert cuil.validar_cuit2('5') == False, "Le faltan digitos"

assert cuil.validar_cuit2('20956250@32/-   ***.....7sdgsd2323') == False, cuil.msj

assert cuil.validar_cuit2('20-95625072-8') == True, cuil.msj