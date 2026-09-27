import os

# 1. Configura el nombre base que quieres (ej. paso_)
prefijo = "seguidor_"

# 2. Obtenemos todas las imágenes de la carpeta actual y las ordenamos
archivos = [f for f in os.listdir('.') if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
archivos.sort() # Mantiene el orden original (alfabético o por fecha)

print(f"🔄 Se encontraron {len(archivos)} imágenes. Iniciando proceso...\n")

# 3. Renombramos cada archivo
for contador, archivo in enumerate(archivos, start=1):
    # Extraemos la extensión original (.jpg, .png, etc.)
    extension = os.path.splitext(archivo)[1]
    
    # Creamos el nuevo nombre. El '02d' fuerza que los números menores a 10 tengan un 0 (01, 02...)
    nuevo_nombre = f"{prefijo}{contador:02d}{extension}"
    
    # Renombramos físicamente el archivo
    os.rename(archivo, nuevo_nombre)
    print(f"✅ {archivo}  -->  {nuevo_nombre}")

print("\n🎉 ¡Renombrado completado con éxito!")