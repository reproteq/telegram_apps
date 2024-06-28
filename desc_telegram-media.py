from telethon.sync import TelegramClient

# Reemplaza estos valores con los que obtuviste de my.telegram.org

#api_id = 1234567  # Asegúrate de que este sea un número entero
#api_hash = 'abcd1234efgh5678ijkl'  # Asegúrate de que este sea una cadena
#phone = '+1234567890'  # Asegúrate de que este sea tu número de teléfono, incluyendo el código de país

api_id = 'YOUR_API_ID'

api_hash = 'YOUR_API_HASH'

phone = 'YOUR_PHONE_NUMBER'



# Crear y conectar al cliente de Telegram
client = TelegramClient('session_name', api_id, api_hash)
client.start(phone)

async def main():
    # ID del grupo o username del grupo
    group_username = 'Els astronautes Liles Inf.5B'
    #group_username = 'public_group_username'  # Reemplaza esto con el username del grupo si es público

    try:
        # Obtener la entidad del grupo
        entity = await client.get_entity(group_username)
        print(f'ID del grupo "{entity.title}": {entity.id}')
    except Exception as e:
        print(f'Error al obtener el ID del grupo: {e}')

with client:
    client.loop.run_until_complete(main())
