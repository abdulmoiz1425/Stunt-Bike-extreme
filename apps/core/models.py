from django.db import models


class SiteSettings(models.Model):
    site_name = models.CharField(max_length=100, default='Stunt Bike Extreme')
    tagline = models.CharField(max_length=200, default='The Ultimate Motorcycle Stunt Racing Game')
    logo = models.ImageField(upload_to='site/', blank=True, null=True)
    favicon = models.ImageField(upload_to='site/', blank=True, null=True)
    contact_email = models.EmailField(default='admin@stuntbikextreme.com')
    pinterest_url = models.URLField(blank=True)
    medium_url = models.URLField(blank=True)
    google_analytics_id = models.CharField(max_length=50, blank=True)
    footer_text = models.TextField(
        default='Stunt Bike Extreme is a fan-dedicated APK download site. '
                'We are not officially affiliated with the original game developer.',
        blank=True,
    )
    cookie_notice = models.TextField(
        default='We use cookies to improve your experience. By continuing, you accept our Privacy Policy.',
        blank=True,
    )

    class Meta:
        verbose_name = 'Site Settings'
        verbose_name_plural = 'Site Settings'

    def __str__(self):
        return self.site_name

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def get_settings(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class FAQ(models.Model):
    question = models.CharField(max_length=400)
    answer = models.TextField()
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'

    def __str__(self):
        return self.question
