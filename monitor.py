import requests
from firebase import firebase
from string import maketrans
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

firebase = firebase.FirebaseApplication('https://pushtest-eb14f.firebaseio.com/')

cname = ['http://speedtester-dev.elasticbeanstalk.com/health.html',
         'http://speedtesterprod.elasticbeanstalk.com/health.html',
         #'http://mauasappconnecti-dev.us-west-2.elasticbeanstalk.com/health.html',
         'http://fileconverter.elasticbeanstalk.com/health.html',
         'http://fileconverter-dev.elasticbeanstalk.com/health.html',
         #'http://otosom-dev.us-west-2.elasticbeanstalk.com/health.html',
         'http://pdfbaron.us-west-2.elasticbeanstalk.com/health.html',
         #'http://pdfbaron-dev.us-west-2.elasticbeanstalk.com/health.html',
         'http://pdfcruncher.us-west-2.elasticbeanstalk.com/health.html',
         'http://pdfcruncher-dev.us-west-2.elasticbeanstalk.com/health.html',
         'http://pdfpronto.us-west-2.elasticbeanstalk.com/health.html',
         #'http://pdfprontodev.us-west-2.elasticbeanstalk.com/health.html',
         'http://pdftoolkit.us-west-2.elasticbeanstalk.com/health.html',
         'http://videoconverter.elasticbeanstalk.com/health.html',
         'http://videoconverter-dev.elasticbeanstalk.com/health.html',
         'http://speedtestervpc-env.us-west-2.elasticbeanstalk.com/health.html',
         'http://apiconnecti-dev.us-east-1.elasticbeanstalk.com/health.html',
         'http://apiconnecti-env.us-east-1.elasticbeanstalk.com/health.html',
         'http://appconnecti-dev.us-east-1.elasticbeanstalk.com/health.html',
         'http://appconnecti-env.us-east-1.elasticbeanstalk.com/health.html',
         'http://beautifulcalendar.elasticbeanstalk.com/health.html',
         'http://beautifulcalendar-dev.elasticbeanstalk.com/health.html',
         'http://foxycalendar-dev.us-east-1.elasticbeanstalk.com/health.html',
         'http://foxycalendar-env.us-east-1.elasticbeanstalk.com/health.html',
         'http://coloring-dev.us-east-1.elasticbeanstalk.com/health.html',
         'http://coloring-prod.us-east-1.elasticbeanstalk.com/health.html',
         'http://minisites-qa.us-east-1.elasticbeanstalk.com/health.html',
         'http://nexus.us-east-1.elasticbeanstalk.com/health.html',
         'http://productsenv.us-east-1.elasticbeanstalk.com/health.html',
         'http://productsenv-dev.us-east-1.elasticbeanstalk.com/health.html',
         'http://sendmanyfilesweb-prod.elasticbeanstalk.com/#/sendFiles/health.html',
         #sendmanyfileswrk-prod worker
         'http://terser-bouncer.us-east-1.elasticbeanstalk.com/health.html',
         'http://widgetsystem-dev.elasticbeanstalk.com/#/health.html',
         'http://widgetsystem-env.elasticbeanstalk.com/health.html',
         'http://yeti.us-east-1.elasticbeanstalk.com/health.html',
         ]

problemcnamearray = []
for index in cname:
    resultcode = requests.get(index)
    responsetostring = str(resultcode)
    if '200' not in responsetostring:
        problemcnamearray.append(index)


cnamearraynobrackets = (",".join(repr(e) for e in problemcnamearray))
stringarray = str(cnamearraynobrackets)
result = firebase.patch('/apps', {'condition': str(stringarray)})


# writetofile = open('Downapps.txt', 'w')
# for item in problemcnamearray:
#     print >> writetofile, item
#
# recipients = ['shahar@somoto.net']
# emaillist = [elem.strip().split(',') for elem in recipients]
# msg = MIMEMultipart()
# msg['Subject'] = 'There is an issue with elastic beanstalk.'
# msg['From'] = 'shahar@somoto.net'
# msg['Reply-to'] = 'shahar@somoto.net'
#
# msg.preamble = 'Multipart massage.\n'
#
# part = MIMEText("The following apps are throwing exceptions:\n" + str(problemcnamearray))
# msg.attach(part)
#
# server = smtplib.SMTP("smtp.gmail.com:587")
# server.ehlo()
# server.starttls()
# server.login("shahar@somoto.net", "Jawa350640")
#
# server.sendmail(msg['From'], emaillist, msg.as_string())

