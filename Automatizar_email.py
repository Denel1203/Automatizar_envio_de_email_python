import smtplib
import email.message 

# funcao de enviar o email
# Corpo do email, codigo em html
def enviar_email():              
    corpo_email='''                                                
    <p>Paragrafo1</p>           
    <p>Paragrafo2</p>
    '''

    msg=email.message.Message()             #criacao do email
    msg['Subject']= 'Assunto'               #Aqui sera o assunto enviado
    msg['From']= 'remetente'                #O email da pessoal ou empresa que vai enviar
    msg['To']= 'destinario'                 #destinatorio
    password= 'Senha'                       #A senha do remetente do email
    msg.add_header('Content-Type', 'text/html')  
    msg.set_payload(corpo_email)

    s= smtplib.SMTP('smtp.gmail.com:587')  #Gral de seguracao da conexao        
    s.starttls()

    s.login(msg['From'],password)           #Faz o login
    s.sendmail(msg['From'],[msg['To']],msg.as_string().encode('utf-8')) #Envia a msg
    print('Email enviado')

enviar_email()