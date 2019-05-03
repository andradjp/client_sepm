import smtplib


def send_email(rede, subject, content, text):
    sender = 'botnucom@brb.com.br'
    receivers = 'servnucomconectividade@brb.com.br'
    # O conteudo da mensagem não pode ter identação,
    # por esse motivo a mensagem não tem espaços,
    # como pode ser observado abaixo.
    message = '''From: Bot NUCOM <botnucom@brb.com.br>
To: NUCOM Seguranca <servnucomconectividade@brb.com.br>
Subject: {}

{}
Rede: {}
----------------------------------------------------

{}

----------------------------------------------------'''.format(subject, text, rede, content)

    try:
        smtpObj = smtplib.SMTP('mail.brb.com.br')
        smtpObj.sendmail(sender, receivers, message)

    except EOFError as e:
        print('Erro: ' + e)
