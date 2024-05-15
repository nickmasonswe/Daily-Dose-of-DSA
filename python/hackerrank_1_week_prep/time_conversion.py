# Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock. # 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock. 
def timeConversion(s):
    if int(s[0:2]) == 12:
        return '00' + s[2:6]
    if s[8:] == 'AM':
        return s[0:8]
    else:
        return str(int(s[0:2]) + 12) + s[2:8]