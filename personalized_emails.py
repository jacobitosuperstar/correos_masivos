import smtplib
import imghdr
from email.message import EmailMessage
import csv

with open("prueba.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader)
    datos = list(csv_reader)

#with open("correos.csv") as csv_file:
#    csv_reader = csv.reader(csv_file, delimiter=",")
#    correos_list = list(csv_reader)

#correos = "".join(str(correo) for correo in correos_list)

#print(correos_list[5])

for documento,correo,nombres,apellidos in datos:

    # exchange Sign In
    exchange_sender = "becassapiencia@itm.edu.co"
    exchange_passwd = "Seguimiento2018"

    msg = EmailMessage()
    msg["from"] = exchange_sender
    msg["subject"] = 'comunicado Becas Tecnologías Alcaldía de Medellín'
    msg["Bcc"] = correo

    ### ESTE ES EL CUERPO DEL COMUNICADO QUE VAMOS A ENVIAR ###
    msg.set_content(f"Hola, {nombres} {apellidos} Este es el correo de prueba para probar el envío de contenido dinámico.")

    ### ESTE ES LO QUE SE VA A HACER PARA AGREGAR PDFs A LOS CORREOS ###
    file_acta=f"{documento}_acta.pdf"
    file_diploma=f"{documento}_diploma.pdf"
    files = [file_acta,file_diploma]

    for file in files:
        with open(file,"rb") as f:
            file_data = f.read()
            file_name = f.name

        msg.add_attachment(file_data, maintype="application", subtype="octet-stream", filename=file_name)

    ### ESTO ES LO QUE SE VA HACER PARA AGREGAR IMÁGENES A LOS CORREOS ###

#    files = ["oferta_académica.jpeg"]
#
#    for file in files:
#        with open(file,"rb") as f:
#            file_data = f.read()
#            file_type = imghdr.what(f.name)
#            file_name = f.name
#
#        msg.add_attachment(file_data, maintype="image", subtype=file_type, filename=file_name)

    server = smtplib.SMTP("smtp.office365.com",587)
    server.ehlo()
    server.starttls()
    server.login(exchange_sender, exchange_passwd)

    try:
        server.send_message(msg)
        print (f"email sent to {nombres}")
    except:
        print (f"error sending mail {nombres}")
    server.quit()
