"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""

import pandas as pd
import os 


def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """
    carpeta_salida = "files/output/"
    os.makedirs(carpeta_salida, exist_ok=True)

    archivo_salida = os.path.join(carpeta_salida, "solicitudes_de_credito.csv")

    df = pd.read_csv("files/input/solicitudes_de_credito.csv", sep=";", index_col=0)

    fechas_formato_ano_primero = pd.to_datetime(df["fecha_de_beneficio"], format="%Y/%m/%d", errors="coerce")
    filas_con_error = fechas_formato_ano_primero.isna()
    fechas_formato_dia_primero = pd.to_datetime(df.loc[filas_con_error, "fecha_de_beneficio"], format="%d/%m/%Y", errors="coerce")
    fechas_formato_ano_primero.loc[filas_con_error] = fechas_formato_dia_primero
    df["fecha_de_beneficio"] = fechas_formato_ano_primero

    df["sexo"] = df["sexo"].str.lower()
    
    df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"].str.lower()

    df["monto_del_credito"] = df["monto_del_credito"].str.replace(".00", "")
    df["monto_del_credito"] = df["monto_del_credito"].str.replace(r"[,. $]", "", regex=True)

    columnas = ["barrio", "línea_credito", "idea_negocio", "monto_del_credito"]
    for columna in columnas:
        if columna in df.columns:
            df[columna] = df[columna].str.lower().str.replace(r"[-_]", " ", regex=True)

    df = df.drop_duplicates()
    
    df = df.dropna()

    df.to_csv(archivo_salida, index=False, sep=";")

if __name__ == "__main__":
    pregunta_01()