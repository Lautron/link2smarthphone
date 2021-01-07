from pushbullet import Pushbullet
from dotenv import load_dotenv
import os, time

load_dotenv()

SECRET_KEY = os.getenv('API_SECRET')

pb = Pushbullet(SECRET_KEY)
links = {
        '78': 'https://clasificados.lavoz.com.ar/avisos/departamentos/4204168/video-visita-virtual-3dor-cochera-subs-aire-y-ventiladores-4r-157',
        '82': 'https://clasificados.lavoz.com.ar/avisos/departamentos/4156755/tres-dormitorios-frente-con-balcon.html',
        '83': 'https://clasificados.lavoz.com.ar/avisos/departamentos/4151835/vendo-departamento-tres-dormitorios.html',
        '84': 'https://clasificados.lavoz.com.ar/avisos/departamentos/4109232/departamento-3-dormitorios-centro.html',
        '85': 'https://clasificados.lavoz.com.ar/avisos/departamentos/4259439/torres-de-castro-barros',
        '86': 'https://clasificados.lavoz.com.ar/avisos/departamentos/4263605/alquilo-depto',
        '92': 'https://clasificados.lavoz.com.ar/avisos/casas/4109174/centro-calle-rioja-259-planta-baja-3-dor.html',
        '96': 'https://clasificados.lavoz.com.ar/avisos/departamentos/4258847/amplio-3-dormitorios-2-banos-patio-montevideo-730',
        '101': 'https://clasificados.lavoz.com.ar/avisos/departamentos/4107040/alquilo-depto-3-dorsin-expensas-b%C2%BA-altos-gral-paz-pje-manuel-vergara-71',
        '103': 'https://clasificados.lavoz.com.ar/avisos/casas/4250224/b%C2%B0-alto-general-paz-casa-esquina-3d-catamarca-esq-gavilan'
        }


for id_num, link in links.items():
    pb.push_link(f'Depto {id_num}', link)
    print(f'Sent: Depto {id_num}')
