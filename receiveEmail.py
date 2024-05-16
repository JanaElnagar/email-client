import tkinter as tk
import imaplib
import email

# Create a new Tkinter window
window = tk.Tk()
window.title("Email Client")

# Create a Text widget to display the email content
email_text = tk.Text(window, height=10, width=80)
email_text.pack(fill=tk.BOTH, expand=True)


# Function to retrieve and display emails
def retrieve_emails():
    imap_server = 'imap.gmail.com'
    email_address = 'nwspring94@gmail.com'
    password = 'kbfe gguf unuc xiwe'

    try:
        # Connect to the IMAP server
        imap = imaplib.IMAP4_SSL(imap_server)

        # Login to the email account
        imap.login(email_address, password)

        # Select the mailbox (e.g., INBOX)
        imap.select('Inbox')

        # Search for emails
        _, msgnum = imap.search(None, 'ALL')

        # Retrieve and display the latest 5 emails
        email_ids = msgnum[0].split()
        email_ids.reverse()  # Reverse the order to get the latest emails first
        email_ids = email_ids[:5]  # Get only the first 5 emails

        # Clear the email_text widget
        email_text.delete('1.0', tk.END)

        for msg in email_ids:
            _, data = imap.fetch(msg, "(RFC822)")

            mail = email.message_from_bytes(data[0][1])
            email_text.insert(tk.END, f"Message number: {msg}\n")
            email_text.insert(tk.END, f"From: {mail.get('From')}\n")
            email_text.insert(tk.END, f"To: {mail.get('To')}\n")
            email_text.insert(tk.END, f"BCC: {mail.get('BCC')}\n")
            email_text.insert(tk.END, f"Date: {mail.get('Date')}\n")
            email_text.insert(tk.END, f"Subject: {mail.get('Subject')}\n")
            email_text.insert(tk.END, "Content:\n")

            for part in mail.walk():
                if part.get_content_type() == 'text/plain':
                    email_text.insert(tk.END, part.as_string())
                    email_text.insert(tk.END, "\n\n")

        # Close the connection to the IMAP server
        imap.close()
        imap.logout()

    except imaplib.IMAP4.error as e:
        email_text.insert(tk.END, f"Error: {e}\n")


# Button
retrieve_button = tk.Button(window, text="Retrieve Emails", command=retrieve_emails)
retrieve_button.pack()

window.mainloop()