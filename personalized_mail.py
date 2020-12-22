import smtplib
import imghdr
from email.message import EmailMessage
import csv
import os

with open("once_am.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=";")
    next(csv_reader)
    datos = list(csv_reader)

#with open("correos.csv") as csv_file:
#    csv_reader = csv.reader(csv_file, delimiter=",")
#    correos_list = list(csv_reader)

#correos = "".join(str(correo) for correo in correos_list)

#print(correos_list[5])

for Programa,Nombre,Correo,Documento in datos:

    ## SIGN IN ##
    EMAIL_SENDER = os.environ["EMAIL_SENDER"]
    EMAIL_PASSWORD = os.environ["EMAIL_PASSWORD"]
    server = smtplib.SMTP(os.environ["EMAIL_HOST"],587)

    msg = EmailMessage()
    msg["from"] = EMAIL_SENDER
    msg["subject"] = f"Grados {Nombre}"
    msg["Bcc"] = Correo

    ### ESTE ES EL CUERPO DEL COMUNICADO QUE VAMOS A ENVIAR ###
    msg.set_content(f"Hola, {Nombre} Este es el correo de prueba para probar el envío de contenido dinámico.")

    ### ESTE ES LO QUE SE VA A HACER PARA AGREGAR PDFs A LOS CORREOS ###
    file_acta=f"../Acta{Documento}.pdf"
    file_diploma=f"../Diploma{Documento}.pdf"
    files = [file_acta,file_diploma]

    for file in files:
        with open(file,"rb") as f:
            file_data = f.read()
            file_name = f.name

        msg.add_attachment(file_data, maintype="application", subtype="octet-stream", filename=file_name)

    ### ESTO ES LO QUE SE VA HACER PARA AGREGAR IMÁGENES A LOS CORREOS ###

    files = ["felicidades_egresados.jpg"]

    for file in files:
        with open(file,"rb") as f:
            file_data = f.read()
            file_type = imghdr.what(f.name)
            file_name = f.name

        msg.add_attachment(file_data, maintype="image", subtype=file_type, filename=file_name)

    server.ehlo()
    server.starttls()
    server.login(EMAIL_SENDER, EMAIL_PASSWORD)

    try:
        server.send_message(msg)
        print (f"email sent to {Nombre}")
    except:
        print (f"error sending mail {Nombre}")
    server.quit()

print("Finalizado el envío de información de prueba")
