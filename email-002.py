""" Use Class Email """
import email_smtp

email = email_smtp.Email()

send_to = 'Bruno Raby <bruno.raby@gmail.com>'
message_body = 'On fera un effort après pour l\'instant c\'est un message de test.\n'

#email.senf_email_to( send_to, message_body )

email.senf_email( message_body )



