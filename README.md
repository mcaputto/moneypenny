# moneypenny [![Build Status](https://travis-ci.org/mcaputto/moneypenny.svg?branch=master)](https://travis-ci.org/mcaputto/moneypenny)

## Usage

To compute personal finance parameters, first initialize the
`moneypenny.Person()` class with the required parameters, and then use the
`Person.printer()` method to view a tabular arrangement.

## Example

```md
$ python3 test_moneypenny.py
Salary                                     $124,800.00
+ Match                                      $6,240.00
+ Bonus                                      $3,744.00
------------------------------------------------------
Gross income                               $134,784.00
- Deduction                                  $6,300.00
- Exemption                                  $4,050.00
------------------------------------------------------
Adjusted gross income                      $124,434.00
- Pretax investment                         $27,984.00
------------------------------------------------------
Taxable income                              $96,450.00

Gross income                               $134,784.00
- Pretax investment                         $27,984.00
- FICA tax                                  $10,310.98
- Federal income tax                        $17,263.75
- State income tax                           $5,895.12
- Posttax investment                         $5,500.00
------------------------------------------------------
Discretionary income                        $67,830.15

Effective FICA tax rate                         7.65 %
Effective federal income tax rate              12.81 %
Effective state tax rate                        4.37 %

Gross income                               $134,784.00
------------------------------------------------------
Spend                                       $67,830.15
Save                                        $33,484.00
Tax                                         $33,469.85
Spend                                          50.33 %
Save                                           24.84 %
Tax                                            24.83 %

After tax income                           $101,314.15
------------------------------------------------------
Spend                                       $67,830.15
Save                                        $33,484.00
Percent net income saved                       33.05 %
Percent net income spent                       66.95 %
```
