import config.func as conf

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Email:

    def __init__( self ):
        # Configuration du serveur SMTP
        configuration = conf.read_configuration( 'email_smtp.json' )
        self.smtp_server = configuration.get( 'SMTP_SERVER', '')
        self.port = configuration.get( 'PORT', 587)  
        self.username = configuration.get( 'USERNAME', '') 
        self.password = configuration.get( 'PASSWORD', '')
        self.send_to = configuration.get( 'SEND_TO', '')

    def senf_email( self, message_body, email_subject="Système de surveillance des marchés financiés" ):
        # Créer le message
        msg = MIMEMultipart()
        msg['From'] = self.username
        msg['To'] = self.send_to
        msg['Subject'] = email_subject

        # Corps du message
        msg.attach( MIMEText( message_body, 'plain') )

        # Connexion au serveur SMTP
        with smtplib.SMTP(self.smtp_server, self.port) as server:
            server.starttls()  # Activer le chiffrement TLS
            server.login(self.username, self.password)  # Authentification
            server.sendmail(self.username, self.send_to, msg.as_string())  # Envoi de l'e-mail
            print('E-mail send with success')

    def senf_email_to( self, send_to, message_body, email_subject="Système de surveillance des marchés financiés" ):
        # Créer le message
        msg = MIMEMultipart()
        msg['From'] = self.username # f"Stock Market <{self.username}>"
        msg['To'] = send_to
        msg['Subject'] = email_subject

        # Corps du message
        msg.attach( MIMEText( message_body, 'plain') )

        # Connexion au serveur SMTP
        with smtplib.SMTP(self.smtp_server, self.port) as server:
            server.starttls()  # Activer le chiffrement TLS
            server.login(self.username, self.password)  # Authentification
            server.sendmail(self.username, send_to, msg.as_string())  # Envoi de l'e-mail
            print('E-mail send with success')