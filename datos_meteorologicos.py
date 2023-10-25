class Datos_meteorologicos:

    def __init__(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo

    def procesar_datos(self) -> tuple[float, float, float, float, str]:
        temperaturas = []
        humedades = []
        presiones = []
        velocidades = []
        direcciones = []

        with open(self.nombre_archivo, "r",) as archivo:
            for linea in archivo:
                partes = linea.split(":")
                clave = partes[0].strip()
                if clave == "Temperatura":
                    temperaturas.append(float(partes[1]))

                elif clave == "Humedades":
                    humedades.append(float(partes[1]))
                elif clave == "Presiones":
                    presiones.append(float(partes[1]))
                elif clave == "Viento":
                    direccion = partes[1].split(",")
                    velocidades.append(float(direccion[0]))
                    direcciones.append(float(partes[1]))

        prom_temperatura = sum(temperaturas)/len(temperaturas)
        prom_humedad = sum(humedades)/len(humedades)
        prom_presion = sum(presiones)/len(presiones)
        prom_velocidad = sum(velocidades)/len(velocidades)
        prom_direccion = sum(direcciones)/len(direcciones)