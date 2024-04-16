import smtplib  # an email library that covers email client specific for Google Mail (Gmail)
import ssl  # a library for establishing secure communication over a computer network
# import os  # a library for supporting the "ENVIRONMENT VARIABLE" for securing a password


def send_email(message, Instructor_name, email):
    receiver = ''
    host = "smtp.gmail.com"
    port = 465

    username = 'autoreply1234bot@gmail.com'
    password = "ebaqrjiingqzumwx"
    if Instructor_name == 'Your Name':
        receiver = email
    elif Instructor_name == 'Ayrton John V. Bantay':
        receiver = 'ayrtonjohn.bantay@vsu.edu.ph'
    elif Instructor_name == 'Vic Angelo L. Impas':
        receiver = 'vicangelo.impas@vsu.edu.ph'
    elif Instructor_name == 'Iñigo Ezekiel Cabase':
        receiver = 'inigo.cabase@vsu.edu.ph'
    elif Instructor_name == 'Edgardo C. Ochavillo':
        receiver = 'edgardo.ochavillo@vsu.edu.ph'
    elif Instructor_name == 'Ronard G. Paña':
        receiver = 'ronard.pana@vsu.edu.ph'
    else:
        pass

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

