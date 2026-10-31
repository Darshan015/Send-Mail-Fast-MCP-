from fastmcp import FastMCP
import smtplib
from email.message import EmailMessage

mcp = FastMCP("Send Email MCP")

sender_email = "darshangowda1658@gmail.com"
app_password = "fbnh tucw jecd tpeq"

def __Send(email:str, subject:str, body:str) -> str:
    
    # Create email message
    message = EmailMessage()
    message["From"] = sender_email
    message["To"] = email
    message["Subject"] = subject
    message.set_content(body)
    try:
        # Connect to SMTP server
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, app_password)

            # Send email
            server.send_message(message)

        return "Email sent successfully!"

    except Exception as e:
        return f"Failed to send email: {e}"


@mcp.tool
def __send_mail(email,subject,body):
    """Tool which takes email, subject and body as a input and send a mail to the specified 'email'"""
    return __Send(email,subject,body)

mcp.run(transport="streamable-http")