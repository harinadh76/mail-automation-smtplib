# mail-automation-smtplib
# Rain Alert 

Python Mail automation using smtplib library..

For Gmail - smtp.gmail.com
For Yahoo - smtp.mail.yahoo.com

Sends a mail during rainy weather

MY_EMAILID : your gmail or yahoo mail id
PASSWORD : gmail password or yahoo mail password

if it shows any error then add port = 587 

`with smtplib.SMTP("smtp.gmail.com", port=587) as connection:`

