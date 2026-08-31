[app]

# نام برنامه (بهتر است انگلیسی باشد)
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

# معماری Android (برای گوشی‌های ۶۴ بیتی جدید)
android.archs = arm64-v8a

# نسخه NDK (تغییر داده شد)
android.ndk = 25b

# نسخه SDK (اضافه شد)
android.api = 33

# مجوز اینترنت
android.permissions = INTERNET

# قبول خودکار licenseهای SDK
android.accept_sdk_license = True


[buildozer]

log_level = 2
warn_on_root = 1