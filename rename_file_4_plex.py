import imdb
import os
import shutil

def obtener_titulo(imdb_id):
    ia = imdb.IMDb()
    movie = ia.get_movie(imdb_id)
    title = movie.get('title', 'Desconocido')
    return title

def main(imdb_id, video_file):
    # Obtener el título de la película
    titulo_original = obtener_titulo(imdb_id)
    
    # Obtener el año de producción de la película
    ia = imdb.IMDb()
    movie = ia.get_movie(imdb_id)
    year = movie.get('year', 'Desconocido')

    # Crear el nombre de la carpeta y el nuevo nombre del archivo de vídeo
    nombre_carpeta = f"{titulo_original} ({year})"
    nuevo_nombre_video = f"{titulo_original} ({year}).mp4"

    # Crear la carpeta
    os.makedirs(nombre_carpeta, exist_ok=True)

    # Mover el archivo de vídeo a la carpeta con el nuevo nombre
    shutil.move(video_file, os.path.join(nombre_carpeta, nuevo_nombre_video))

if __name__ == "__main__":
    imdb_id = input("Introduce el ID de IMDb de la película: ")
    video_file = input("Introduce la ruta del archivo de vídeo: ")
    main(imdb_id, video_file)