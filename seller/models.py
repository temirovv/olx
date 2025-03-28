from django.db import models


class SellerAccount(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    language = models.CharField(max_length=20)
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Seller - {self.name}"


class RegistrationTypes(models.TextChoices):
    YURIDIK_SHAXS = ('yurudik_shaxs', 'Yuridik Shaxs')
    YAKKA_TARTIBDAGI_TADBIRKOR= ('yakka_tartibdagi_tadbirkor', 'Yakka tartibdagi tadbirkor')
    OZINI_OZI_BAND_QILGAN = ('ozini_ozi_band_qilgan', "O'zini o'zi band qilgan")


class RegistrationForm(models.Model):
    registration_type = models.CharField(max_length=30, choices=RegistrationTypes.choices)
    name_of_legal_entity = models.CharField(max_length=255)
    sitr = models.CharField(max_length=255)
    ifut_code = models.CharField(max_length=255)
    seller_account = models.ForeignKey('SellerAccount', on_delete=models.CASCADE)

    def __str__(self):
        return f"Form of {self.seller_account.name}"

class Document(models.Model):
    file = models.FileField(upload_to='files/')
    registration_form = models.ForeignKey('RegistrationForm', on_delete=models.CASCADE)
