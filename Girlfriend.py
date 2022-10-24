from datetime import datetime
import pywhatkit as pwt
import random
import time

rng = random.randint(0,30)

number = "+5215537717999"

message_moorning = [
    "buenos días amor 🥰",
    "Ya despiertate guapa ❤️❤️❤️",
    "amor ten un bonito día 🥰",
    "Feliz día hermosa 🥰🥰🥰",
    "como amanecio mi princesa hermosa 🥰 ???"]

message_night  = [
    "buenas noches bb te amo 😘<3",
    "Buenas noches mi amor 🥰",
    "ya me voy a dormir amor, te amo 🥰",
    "me voy a dormir te veo mañana amor 😍",
    "me voy hechar un sueñito amor, si me quedo dormido sulces sueños bb 😍😍😍"
    ]
message_work = [
    "Ya me voy al trabajo bebe, te veo en la noche ❤️❤️❤️",
    "Me voy a trabajar amor <3",
    "Ya voy a la oficina amor <3",
]
message_return = [
    "Hola amor ya llegue a mi casa"
]
message_home = [
    "Amor ya me voy a la casa 🥰🥰🥰",
    "Cariño ya voy de regreso 🥰🥰🥰",
    "Hola amor ya voy para la casa 🥰🥰🥰",
    "Voy de regreso amor 🥰🥰🥰"
]


def good_morning_(number,mensaje_, hora, minuto):
    try:
        pwt.sendwhatmsg(number, mensaje_, hora, minuto, 40)
        return print ("Mensaje buenos días enviado con exito")
    except:
        print("error al enviar mensaje de buenos días")

def go_to_work_(number,mensaje_, hora, minuto):
    try:
        pwt.sendwhatmsg(number, mensaje_, hora, minuto, 40)
        return print ("Mensaje voy al trabajo enviado con exito")
    except:
        print("error al enviar mensaje al trabajo")

def go_to_home_(number,mensaje_, hora, minuto):
    try:
        pwt.sendwhatmsg(number, mensaje_, hora, minuto, 40)
        return print ("Mensaje voy a la casa enviado con exito")
    except:
        print("error al enviar mensaje de regreso a casa")

def return_to_home_(number,mensaje_, hora, minuto):
    try:
        pwt.sendwhatmsg(number, mensaje_, hora, minuto, 40)
        return print ("Mensaje he llegado a casa enviado con exito")
    except:
        print("error al enviar mensaje de llegue a casa a casa")

def good_nigh_(number,mensaje_, hora, minuto):
    try:
        pwt.sendwhatmsg(number, mensaje_, hora, minuto, 40)
        return print ("Mensaje buenas noches enviado con exito")
    except:
        print("error al enviar mensaje de buenas noches")

now = datetime.now()
hora = now.hour
hora

while hora < 25:
    if hora == 6:
        good_morning_(number,message_moorning[random.randint(0,len(message_moorning))], hora, random.randint(1,15))
    elif hora == 7:
        go_to_work_(number,message_work[random.randint(0,len(message_work))], hora, random.randint(1,25))
    elif hora == 18:
        go_to_home_(number,message_home[random.randint(0,len(message_home))], hora, random.randint(1,10))
    elif hora == 20:
        return_to_home_(number,message_return, hora, random.randint(1,30))
    elif hora == 22:
        good_nigh_(number,message_night[random.randint(0,len(message_night))], hora, random.randint(1,30))
    else:
        hora = now.hour
        time.sleep(60)

