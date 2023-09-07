import smtplib
import email

email_addresses = ["johndoe@example.com", "janedoe@example.com"]
sender_email = 'example@mail.com'
password = 'password'

message = email.message.EmailMessage()
message.set_content("Example of an Automated Mail")
message['Subject'] = "Automated Email"
message['From'] = sender_email
message['To'] = email_addresses

smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.starttls()

smtp.login(sender_email, password)

smtp.sendmail(sender_email, email_addresses, message.as_string())


smtp.quit()
