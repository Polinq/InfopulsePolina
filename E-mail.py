import smtplib
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.starttls()
smtpObj.login('polinq@gmail.com','**********')
smtpObj.sendmail("polinq@gmail.com","elpiankova@gmail.com","I did it!")
smtpObj.quit()
