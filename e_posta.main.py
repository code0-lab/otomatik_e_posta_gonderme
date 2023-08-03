import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, receiver_email, subject, message):
    smtp_server = "smtp.gmail.com"  
    smtp_port = 587
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
    except Exception as e:
        print("E-posta sunucusuna bağlanma hatası:", str(e))
    return



    
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(message, "plain"))


    try:
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print("E-posta gönderildi.")
    except Exception as e:
        print("E-posta gönderme hatası:", str(e))


    server.quit()
if __name__ == "__main__":
    sender_email = input("e_mailiniz: ")
    sender_password = input("şifreniz: ")
    receiver_email = input("Alıcının_e_maili: ")
    subject = input("Konu: ")
    message = input("Mesajınız: ")

    send_email(sender_email, sender_password, receiver_email, subject, message)
