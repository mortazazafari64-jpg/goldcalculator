[app]

# نام برنامه
title = Gold Calculator

# نام package
package.name = goldcalculator
package.domain = org.goldcalculator

# محل فایل main.py
source.dir = .

# فایل‌هایی که همراه APK قرار می‌گیرند
source.include_exts = py,kv,png,jpg,jpeg,atlas,ttf,otf

# نسخه برنامه
version = 1.0

# کتابخانه‌های موردنیاز
requirements = python3,kivy,kivymd

# حالت نمایش
orientation = portrait

# معماری Android
android.archs = arm64-v8a

# نسخه NDK (تغییر داده شد)
android.ndk = 25b

# نسخه SDK
android.api = 33
android.minapi = 21

# مجوز اینترنت
android.permissions = INTERNET

# قبول خودکار licenseهای SDK
android.accept_sdk_license = True

# تنظیمات اضافی برای جلوگیری از خطای apt
android.gradle_repository = maven { url 'https://maven.google.com' }
android.bootstrap = sdl2

[buildozer]

log_level = 2
warn_on_root = 1
