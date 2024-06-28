#reproteq codigo para descargar todas las fotos de un grupo de telegram.
#instalar python
#instalar pip ,Ve a https://bootstrap.pypa.io/get-pip.py Guarda el archivo get-pip.py luego instalar ejecutando : python get-pip.py 
#instalar telthon con ejecutando : pip install telethon
#identifica el nombre del grupo desde :https://web.telegram.org/#/im?p=Els astronautes Liles Inf.5B
#Ejemplo: Els astronautes Liles Inf.5B es el id:963062987
#Crea una app para poder obtener credenciales desde: https://my.telegram.org/
#Guarda los datos para poder agregarlos al script : https://my.telegram.org/apps
#Credenciales API de Telegram
#api_id = 'YOUR_API_ID'
#api_hash = 'YOUR_API_HASH'
#phone = 'YOUR_PHONE_NUMBER'

#Por ultimo ejecuta este script: python desc_telegram-media.py

from telethon import TelegramClient, sync, events
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import InputMessagesFilterPhotos
import os
 
# Credenciales API de Telegram
# Reemplaza estos valores con los que obtuviste de my.telegram.org
api_id = 1234567  # Asegúrate de que este sea un número entero
api_hash = 'abcd1234efgh5678ijkl'  # Asegúrate de que este sea una cadena
phone = '+3434567890'  # Asegúrate de que este sea tu número de teléfono, incluyendo el código de país +34 para spain


# ID numérico del grupo que deseas obtener
#group_id = 963062987  # Reemplaza con el ID numérico correcto del grupo
# Crear y conectar al cliente de Telegram

# Obtener la ruta del directorio donde está el script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Crear el directorio 'images' en la misma ruta del script si no existe
images_directory = os.path.join(script_directory, 'images')
if not os.path.exists(images_directory):
    os.makedirs(images_directory)

# Crear y conectar al cliente de Telegram
client = TelegramClient('session_name', api_id, api_hash)

async def main():
    try:
        await client.start(phone)

        # Obtener la entidad del grupo usando get_entity
        entity = await client.get_entity(group_id)
        print(f'ID del grupo: {entity.id}')
        print(f'Nombre del grupo: {entity.title}')

        # Descargar las imágenes del grupo
        async for message in client.iter_messages(entity, filter=InputMessagesFilterPhotos):
            if message.photo:
                file_path = await client.download_media(message.photo, images_directory)
                print(f'Imagen guardada en {file_path}')

    except Exception as e:
        print(f'Error: {e}')
    finally:
        await client.disconnect()

if __name__ == "__main__":
    client.loop.run_until_complete(main())
