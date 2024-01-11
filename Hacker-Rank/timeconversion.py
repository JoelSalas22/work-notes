"""
string: the time in 24 hour format
Sample Input: '07:05:45PM'
returns 19:05:45
"""
  if 'AM' in s:
        # Replace AM with empty string
        s = s.replace('AM', '')
        hourtime = int(s[:2])
        if hourtime == 12:
            hourtime = '00'
        # Convert back to string
            s = str(hourtime) + s[2:]
        return s
    elif 'PM' in s:
        # Replace PM with empty string 
        s = s.replace('PM', '')
        # Convert hour to 24hour time by adding + 12
        hourtime = int(s[:2]) + 12
        if hourtime == 24:
            hourtime = '12'
        s = str(hourtime) + s[2:]
        return s
