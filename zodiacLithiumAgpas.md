# Chinese Zodiac Program

## Coding Exercise

This exercise creates a Python program that determines a person's Chinese
zodiac sign based only on their year of birth.

## Requirements

1. Ask the user to enter a year of birth.
2. Use 1900 as the baseline year.
3. Validate that the year is not earlier than 1900.
4. Display an appropriate error message for an invalid year.
5. Determine the Chinese zodiac sign using a 12-year cycle.
6. Consider only the year of birth.
7. Test and run the program before submission.

## Source Code

```python
# zodiacSectionLN.py
# Chinese Zodiac Program
# Baseline year: 1900

year_of_birth = int(input("Enter your year of birth: "))

if year_of_birth < 1900:
    print("Invalid year. The year of birth must not be earlier than 1900.")
else:
    zodiac_number = (year_of_birth - 1900) % 12

    if zodiac_number == 0:
        zodiac = "Rat (鼠 / Shǔ)"
    elif zodiac_number == 1:
        zodiac = "Ox (牛 / Niú)"
    elif zodiac_number == 2:
        zodiac = "Tiger (虎 / Hǔ)"
    elif zodiac_number == 3:
        zodiac = "Rabbit (兔 / Tù)"
    elif zodiac_number == 4:
        zodiac = "Dragon (龙 / Lóng)"
    elif zodiac_number == 5:
        zodiac = "Snake (蛇 / Shé)"
    elif zodiac_number == 6:
        zodiac = "Horse (马 / Mǎ)"
    elif zodiac_number == 7:
        zodiac = "Goat (羊 / Yáng)"
    elif zodiac_number == 8:
        zodiac = "Monkey (猴 / Hóu)"
    elif zodiac_number == 9:
        zodiac = "Rooster (鸡 / Jī)"
    elif zodiac_number == 10:
        zodiac = "Dog (狗 / Gǒu)"
    else:
        zodiac = "Pig (猪 / Zhū)"

    print(f"Year of birth: {year_of_birth}")
    print(f"Chinese Zodiac: {zodiac}")


