import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class GoldProfitCalculator(toga.App):
    def startup(self):
        self.main_window = toga.MainWindow(title=self.name)

        # ورودی‌ها
        self.price_daily_input = toga.TextInput(
            placeholder='قیمت روز طلا (هر گرم)',
            style=Pack(flex=1, padding=(0, 5))
        )
        self.seller_price_input = toga.TextInput(
            placeholder='قیمت فروشنده (کل طلا)',
            style=Pack(flex=1, padding=(0, 5))
        )
        self.weight_input = toga.TextInput(
            placeholder='وزن طلا (گرم)',
            style=Pack(flex=1, padding=(0, 5))
        )

        # دکمه‌ها
        calc_button = toga.Button(
            '🧮 محاسبه سود',
            on_press=self.calculate,
            style=Pack(padding=5)
        )
        clear_button = toga.Button(
            '🔄 پاک کردن',
            on_press=self.clear_all,
            style=Pack(padding=5)
        )

        # برچسب‌های نتیجه
        self.result_title = toga.Label(
            '📊 نتیجه محاسبات',
            style=Pack(font_size=16, font_weight='bold', padding=(10, 5))
        )
        self.result_percent = toga.Label(
            '',
            style=Pack(font_size=28, font_weight='bold', padding=(0, 5))
        )
        self.result_analysis = toga.Label(
            '',
            style=Pack(padding=(0, 5))
        )
        self.result_details = toga.Label(
            '',
            style=Pack(padding=(0, 5))
        )

        # چیدمان اصلی
        box = toga.Box(style=Pack(direction=COLUMN, padding=10))

        box.add(toga.Label(
            '💎 محاسبه‌گر سود طلا',
            style=Pack(font_size=20, font_weight='bold', padding=(5, 5))
        ))
        box.add(toga.Label(
            'محاسبه درصد سود فروشنده طلا',
            style=Pack(padding=(0, 10))
        ))

        box.add(toga.Label('💰 قیمت روز طلا (هر گرم)', style=Pack(padding=(5, 0))))
        box.add(self.price_daily_input)
        box.add(toga.Label('🏪 قیمت فروشنده (کل طلا)', style=Pack(padding=(5, 0))))
        box.add(self.seller_price_input)
        box.add(toga.Label('⚖️ وزن طلا (گرم)', style=Pack(padding=(5, 0))))
        box.add(self.weight_input)

        button_box = toga.Box(style=Pack(direction=ROW, padding=5))
        button_box.add(calc_button)
        button_box.add(clear_button)
        box.add(button_box)

        box.add(toga.Divider(style=Pack(padding=(10, 0))))
        box.add(self.result_title)
        box.add(self.result_percent)
        box.add(self.result_analysis)
        box.add(self.result_details)

        self.main_window.content = box
        self.main_window.show()
        self.show_empty_result()

    # ── توابع کمکی ──
    def fa_to_en(self, text):
        persian_digits = '۰۱۲۳۴۵۶۷۸۹'
        english_digits = '0123456789'
        trans = str.maketrans(persian_digits, english_digits)
        return text.translate(trans)

    def get_clean_value(self, input_widget, field_name):
        raw = input_widget.value.strip()
        raw = raw.replace(',', '').replace('،', '')
        raw = self.fa_to_en(raw)
        if raw == '':
            raise ValueError(f"لطفاً {field_name} را وارد کنید")
        return float(raw)

    # ── منطق محاسبه ──
    def calculate(self, widget):
        try:
            daily_price = self.get_clean_value(self.price_daily_input, "قیمت روز طلا")
            seller_price = self.get_clean_value(self.seller_price_input, "قیمت فروشنده")
            weight = self.get_clean_value(self.weight_input, "وزن طلا")

            if daily_price <= 0 or seller_price <= 0 or weight <= 0:
                self.main_window.error_dialog('خطا', '❌ همه مقادیر باید بزرگتر از صفر باشند!')
                return

            actual_value = daily_price * weight
            profit_amount = seller_price - actual_value
            profit_percentage = (profit_amount / actual_value) * 100

            self.show_result(actual_value, seller_price, profit_amount, profit_percentage)

        except ValueError as e:
            self.main_window.error_dialog('خطا', f'❌ {str(e)}')

    def show_result(self, actual_value, seller_price, profit_amount, profit_percentage):
        color = self.get_profit_color(profit_percentage)

        self.result_title.text = '📊 درصد سود فروشنده'
        self.result_percent.text = f'{profit_percentage:+.1f}%'
        self.result_percent.style.color = color
        self.result_analysis.text = self.get_analysis(profit_percentage)
        self.result_analysis.style.color = color

        details = (
            f'💎 ارزش واقعی: {actual_value:,.0f} تومان\n'
            f'🏪 قیمت فروشنده: {seller_price:,.0f} تومان\n'
            f'📈 مقدار سود: {profit_amount:+,.0f} تومان'
        )
        self.result_details.text = details

    def show_empty_result(self):
        self.result_title.text = '📊 نتیجه محاسبات'
        self.result_percent.text = ''
        self.result_analysis.text = 'منتظر ورود اطلاعات...'
        self.result_details.text = ''

    def clear_all(self, widget):
        self.price_daily_input.value = ''
        self.seller_price_input.value = ''
        self.weight_input.value = ''
        self.show_empty_result()

    # ── رنگ‌بندی و تحلیل ──
    def get_profit_color(self, pct):
        if pct > 20: return '#e94560'
        if pct > 10: return '#ff6b00'
        if pct > 5:  return '#ffd700'
        if pct >= 0: return '#00c853'
        return '#00bcd4'

    def get_analysis(self, pct):
        if pct > 20: return "⚠️ سود خیلی زیاد! احتیاط کنید."
        if pct > 10: return "💡 سود نسبتاً بالاست."
        if pct > 5:  return "✅ سود منطقی"
        if pct > 0:  return "👍 سود منصفانه"
        if pct == 0: return "🎯 بدون سود (قیمت بازار)"
        return "🎉 زیر قیمت بازار!"


def main():
    return GoldProfitCalculator('GoldProfitCalculator', 'org.example.goldprofit')


if __name__ == '__main__':
    main().main_loop()
