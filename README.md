# moneypenny

![](https://upload.wikimedia.org/wikipedia/en/9/9b/Miss_Moneypenny_by_Lois_Maxwell.jpg)

## Usage

To compute personal finance parameters, first initialize the
`moneypenny.Person()` class with the required parameters, and then use the
`Person.printer()` method to view a tabular arrangement.

## Example

```md
$ python3 example.py
Salary                                       $124,800.00
+ Match:                                       $6,240.00
+ Bonus:                                       $3,744.00
= Gross income:                              $134,784.00

Fica taxes:                                   $10,310.98
- Deduction:                                   $6,300.00
- Exemption:                                   $4,050.00
= Adjusted gross income:                     $124,434.00

- Pretax investment:                          $27,984.00
= Taxable income:                             $96,450.00

- Fed taxes:                                  $17,263.75
- State taxes:                                 $5,895.12
Effective Federal Income Tax Rate:                 12.81
Effective FICA Tax Rate:                            7.65
Effective State Tax Rate:                           4.37

- Posttax investment:                          $5,500.00
= Discretionary spend:                        $67,830.15

Gross income:                                $134,784.00
Discretionary spend:                          $67,830.15
Retirement spend:                             $33,484.00
Government spend:                             $33,469.85
Percent gross income taxed:                        24.83
Percent gross income saved:                        24.84
Percent gross income spent:                        50.33

Net income:                                  $101,314.15
Discretionary spend:                          $67,830.15
Retirement spend:                             $33,484.00
Percent net income saved:                          33.05
Percent net income spent:                          66.95
```
