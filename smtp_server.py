from aiosmtpd.controller import Controller
from aiosmtpd.smtp import SMTP
from email import message_from_bytes
from flask import Flask, render_template, request
import asyncio

# Custom SMTP handler class
class CustomSMTPHandler:
    async def handle_DATA(self, server, session, envelope):
        print(f"Received message from: {envelope.mail_from}")
        print(f"To: {envelope.rcpt_tos}")
        print(f"Message data:\n{envelope.content.decode('utf-8')}")
        return '250 Message accepted for delivery'

# Global variables for the SMTP server
smtp_controller = None

# Start the SMTP server
def start_smtp_server(host='0.0.0.0', port=1025):
    global smtp_controller
    handler = CustomSMTPHandler()
    smtp_controller = Controller(handler, hostname=host, port=port)
    smtp_controller.start()
    print(f"SMTP server started on {host}:{port}")

# Stop the SMTP server
def stop_smtp_server():
    global smtp_controller
    if smtp_controller:
        smtp_controller.stop()
        smtp_controller = None
        print("SMTP server stopped.")