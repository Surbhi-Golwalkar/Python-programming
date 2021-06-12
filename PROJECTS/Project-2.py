import smtplib as s
ob = s.SMTP("smtp.gmail.com",587)
ob.starttls()
ob.login('surbhi.golwalkar2904@gmail.com','SuRbHi@999#*')
subject = "PROJECT-2"
body = "Sending e-mail using python"
message = "Subject:{}\n\n{}".format(subject,body)
listofaddress = ['surbhi.golwalkar2904@gmail.com','shruti.golwalkar0109@gmail.com','ajay.golwalkar2016@gmail.com']
ob.sendmail('surbhi.golwalkar2904',listofaddress,message)
print("Mail Sent Successfully")
ob.quit()