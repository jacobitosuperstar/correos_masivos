import smtplib
from email.message import EmailMessage
import csv

def send_email(send_to):
    # exchange Sign In
    exchange_sender = "becassapiencia@itm.edu.co"
    exchange_passwd = "Seguimiento2018"

    msg = EmailMessage()
    msg["from"] = exchange_sender
    msg["subject"] = 'comunicado Becas Tecnologías Alcaldía de Medellín'
    msg["Bcc"] = send_to
    msg.set_content("pdf sapiencia")

    files = ["comunicado_becas_sapiencia.pdf"]

    for file in files:
        with open(file,"rb") as f:
            file_data = f.read()
            file_name = f.name

        msg.add_attachment(file_data, maintype="application", subtype="octet-stream", filename=file_name)

    server = smtplib.SMTP("smtp.office365.com",587)
    server.ehlo()
    server.starttls()
    server.login(exchange_sender, exchange_passwd)

    try:
        server.send_message(msg)
        print ('email sent')
    except:
        print ('error sending mail')
    server.quit()

with open("correos.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    correos_list = list(csv_reader)

#correos = "".join(str(correo) for correo in correos_list)

#print(correos_list[5])

for correo in correos_list:
    send_email(correo)
