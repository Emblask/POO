class DatosMeteorologicos:
    def __init__(self, nombre_archivo:str):
        self.nombre_archivo = nombre_archivo

    def procesar_datos(self) -> tuple[float, float, float, float, str]:
        temperatura_promedio = 0
        humedad_promedio = 0
        presión_promedio = 0
        velocidad_promedio = 0
        direccion_promedio = 0
        contador_temperaturas = 0
        contador_humedades = 0
        contador_presiones = 0
        contador_velocidades = 0
        contador_direcciones = 0
        diferencia_minima = float('inf')
        direcciones_a_grados = {
            "N": 0,
            "NNE": 22.5,
            "NE": 45,
            "ENE": 67.5,
            "E": 90,
            "ESE": 112.5,
            "SE": 135,
            "SSE": 157.5,
            "S": 180,
            "SSW": 202.5,
            "SW": 225,
            "WSW": 247.5,
            "W": 270,
            "WNW": 292.5,
            "NW": 315,
            "NNW": 337.5
        }
        with open(self.nombre_archivo, 'r') as archivo:
            for linea in archivo:
                if "Temperatura" in linea:
                    contador_temperaturas += 1
                    temperatura_promedio += float(linea.split(': ')[1].strip())
                if "Humedad" in linea:
                    contador_humedades += 1
                    humedad_promedio += float(linea.split(': ')[1].strip())
                if "Presion" in linea:
                    contador_presiones += 1
                    presión_promedio += float(linea.split(': ')[1].strip())
                if "Viento" in linea:
                    contador_velocidades += 1
                    contador_direcciones += 1
                    velocidad_promedio += float(linea.split(': ')[1].split(',')[0].strip())
                    direccion_actual = linea.split(': ')[1].split(',')[1].strip()
                    direccion_promedio += direcciones_a_grados[direccion_actual]
                
        for direccion, grados in direcciones_a_grados.items():
            diferencia = abs(grados - direccion_promedio)
            if diferencia < diferencia_minima:
                diferencia_minima = diferencia
                direccion_cercana = direccion

        print (f"Temperatura promedio: {round(temperatura_promedio / contador_temperaturas, 2)}")
        print (f"Humedad promedio: {round(humedad_promedio / contador_humedades, 2)}")
        print (f"Presión promedio: {round(presión_promedio / contador_presiones, 2)}")
        print (f"Velocidad promedio: {round(velocidad_promedio / contador_velocidades, 2)}")
        print (f"Dirección promedio: {direccion_cercana}")
            

                    
        