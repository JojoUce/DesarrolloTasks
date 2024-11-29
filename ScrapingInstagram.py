import instaloader
import time

# Inicializa Instaloader
loader = instaloader.Instaloader()

# Nombre de usuario de la cuenta desde la cual cargarás la sesión
session_username = "estefania.enriquez19"
target_username = "estefania.enriquez19"  # Nombre de usuario del objetivo

# Carga la sesión guardada
try:
    loader.load_session_from_file(session_username)
    print(f"Sesión cargada correctamente para el usuario: {session_username}")
except Exception as e:
    print(f"No se pudo cargar la sesión: {e}")
    print("Ejecuta un script para guardar la sesión antes de continuar.")
    exit()

# Obtén el perfil objetivo
try:
    profile = instaloader.Profile.from_username(loader.context, target_username)
    print(f"Objetivo: {profile.username} - Seguidores: {profile.followers}")
except Exception as e:
    print(f"Error al cargar el perfil objetivo: {e}")
    exit()

# Iterar sobre los seguidores y obtener su información
try:
    print("Extrayendo seguidores y su cantidad de seguidores...")
    for follower in profile.get_followers():
        try:
            follower_profile = instaloader.Profile.from_username(loader.context, follower.username)
            print(f"{follower.username}: {follower_profile.followers} seguidores")
            time.sleep(20)  # Pausa de 5 segundos entre solicitudes
        except Exception as e:
            print(f"Error al obtener datos del seguidor {follower.username}: {e}")
except Exception as e:
    print(f"Error al iterar sobre los seguidores: {e}")
