from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from src.services.email_service import email_service
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/contact", tags=["Contact"])

class ContactForm(BaseModel):
    name: str
    email: EmailStr
    subject: str
    message: str

@router.post("/send")
async def send_contact_email(form_data: ContactForm):
    """
    Send contact form email
    
    - **name**: Sender's full name
    - **email**: Sender's email address
    - **subject**: Email subject
    - **message**: Email message content
    """
    try:
        # Convert to dict
        data = form_data.dict()
        
        # Send email
        success = email_service.send_contact_email(data)
        
        if success:
            return {
                "success": True,
                "message": "Email sent successfully! We'll get back to you soon."
            }
        else:
            raise HTTPException(
                status_code=500,
                detail="Failed to send email. Please try again later."
            )
            
    except Exception as e:
        logger.error(f"Contact form error: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="An error occurred while sending your message."
        )
