import locale


medicare = .0145
fica = .062
fed_tax_brackets = {
    9325: .1,
    37950: .15,
    91900: .25,
    191650: .28,
    416700: .33,
    418400: .35,
    418401: .396,
    }
idaho_tax_brackets = {
    1452: .016,
    2940: .036,
    4356: .041,
    5808: .051,
    7260: .061,
    10890: .071,
    10890: .071,
    }


def tax(agi, deductions, exemptions, schedule):
    ti = agi - deductions - exemptions
    tax_due = 0
    last_bracket = 0
    loops = 1
    for bracket in schedule:
        # Loop ends here if we are in top bracket
        if loops == len(schedule):
            marginal = (ti - last_bracket) * schedule[bracket]
            tax_due += marginal
        # Main loop begins
        elif ti - bracket >= 0:
            marginal = (bracket - last_bracket) * schedule[bracket]
            tax_due += marginal
            loops += 1
        # Loop ends (unless we are in top bracket)
        else:
            marginal = (ti - last_bracket) * schedule[bracket]
            tax_due += marginal
            break  # Necessary to stop early if not in top bracket
                   # Otherwise, loop continues until error due to string
        last_bracket = bracket
    return tax_due


def usd(money):
    return locale.currency(money, grouping=True)


def percent(numerator, denominator):
    return round(100 * numerator / denominator, 2)


def salary(hours, hourly_rate):
    return hours * hourly_rate


def bonus(salary, bonus):
    return salary * bonus


def match(salary, match):
    return salary * match


def pension(salary, pension):
    return salary * pension


def gross_income(salary, match, bonus):
    return salary + match + bonus


def adjusted_gross_income(gross_income, deductions, exemptions):
    return gross_income - deductions - exemptions


def taxable(gross_income, pretax_investment, deduction, exemption):
    return gross_income - pretax_investment - deduction - exemption


def fica_taxes(gross_income, ssi, medicare):
    return gross_income * (ssi + medicare)


def pretax_investment(salary, pension, pretax_save):
    return salary * pension + pretax_save


def retirement_portion(pretax_investment, posttax_save):
    return pretax_investment + posttax_save


def government_portion(fica_taxes, fed_taxes, state_taxes):
    return fica_taxes + fed_taxes + state_taxes


def discretionary_spend(gross_income, retirement_portion, government_portion):
    return gross_income - retirement_portion - government_portion


def net_income(gross_income, fica_taxes, fed_taxes, state_taxes):
    return gross_income - fica_taxes - fed_taxes - state_taxes


class Person:
    def __init__(
            self,
            name,
            hourly_rate,
            hours,
            match_percentage,
            bonus_percentage,
            pension,
            posttax_save,
            pretax_save,
            exemption,
            deduction,
        ):
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours = hours
        self.match_percentage = match_percentage
        self.bonus_percentage = bonus_percentage
        self.pension = pension
        self.posttax_save = posttax_save
        self.pretax_save = pretax_save
        self.exemption = exemption
        self.deduction = deduction

        self.my_salary = salary(self.hours, self.hourly_rate)
        self.my_match = match(self.my_salary, self.match_percentage)
        self.my_bonus = bonus(self.my_salary, self.bonus_percentage)
        self.my_gross_income = self.my_salary + self.my_match + self.my_bonus
        self.my_adjusted_gross_income = adjusted_gross_income(self.my_gross_income, self.deduction, self.exemption)
        self.my_pretax_deduction = pretax_investment(self.my_salary, self.pension, self.pretax_save)
        self.my_taxable_income = taxable(self.my_gross_income, self.my_pretax_deduction, self.deduction, self.exemption)
        self.my_fed_taxes = tax(self.my_taxable_income, self.deduction, self.exemption, fed_tax_brackets)
        self.my_state_taxes = tax(self.my_taxable_income, self.deduction, self.exemption, idaho_tax_brackets)
        self.my_fica_taxes = fica_taxes(self.my_gross_income, fica, medicare)
        self.my_net_income = net_income(self.my_gross_income, self.my_fica_taxes, self.my_fed_taxes, self.my_state_taxes)
        self.my_retirement_spend = retirement_portion(self.my_pretax_deduction, self.posttax_save)
        self.my_government_spend = government_portion(self.my_fica_taxes, self.my_fed_taxes, self.my_state_taxes)
        self.my_discretionary_spend = discretionary_spend(self.my_gross_income, self.my_retirement_spend, self.my_government_spend)
        self.my_eff_fed = str(percent(self.my_fed_taxes, self.my_gross_income)) + ' %'
        self.my_eff_state = str(percent(self.my_state_taxes, self.my_gross_income)) + ' %'
        self.my_eff_fica = str(percent(self.my_fica_taxes, self.my_gross_income)) + ' %'
        self.my_ptaxed = str(percent(self.my_government_spend, self.my_gross_income)) + ' %'
        self.my_psaved = str(percent(self.my_retirement_spend, self.my_gross_income)) + ' %'
        self.my_pspent = str(percent(self.my_discretionary_spend, self.my_gross_income)) + ' %'
        self.my_fire_saved = str(percent(self.my_retirement_spend, self.my_net_income)) + ' %'
        self.my_fire_spent = str(percent(self.my_discretionary_spend, self.my_net_income)) + ' %'

    def printer(self):
        '''Prints personal finance metrics.'''
        rows = [
            ['Salary',                             str(usd(self.my_salary)).rjust(20)               ],
            ['+ Match',                            str(usd(self.my_match)).rjust(20)                ],
            ['+ Bonus',                            str(usd(self.my_bonus)).rjust(20)                ],
            ['----------------------------------', '--------------------'                           ],
            ['Gross income',                       str(usd(self.my_gross_income)).rjust(20)         ],
            ['- Deduction',                        str(usd(self.deduction)).rjust(20)               ],
            ['- Exemption',                        str(usd(self.exemption)).rjust(20)               ],
            ['----------------------------------', '--------------------'                           ],
            ['Adjusted gross income',              str(usd(self.my_adjusted_gross_income)).rjust(20)],
            ['- Pretax investment',                str(usd(self.my_pretax_deduction)).rjust(20)     ],
            ['----------------------------------', '--------------------'                           ],
            ['Taxable income',                     str(usd(self.my_taxable_income)).rjust(20)       ],
            ['',                                   ''                                               ],
            ['Gross income',                       str(usd(self.my_gross_income)).rjust(20)         ],
            ['- Pretax investment',                str(usd(self.my_pretax_deduction)).rjust(20)     ],
            ['- FICA tax',                         str(usd(self.my_fica_taxes)).rjust(20)           ],
            ['- Federal income tax',               str(usd(self.my_fed_taxes)).rjust(20)            ],
            ['- State income tax',                 str(usd(self.my_state_taxes)).rjust(20)          ],
            ['- Posttax investment',               str(usd(self.posttax_save)).rjust(20)            ],
            ['----------------------------------', '--------------------'                           ],
            ['Discretionary income',               str(usd(self.my_discretionary_spend)).rjust(20)  ],
            ['',                                   ''                                               ],
            ['Effective FICA tax rate',            str(self.my_eff_fica).rjust(20)                  ],
            ['Effective federal income tax rate',  str(self.my_eff_fed).rjust(20)                   ],
            ['Effective state tax rate',           str(self.my_eff_state).rjust(20)                 ],
            ['',                                   ''                                               ],
            ['Gross income',                       str(usd(self.my_gross_income)).rjust(20)         ],
            ['----------------------------------', '--------------------'                           ],
            ['Spend',                              str(usd(self.my_discretionary_spend)).rjust(20)  ],
            ['Save',                               str(usd(self.my_retirement_spend)).rjust(20)     ],
            ['Tax',                                str(usd(self.my_government_spend)).rjust(20)     ],
            ['Spend',                              str(self.my_pspent).rjust(20)                    ],
            ['Save',                               str(self.my_psaved).rjust(20)                    ],
            ['Tax',                                str(self.my_ptaxed).rjust(20)                    ],
            ['',                                   ''                                               ],
            ['After tax income',                   str(usd(self.my_net_income)).rjust(20)           ],
            ['----------------------------------', '--------------------'                           ],
            ['Spend',                              str(usd(self.my_discretionary_spend)).rjust(20)  ],
            ['Save',                               str(usd(self.my_retirement_spend)).rjust(20)     ],
            ['Percent net income saved',           str(self.my_fire_saved).rjust(20)                ],
            ['Percent net income spent',           str(self.my_fire_spent).rjust(20)                ],
            ]

        widths = [max(map(len, col)) for col in zip(*rows)]
        for row in rows:
            print("".join((val.ljust(width) for val, width in zip(row, widths))))

        return None
