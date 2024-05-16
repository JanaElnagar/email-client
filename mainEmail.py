from tkinter import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# main screen
master = Tk()
master.title('Python Mail App')

# Functions
def send():
    try:
        username = temp_username.get()
        password = temp_pass.get()
        to = temp_receiver.get()
        subject = temp_subject.get()
        body = bodyEntry.get(1.0, 'end')  # Get the body from Text widget
        if username == '' or password == '' or to == '' or subject == '' or body == '':
            notif.config(text="All fields are required!", fg="red")
            return
        else:
            message = MIMEMultipart()
            message['From'] = username
            message['To'] = to
            message['Subject'] = subject

            message.attach(MIMEText(body, 'plain'))

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(username, password)
            server.sendmail(username, to, message.as_string())
            server.quit()
            notif.config(text="Email sent successfully!", fg="green")
    except:
        notif.config(text="Error sending email!", fg="red")


def reset():
    usernameEntry.delete(0, 'end')
    passEntry.delete(0, 'end')
    receiverEntry.delete(0, 'end')
    subjectEntry.delete(0, 'end')
    bodyEntry.delete('1.0', 'end')  # Clear the text in the Text widget


# Graphics
titleLabel = Label(master, text="Email App", font=('Calibri', 15))
titleLabel.grid(row=0, column=0, columnspan=2, sticky=N)  # Span across two columns
Label(master, text="Use the form below to send an email", font=('Calibri', 11)).grid(row=1, column=0, columnspan=2, sticky=W, padx=5)  # Span across two columns

Label(master, text="Email", font=('Calibri', 11)).grid(row=2, column=0, sticky=W, padx=5, pady=(10, 0))

Label(master, text="Password", font=('Calibri', 11)).grid(row=3, column=0, sticky=W, padx=5, pady=(5, 0))

Label(master, text="To", font=('Calibri', 11)).grid(row=4, column=0, sticky=W, padx=5)
Label(master, text="Subject", font=('Calibri', 11)).grid(row=5, column=0, sticky=W, padx=5)
Label(master, text="Body", font=('Calibri', 11)).grid(row=6, column=0, sticky=W, padx=5)
notif = Label(master, text="", font=('Calibri', 11))
notif.grid(row=7, column=0, sticky=S, padx=5)

# Storage
temp_username = StringVar()
temp_pass = StringVar()
temp_receiver = StringVar()
temp_subject = StringVar()
temp_body = StringVar()

# Entries
usernameEntry = Entry(master, textvariable=temp_username)
usernameEntry.grid(row=2, column=1, padx=5, pady=(10, 5))
passEntry = Entry(master, show='*', textvariable=temp_pass)
passEntry.grid(row=3, column=1, padx=5, pady=(0, 5) )
receiverEntry = Entry(master, textvariable=temp_receiver)
receiverEntry.grid(row=4, column=1, padx=5, pady=5)
subjectEntry = Entry(master, textvariable=temp_subject)
subjectEntry.grid(row=5, column=1, padx=5, pady=5)
bodyEntry = Text(master, height=10, width=30)  # Use Text widget instead of Entry for bigger text boxw
bodyEntry.grid(row=6, column=1, padx=5, pady=5, sticky=W)

# Buttons
Button(master, text="Send", command=send).grid(row=8, column=0, sticky=W, pady=15, padx=5)
Button(master, text="Reset", command=reset).grid(row=8, column=1, sticky=W, pady=15, padx=5)

master.mainloop()