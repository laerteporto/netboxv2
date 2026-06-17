import os
import re
import pynetbox

# Configurações do NetBox
NETBOX_URL = "http://192.168.4.82:8000"   # ajuste se estiver usando outro host/porta
NETBOX_TOKEN = "nbt_IyprJWV8xfFn.JbKrMNq8q3VvhEuD2uxhPBwTAGpGts8y0cLDjCSe"        # gere um token no NetBox (Admin → API Tokens)

BASE_PATH = "./devicetype-library/elevation-images"

nb = pynetbox.api(NETBOX_URL, token=NETBOX_TOKEN)

def slugify(value):
    # substitui caracteres inválidos por hífen
    value = value.lower()
    value = re.sub(r'[^a-z0-9_-]+', '-', value)
    return value.strip('-')

def atualizar_ou_criar_device_types():
    print(f"Percorrendo pasta: {BASE_PATH}")
    for root, dirs, files in os.walk(BASE_PATH):
        for f in files:
            print(f"Encontrado arquivo: {os.path.join(root, f)}")

            if not f.lower().endswith((".png", ".jpg", ".jpeg", ".svg")):
                print(" → Ignorado (não é imagem suportada)")
                continue

            model_name = os.path.splitext(f)[0]
            manufacturer_name = os.path.basename(root)

            print(f" → Modelo: {model_name}, Fabricante: {manufacturer_name}")

            manufacturer = nb.dcim.manufacturers.get(name=manufacturer_name)
            if not manufacturer:
                print(f" → Fabricante não encontrado, criando: {manufacturer_name}")
                manufacturer = nb.dcim.manufacturers.create({
                    "name": manufacturer_name,
                    "slug": slugify(manufacturer_name)
                })

            device_type = nb.dcim.device_types.get(model=model_name, manufacturer_id=manufacturer.id)

            image_path = os.path.relpath(os.path.join(root, f), BASE_PATH)
            image_url = f"/static/elevation-images/{image_path}"

            if device_type:
                print(f" → Atualizando {model_name} com imagem {image_url}")
                device_type.update({
                    "custom_fields": {
                        "elevation_image": image_url
                    }
                })
            else:
                print(f" → Criando novo device type: {model_name}")
                nb.dcim.device_types.create({
                    "manufacturer": manufacturer.id,
                    "model": model_name,
                    "slug": slugify(model_name),
                    "custom_fields": {
                        "elevation_image": image_url
                    }
                })

if __name__ == "__main__":
    atualizar_ou_criar_device_types()
