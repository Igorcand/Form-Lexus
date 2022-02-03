import smtplib 
from email.mime.text  import MIMEText

def send_email(customer, dealer, rating, comments):
    #You need to register in the MailTrap
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = 'your login'
    password = 'your password'
    message = f"""<h3> New feedback Submission </h3>
    <ul>
        <li> Customer: {customer}</li> 
        <li> Dealer: {dealer}</li>
        <li> Rating: {rating}</li>
        <li> Comments: {comments}</li>
    </ul>"""

    sender_email = 'exemple_sender01@exemple.com'
    receive_email = 'exemple_receive02@exemple.com'

    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Lexus Feedback'
    msg['From'] = sender_email
    msg['To'] = receive_email


    #Send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receive_email, msg.as_string())
