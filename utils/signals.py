from django.dispatch import Signal

post_data = Signal(providing_args=["request", "user"])




