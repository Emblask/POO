from model.Meteorologia import DatosMeteorologicos

dt = DatosMeteorologicos("resources/datos.txt")
dt.procesar_datos()