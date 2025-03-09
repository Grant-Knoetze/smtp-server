# smtp-server
This is an SMTP server for use with Gophish for red teaming operations.
How It Works
The SMTP server listens on port 1025 for incoming emails and logs them to the console.

The Flask web interface allows you to start and stop the SMTP server.

When an email is received, the sender, recipient, and message content are printed to the console.

Enhancements
Logging to a File: Modify the process_message method to log emails to a file instead of the console.

Authentication: Add SMTP authentication if needed.

Integration with GoPhish: Configure GoPhish to use your custom SMTP server by setting the SMTP settings to localhost:1025.


