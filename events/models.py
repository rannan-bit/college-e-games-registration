from django.db import models


class Registration(models.Model):

    EVENT_CHOICES = [
        ('Mini Militia', 'Mini Militia'),
        ('eFootball', 'eFootball'),
        ('PUBG', 'PUBG Mobile'),
    ]

    PAYMENT_METHODS = [
        ('UPI', 'UPI Transaction'),
        ('Screenshot', 'Upload Screenshot'),
        ('Cash', 'Cash Payment'),
    ]

    participant_name = models.CharField(max_length=100)

    semester_department = models.CharField(max_length=100)

    contact_number = models.CharField(max_length=15)

    email = models.EmailField()

    event_name = models.CharField(
        max_length=50,
        choices=EVENT_CHOICES
    )

    team_name = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    player2 = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    player3 = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    player4 = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    payment_method = models.CharField(
        max_length=50,
        choices=PAYMENT_METHODS
    )

    transaction_id = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    payment_screenshot = models.ImageField(
        upload_to='payments/',
        blank=True,
        null=True
    )

    payment_status = models.BooleanField(default=False)

    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.participant_name