from django.db import models
from django.utils import timezone


class Platform(models.Model):
    PLATFORM_CHOICES = [
        ('android', 'Android APK'),
        ('mod', 'MOD APK'),
        ('pc', 'PC'),
        ('ios', 'iOS'),
        ('smart_tv', 'Smart TV'),
        ('tv_box', 'TV Box'),
    ]

    PLATFORM_ICONS = {
        'android': '🤖',
        'mod': '⚡',
        'pc': '💻',
        'ios': '🍎',
        'smart_tv': '📺',
        'tv_box': '📦',
    }

    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    platform_type = models.CharField(max_length=20, choices=PLATFORM_CHOICES, unique=True)
    tagline = models.CharField(max_length=200, blank=True)
    description = models.TextField()
    installation_guide = models.TextField(
        help_text='Enter each step on a new line, e.g. "Step 1: ..."'
    )
    features = models.TextField(help_text='One feature per line')
    meta_title = models.CharField(max_length=200)
    meta_description = models.CharField(max_length=300)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

    def get_latest_version(self):
        return self.apkversion_set.filter(is_latest=True).first()

    def get_features_list(self):
        return [f.strip() for f in self.features.split('\n') if f.strip()]

    def get_installation_steps(self):
        return [s.strip() for s in self.installation_guide.split('\n') if s.strip()]

    def get_icon(self):
        return self.PLATFORM_ICONS.get(self.platform_type, '📱')

    def get_url_name(self):
        url_map = {
            'android': 'home',
            'mod': 'mod_apk',
            'pc': 'for_pc',
            'ios': 'for_ios',
            'smart_tv': 'for_smart_tv',
            'tv_box': 'for_tv_box',
        }
        return url_map.get(self.platform_type, 'home')


class APKVersion(models.Model):
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    version = models.CharField(max_length=50)
    apk_file = models.FileField(
        upload_to='apk/',
        blank=True,
        null=True,
        help_text='Upload the APK file directly (optional)',
    )
    external_url = models.URLField(
        blank=True,
        help_text='External download link (used if no file is uploaded)',
    )
    file_size = models.CharField(max_length=20, help_text='e.g., 85 MB')
    android_requirement = models.CharField(max_length=50, default='Android 5.0+')
    release_date = models.DateField(default=timezone.now)
    download_count = models.PositiveIntegerField(default=0)
    is_latest = models.BooleanField(default=False)
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=4.5)
    changelog = models.TextField(blank=True)

    class Meta:
        ordering = ['-release_date']

    def __str__(self):
        return f'{self.platform.name} v{self.version}'

    def get_download_url(self):
        if self.apk_file:
            return self.apk_file.url
        if self.external_url and self.external_url != '#':
            return self.external_url
        return None

    def save(self, *args, **kwargs):
        if self.is_latest:
            APKVersion.objects.filter(
                platform=self.platform, is_latest=True
            ).exclude(pk=self.pk).update(is_latest=False)
        super().save(*args, **kwargs)


class Screenshot(models.Model):
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE, related_name='screenshots')
    image = models.ImageField(upload_to='screenshots/')
    caption = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'Screenshot for {self.platform.name} #{self.order}'
