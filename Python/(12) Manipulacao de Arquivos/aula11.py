# Aula 11 - Criando e Disparando Email

import smtplib
import ssl
import email.message

de = 'teste@gmail.com'
para = 'teste2@email.com'
senha = '123'
mensagem = '''
   Olá, mensagem de teste
'''

# smtp.gmail.com
# smtp-mail.outlook.com
# smtp.mail.yahoo.com
'''conexao = smtplib.SMTP('smtp.gmail.com', 587)
conexao.ehlo()
conexao.starttls()  # Inicia a criptografia
conexao.login(de, senha)
conexao.sendmail(de, para, msg)
conexao.quit()  # Encerra a conexão'''

'''context = ssl.create_default_context()
with smtplib.SMTP('smtp.gmail.com', 587) as conexao:
   conexao.ehlo()
   conexao.starttls(context=context)  # Inicia a criptografia
   conexao.login(de, senha)
   conexao.sendmail(de, para, msg)
   conexao.quit()  # Encerra a conexão'''

msg = email.message.Message()
setor = 'B'
msg['Subject'] = f'Planilha Financeiro para departamento: {setor}'

nome = 'Equipe do Financeiro'
body = f'''
   <p>Olá, {nome}</p> 
   <p>Segue em anexo a planilha com resultados desse Mês.</p>

   <p>Atenciosamente,</p>
   <p>Gerente ADM</p>
'''
msg['From'] = 'teste@gmail.com'
msg['To']= 'teste2@email.com'
password = '123'
msg.add_header('Content-Type', 'text/html')
msg.set_payload(body)

context = ssl.create_default_context()
with smtplib.SMTP('smtp.gmail.com', 587) as conexao:
   conexao.ehlo()
   conexao.starttls(context=context)  # Inicia a criptografia
   conexao.login(msg['From'], password)
   conexao.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))
   conexao.quit()  # Encerra a conexão