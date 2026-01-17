import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import Dict
import logging

logger = logging.getLogger(__name__)

class EmailService:
    def __init__(self):
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587
        self.sender_email = "abhishekgiri1978@gmail.com"
        self.sender_password = "kytasopwdbrgrzou"
    
    def send_contact_email(self, form_data: Dict[str, str]) -> bool:
        """Send contact form email"""
        try:
            # Create message
            message = MIMEMultipart("alternative")
            message["Subject"] = f"SATYA-DRISHTI Contact: {form_data['subject']}"
            message["From"] = self.sender_email
            message["To"] = self.sender_email
            message["Reply-To"] = form_data['email']
            
            # Create HTML content
            html_content = f"""
            <html>
                <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
                    <div style="max-width: 600px; margin: 0 auto; padding: 20px; background: #f8fafc; border-radius: 10px;">
                        <div style="background: linear-gradient(135deg, #1e40af, #3b82f6); padding: 30px; border-radius: 10px 10px 0 0; text-align: center;">
                            <h1 style="color: white; margin: 0; font-size: 28px;">🇮🇳 SATYA-DRISHTI</h1>
                            <p style="color: rgba(255,255,255,0.9); margin: 10px 0 0 0;">New Contact Form Submission</p>
                        </div>
                        
                        <div style="background: white; padding: 30px; border-radius: 0 0 10px 10px;">
                            <h2 style="color: #1e40af; margin-top: 0;">Contact Details</h2>
                            
                            <div style="margin: 20px 0; padding: 15px; background: #eff6ff; border-left: 4px solid #3b82f6; border-radius: 5px;">
                                <p style="margin: 5px 0;"><strong style="color: #1e40af;">Name:</strong> {form_data['name']}</p>
                                <p style="margin: 5px 0;"><strong style="color: #1e40af;">Email:</strong> {form_data['email']}</p>
                                <p style="margin: 5px 0;"><strong style="color: #1e40af;">Subject:</strong> {form_data['subject']}</p>
                            </div>
                            
                            <h3 style="color: #1e40af; margin-top: 25px;">Message:</h3>
                            <div style="background: #f8fafc; padding: 20px; border-radius: 8px; border: 1px solid #e2e8f0;">
                                <p style="margin: 0; white-space: pre-wrap;">{form_data['message']}</p>
                            </div>
                            
                            <div style="margin-top: 30px; padding-top: 20px; border-top: 2px solid #e2e8f0; text-align: center; color: #64748b; font-size: 14px;">
                                <p>This email was sent from the SATYA-DRISHTI contact form</p>
                                <p style="margin: 5px 0;">Reply directly to this email to respond to {form_data['name']}</p>
                            </div>
                        </div>
                    </div>
                </body>
            </html>
            """
            
            # Attach HTML content
            html_part = MIMEText(html_content, "html")
            message.attach(html_part)
            
            # Send email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.send_message(message)
            
            logger.info(f"Contact email sent successfully from {form_data['email']}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to send contact email: {str(e)}")
            return False

email_service = EmailService()
