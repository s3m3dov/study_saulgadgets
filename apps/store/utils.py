from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from apps.order.views import render_to_pdf

def decrement_product_quantity(order):
    # Decrement the number of available products by quantity for each product after ordered
    for item in order.items.all():
        product = item.product
        product.num_available -= item.quantity
        product.save()

def send_order_confirmation(order):
    # Send html page(order confirmation) as mail
    subject = 'Order confirmation'
    from_email = 'noreply@saulgadgets.com'
    to = ['mail@saulgadgets.com', order.email]
    text_content = 'Your order has been confirmed!'
    html_content = render_to_string('order_confirmation.html', {'order': order})
    pdf = render_to_pdf({'order': order})
    # Add data to message variable
    msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    msg.attach_alternative(html_content, "text/html")
    # Attach Invoice (pdf)
    if pdf:
        name = f'order_{order.id}.pdf'
        msg.attach(name, pdf, 'application/pdf')
    msg.send()