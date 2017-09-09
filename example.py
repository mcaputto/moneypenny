import locale
import moneypenny


def main():
    locale.setlocale(locale.LC_ALL, '')
    locale.localeconv()

    test = moneypenny.Person(
        name='foo',
        hourly_rate=60.00,
        hours=2080.0,
        match_percentage=.05,
        bonus_percentage=.03,
        pension=.08,
        posttax_save=5500.00,
        pretax_save=18000.00,
        exemption=4050.00,
        deduction=6300.00,
        )

    test.printer()


if __name__ == '__main__':
    main()
