def send_email():
    pass


def call_back_email_after_save_product(sender, instance, created, **kwargs):
    "this signal is going to send an email if the product was saved"
    
    if created:
        send_email()

