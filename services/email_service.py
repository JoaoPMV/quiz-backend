import smtplib
from email.message import EmailMessage
from flask import current_app

def send_reset_email(to_email, reset_token):
    frontend_url = current_app.config.get("FRONTEND_URL", "http://localhost:5173")
    reset_link = f"{frontend_url}/reset-password?token={reset_token}"

    from_email = current_app.config["MAIL_FROM"]
    host = current_app.config["MAIL_SERVER"]
    port = int(current_app.config["MAIL_PORT"])
    username = current_app.config["MAIL_USERNAME"]
    password = current_app.config["MAIL_PASSWORD"]
    use_tls = str(current_app.config.get("MAIL_USE_TLS", "true")).lower() == "true"

    subject = "Redefinicao de senha | Password reset"

    text_body = f"""PT-BR
Ola!

Recebemos uma solicitacao para redefinir sua senha do Quiz English.

Link para redefinir:
{reset_link}

Este link expira em 1 hora.
Se voce nao fez esta solicitacao, ignore este email.

------------------------------------------------------------

EN
Hello!

We received a request to reset your Quiz English password.

Reset link:
{reset_link}

This link expires in 1 hour.
If you did not request this, you can ignore this email.
"""

    html_body = f"""
<!doctype html>
<html>
  <body style="margin:0;padding:0;background:#f6f9fc;font-family:Arial,sans-serif;color:#1f2937;">
    <table width="100%" cellpadding="0" cellspacing="0" style="padding:24px 0;">
      <tr>
        <td align="center">
          <table width="620" cellpadding="0" cellspacing="0" style="background:#ffffff;border-radius:12px;padding:28px;">
            <tr>
              <td>
                <h2 style="margin:0 0 14px;">Redefinicao de senha | Password reset</h2>

                
                <p style="margin:0 0 14px;line-height:1.6;">
                  Recebemos uma solicitacao para redefinir sua senha do <strong>Quiz English</strong>.
                </p>

               
                <p style="margin:0 0 18px;line-height:1.6;">
                  We received a request to reset your <strong>Quiz English</strong> password.
                </p>

                <p style="margin:22px 0;">
                  <a href="{reset_link}" style="background:#2563eb;color:#fff;text-decoration:none;padding:12px 18px;border-radius:8px;display:inline-block;">
                    Redefinir senha / Reset password
                  </a>
                </p>

                <p style="margin:0 0 8px;line-height:1.6;">Link:</p>
                <p style="word-break:break-all;margin:0 0 16px;color:#2563eb;">{reset_link}</p>

                <p style="margin:0 0 6px;line-height:1.6;">
                  <strong>PT-BR:</strong> Este link expira em 1 hora.
                </p>
                <p style="margin:0 0 14px;line-height:1.6;">
                  <strong>EN:</strong> This link expires in 1 hour.
                </p>

                <p style="margin:0;line-height:1.6;color:#6b7280;">
                  PT-BR: Se voce nao fez esta solicitacao, ignore este email.<br/>
                  EN: If you did not request this, you can ignore this email.
                </p>
              </td>
            </tr>
          </table>
          <p style="font-size:12px;color:#9ca3af;margin-top:12px;">© Quiz English</p>
        </td>
      </tr>
    </table>
  </body>
</html>
"""

    msg = EmailMessage()
    msg["From"] = from_email
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.set_content(text_body)
    msg.add_alternative(html_body, subtype="html")

    with smtplib.SMTP(host, port, timeout=30) as s:
        s.ehlo()
        if use_tls:
            s.starttls()
            s.ehlo()
        s.login(username, password)
        s.send_message(msg)