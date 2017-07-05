from lxml import html
import requests
import time
import email
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

MY_ADDRESS = 'ianoheir@gmail.com'
PASSWORD = 'Taking out for obvious reasons'

def sendEmail():
    # set up the SMTP server
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("ianoheir@gmail.com", "Taking out or obvious reasons")



        msg = MIMEMultipart()
        message="On sale"

        # setup the parameters of the message
        msg['From']=MY_ADDRESS
        msg['To']='ianoheir@email.arizona.edu'
        msg['Subject']="Tickets on sale"

        # add in the message body
        msg.attach(MIMEText(message, 'plain'))

        # send the message via the server set up earlier.
        s.send_message(msg)
        del msg

    # Terminate the SMTP session and close the connection
        s.quit()



def main():
    print("working")
    while (True):
        #Set a timer to check the site every 15 seconds and if it gets updated with
        #the 7th day, I can buy the tickets
        time.sleep(15)
        page = requests.get('https://roadhousecinemas.com/movie-theater/scottsdale')
        tree = html.fromstring(page.content)
        chairs = tree.xpath('//*[@id="nowPlaying"]/div[1]/div/div[2]/ul/li/@class')
        if("772017 sbDateItem" in chairs):
            sendEmail()
            exit()
        print(chairs)



if __name__ == '__main__':
    main()
