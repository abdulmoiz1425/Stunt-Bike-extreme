from django.core.management.base import BaseCommand
from django.utils import timezone

from apps.core.models import SiteSettings, FAQ
from apps.apk.models import Platform, APKVersion


PLATFORMS = [
    {
        'name': 'Stunt Bike Extreme APK',
        'slug': 'stunt-bike-extreme-apk',
        'platform_type': 'android',
        'tagline': 'Download Free for Android',
        'description': (
            'Stunt Bike Extreme is one of the most thrilling motorcycle stunt racing games '
            'available for Android. Packed with physics-based gameplay, dozens of challenging '
            'levels, and multiple high-performance bikes, this game delivers an unmatched '
            'two-wheel experience right on your phone. Whether you are a casual rider or a '
            'hardcore racer, Stunt Bike Extreme will keep you hooked for hours. '
            'The game is completely free to download and play, with regular updates bringing '
            'new content, bikes, and levels to keep things fresh.'
        ),
        'installation_guide': (
            'Step 1: Go to Settings > Security on your Android device.\n'
            'Step 2: Enable "Unknown Sources" to allow APK installation.\n'
            'Step 3: Tap the Download APK button on this page.\n'
            'Step 4: Once the download completes, open the APK file from your notifications or Downloads folder.\n'
            'Step 5: Tap "Install" and wait for the installation to finish.\n'
            'Step 6: Launch Stunt Bike Extreme from your home screen and enjoy!'
        ),
        'features': (
            'Real Physics-Based Gameplay\n'
            '50+ Challenging Levels\n'
            'Multiple High-Performance Bikes\n'
            'HD Graphics & Smooth Animations\n'
            'Intuitive Touch Controls\n'
            'Offline Mode — No Internet Required\n'
            'Free to Download & Play\n'
            'Regular Updates with New Content\n'
            'Career & Free Ride Modes\n'
            'Global Leaderboards'
        ),
        'meta_title': 'Stunt Bike Extreme APK Download Latest Version Free for Android',
        'meta_description': (
            'Download Stunt Bike Extreme APK latest version free for Android. '
            'Physics-based motorcycle stunt game with 50+ levels, HD graphics, and offline mode.'
        ),
        'order': 1,
    },
    {
        'name': 'Stunt Bike Extreme MOD APK',
        'slug': 'stunt-bike-extreme-mod-apk',
        'platform_type': 'mod',
        'tagline': 'Unlimited Coins & All Bikes Unlocked',
        'description': (
            'The Stunt Bike Extreme MOD APK is a modified version of the original game that '
            'unlocks all premium features for free. With unlimited coins, all bikes available '
            'from the start, zero ads, and max level unlocked, you can enjoy the full game '
            'experience without any restrictions. This MOD version is ideal for players who '
            'want to explore every feature of the game without grinding for resources.'
        ),
        'installation_guide': (
            'Step 1: Uninstall the original Stunt Bike Extreme if already installed.\n'
            'Step 2: Go to Settings > Security > Enable "Unknown Sources".\n'
            'Step 3: Download the MOD APK from the button above.\n'
            'Step 4: Open the downloaded file from your Downloads folder.\n'
            'Step 5: Tap "Install" and wait for completion.\n'
            'Step 6: Open the game — all MOD features are automatically active!'
        ),
        'features': (
            'Unlimited Coins & Currency\n'
            'All Bikes Unlocked from Start\n'
            'No Ads — Ad-Free Experience\n'
            'All Levels Unlocked\n'
            'God Mode Available\n'
            'Premium Bikes Available for Free\n'
            'Unlimited Fuel\n'
            'All Skins & Customizations Unlocked'
        ),
        'meta_title': 'Stunt Bike Extreme MOD APK — Unlimited Coins & All Bikes Unlocked',
        'meta_description': (
            'Download Stunt Bike Extreme MOD APK with unlimited coins, all bikes unlocked, '
            'no ads, and all premium features for free on Android.'
        ),
        'order': 2,
    },
    {
        'name': 'Stunt Bike Extreme for PC',
        'slug': 'stunt-bike-extreme-for-pc',
        'platform_type': 'pc',
        'tagline': 'Play on Windows & Mac via Emulator',
        'description': (
            'Want to experience Stunt Bike Extreme on a big screen? You can play it on your '
            'Windows or Mac PC using an Android emulator like BlueStacks or NoxPlayer. '
            'Playing on PC gives you the advantage of a larger display, keyboard controls, '
            'and smoother performance depending on your hardware.'
        ),
        'installation_guide': (
            'Step 1: Download and install BlueStacks (bluestacks.com) on your Windows or Mac.\n'
            'Step 2: Sign in with your Google account inside BlueStacks.\n'
            'Step 3: Download the Stunt Bike Extreme APK from this website.\n'
            'Step 4: Double-click the APK file — BlueStacks will install it automatically.\n'
            'Step 5: Find the game in BlueStacks app library and click to launch.\n'
            'Step 6: Configure keyboard controls from BlueStacks settings for the best experience.'
        ),
        'features': (
            'Large Screen Gameplay\n'
            'Keyboard & Mouse Controls\n'
            'Better Performance on High-End PCs\n'
            'Compatible with Windows 7/8/10/11\n'
            'Compatible with macOS 10.12+\n'
            'Free via BlueStacks or NoxPlayer\n'
            'Full HD Rendering'
        ),
        'meta_title': 'Stunt Bike Extreme for PC — Download & Play on Windows/Mac',
        'meta_description': (
            'Learn how to download and play Stunt Bike Extreme on PC using BlueStacks emulator. '
            'Step-by-step guide for Windows and Mac.'
        ),
        'order': 3,
    },
    {
        'name': 'Stunt Bike Extreme for iOS',
        'slug': 'stunt-bike-extreme-for-ios',
        'platform_type': 'ios',
        'tagline': 'Install on iPhone & iPad',
        'description': (
            'Stunt Bike Extreme can be installed on your iPhone or iPad using AltStore, '
            'a trusted third-party app installer for iOS. Follow the steps below to get '
            'the game running on your Apple device without jailbreaking.'
        ),
        'installation_guide': (
            'Step 1: Install AltStore on your iPhone/iPad via altstore.io.\n'
            'Step 2: Download the IPA version of Stunt Bike Extreme from the link above.\n'
            'Step 3: Open AltStore on your device and tap the "+" button.\n'
            'Step 4: Select the downloaded IPA file.\n'
            'Step 5: AltStore will install the app — enter your Apple ID when prompted.\n'
            'Step 6: Go to Settings > General > VPN & Device Management and trust the developer.\n'
            'Step 7: Launch Stunt Bike Extreme from your home screen!'
        ),
        'features': (
            'Compatible with iPhone 6s and newer\n'
            'Compatible with iPad (5th gen+)\n'
            'Requires iOS 12.0 or later\n'
            'No Jailbreak Required\n'
            'Full Touch Screen Controls\n'
            'Optimized for Apple Hardware'
        ),
        'meta_title': 'Stunt Bike Extreme for iOS — Install on iPhone & iPad',
        'meta_description': (
            'Download and install Stunt Bike Extreme on iPhone and iPad. '
            'Step-by-step guide using AltStore — no jailbreak required.'
        ),
        'order': 4,
    },
    {
        'name': 'Stunt Bike Extreme for Smart TV',
        'slug': 'stunt-bike-extreme-for-smart-tv',
        'platform_type': 'smart_tv',
        'tagline': 'Play on Your Smart TV Screen',
        'description': (
            'Enjoy Stunt Bike Extreme on the big screen of your Android Smart TV. '
            'Most Android-based Smart TVs (Samsung, LG Android TV, Sony Bravia, Xiaomi TV, etc.) '
            'support APK sideloading, allowing you to install and play the game directly on your TV.'
        ),
        'installation_guide': (
            'Step 1: On your Smart TV, go to Settings > Security > Enable Unknown Sources.\n'
            'Step 2: Install a file manager app (e.g., ES File Explorer) from the TV app store.\n'
            'Step 3: Download the APK from this website on your phone or computer.\n'
            'Step 4: Transfer the APK to a USB drive and plug it into your Smart TV.\n'
            'Step 5: Open ES File Explorer on TV, navigate to the USB drive, and select the APK.\n'
            'Step 6: Tap "Install" and launch the game. Use a gamepad for best experience.'
        ),
        'features': (
            'Play on a Large TV Screen\n'
            'Android TV Compatible\n'
            'Gamepad / Remote Support\n'
            'HD Visuals on Big Display\n'
            'Compatible with Samsung, Sony, Xiaomi TVs\n'
            'Simple Sideload Installation'
        ),
        'meta_title': 'Stunt Bike Extreme for Smart TV — APK Installation Guide',
        'meta_description': (
            'Learn how to install and play Stunt Bike Extreme on your Android Smart TV. '
            'Step-by-step APK sideloading guide.'
        ),
        'order': 5,
    },
    {
        'name': 'Stunt Bike Extreme for TV Box',
        'slug': 'stunt-bike-extreme-for-tv-box',
        'platform_type': 'tv_box',
        'tagline': 'Install on Android TV Box',
        'description': (
            'Android TV Boxes are powerful media devices that run full Android OS, '
            'making them perfect for installing and playing Stunt Bike Extreme. '
            'Popular TV boxes like Xiaomi Mi Box, NVIDIA Shield, and Amazon Fire TV Stick '
            'all support APK installation. Follow the guide below to set it up.'
        ),
        'installation_guide': (
            'Step 1: On your TV Box, enable Developer Options and USB Debugging in Settings.\n'
            'Step 2: Enable "Unknown Sources" in Settings > Security.\n'
            'Step 3: Install the Downloader app from the TV Box app store.\n'
            'Step 4: Open Downloader and enter the direct APK URL from this page.\n'
            'Step 5: Let Downloader fetch and install the APK.\n'
            'Step 6: Launch Stunt Bike Extreme from the home screen. Connect a gamepad for best play.'
        ),
        'features': (
            'Full Android APK Support\n'
            'Works on Mi Box, NVIDIA Shield, Amazon Fire TV\n'
            'Gamepad Controller Support\n'
            'High Performance Gameplay\n'
            'Easy Downloader App Installation\n'
            'Stream and Play on Any TV'
        ),
        'meta_title': 'Stunt Bike Extreme for TV Box — Android TV Box APK Guide',
        'meta_description': (
            'Install Stunt Bike Extreme on your Android TV Box. Complete APK guide for '
            'Mi Box, NVIDIA Shield, Amazon Fire TV Stick, and more.'
        ),
        'order': 6,
    },
]

FAQS = [
    ('Is Stunt Bike Extreme free to download?',
     'Yes, Stunt Bike Extreme is completely free to download from our website. No registration or payment is required.',
     1),
    ('Is the APK file safe to install?',
     'Absolutely. All APK files hosted on our website are scanned for malware and viruses before being made available. We only provide clean, safe files.',
     2),
    ('What Android version does Stunt Bike Extreme require?',
     'Stunt Bike Extreme requires Android 5.0 (Lollipop) or higher. It is compatible with most Android smartphones and tablets.',
     3),
    ('Can I play Stunt Bike Extreme offline?',
     'Yes! Stunt Bike Extreme fully supports offline gameplay. You can play without an internet connection once the game is installed.',
     4),
    ('What is the difference between the regular APK and MOD APK?',
     'The regular APK is the original version of the game. The MOD APK is a modified version that includes unlimited coins, all bikes unlocked, and no ads — without any cost.',
     5),
    ('How do I update Stunt Bike Extreme to the latest version?',
     'Simply download the latest APK from our website and install it over your existing version. Your game progress will be saved.',
     6),
    ('Can I play Stunt Bike Extreme on PC?',
     'Yes! You can play Stunt Bike Extreme on Windows or Mac by using an Android emulator like BlueStacks. Visit our "For PC" page for the full guide.',
     7),
    ('Will installing an APK from this site void my warranty?',
     'Installing third-party APKs does not typically void your device warranty. However, we recommend reading your device manufacturer\'s policy for full clarity.',
     8),
]


class Command(BaseCommand):
    help = 'Populate the database with initial platform data, versions, and FAQs'

    def handle(self, *args, **options):
        self.stdout.write('Creating platforms...')
        for data in PLATFORMS:
            platform, created = Platform.objects.get_or_create(
                platform_type=data['platform_type'],
                defaults={k: v for k, v in data.items() if k != 'platform_type'},
            )
            if created:
                self.stdout.write(f'  Created: {platform.name}')
                APKVersion.objects.create(
                    platform=platform,
                    version='1.2.3',
                    file_size='85 MB',
                    android_requirement='Android 5.0+',
                    external_url='#',
                    is_latest=True,
                    rating=4.5,
                    release_date=timezone.now().date(),
                    changelog='Initial release available on this site.',
                )
            else:
                self.stdout.write(f'  Already exists: {platform.name}')

        self.stdout.write('Creating FAQs...')
        for question, answer, order in FAQS:
            FAQ.objects.get_or_create(
                question=question,
                defaults={'answer': answer, 'order': order},
            )

        self.stdout.write('Creating site settings...')
        SiteSettings.get_settings()

        self.stdout.write(self.style.SUCCESS('Initial data populated successfully!'))
        self.stdout.write('Next steps:')
        self.stdout.write('  1. python manage.py createsuperuser')
        self.stdout.write('  2. python manage.py runserver')
        self.stdout.write('  3. Go to /admin/ to manage content and update APK download links')
