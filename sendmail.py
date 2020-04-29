import smtplib
import config


class SendMail:
    def __init__(self, ans, asin, url, productName):
        self.url = url
        self.ans = ans
        self.asin = asin
        self.emailaddress = config.GMAIL_EMAIL
        self.title = productName

    def sendemail(self):
        GMAIL_USERNAME = config.GMAIL_USERNAME
        GMAIL_PASSWORD = config.GMAIL_PASSWORD

        recipient = self.emailaddress
        body_of_email = self.ans
        email_subject = self.asin + ' Product is in stock'

        # creates SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)

        # start TLS for security
        s.starttls()

        # Authentication
        s.login(GMAIL_USERNAME, GMAIL_PASSWORD)

        # message to be sent
        headers = "\r\n".join(["from: " + GMAIL_USERNAME,
                               "subject: " + email_subject,
                               "to: " + recipient,
                               "mime-version: 1.0",
                               "content-type: text/html"])

        content = headers + "\r\n\r\n" + body_of_email + " " + self.title[0] + " " + self.url
        s.sendmail(GMAIL_USERNAME, recipient, content)
        s.quit()