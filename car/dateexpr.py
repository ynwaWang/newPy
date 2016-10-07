import re
from datetime import datetime
from dateutil.relativedelta import relativedelta


def expr(input_str):
    time_format = re.search(r'\$\{(.+)([\+\-])(\d*)(\w?)\}', input_str)
    if time_format:
        interval = int(time_format.group(3)) if time_format.group(3) else 0
        input_str = __options[time_format.group(2) + time_format.group(4)](interval).strftime(
            time_format.group(1))
    # ex_result =  re.sub(r'\s+', ' ', input_str).strip()
    return input_str


def __addDay(days=0):
    return datetime.now() + relativedelta(days=days)


def __subDay(days=0):
    return datetime.now() - relativedelta(days=days)


def __addMonth(months=1):
    return datetime.now() + relativedelta(months=months)


def __subMonth(months=1):
    return datetime.now() - relativedelta(months=months)


def __addHour(hours=1):
    return datetime.now() + relativedelta(hours=hours)


def __subHour(hours=1):
    return datetime.now() - relativedelta(hours=hours)


def __addYear(years=1):
    return datetime.now() + relativedelta(years=years)


def __subYear(years=1):
    return datetime.now() - relativedelta(years=years)


__options = {
    '+': __addDay,
    '-': __subDay,
    '+d': __addDay,
    '-d': __subDay,
    '+m': __addMonth,
    '-m': __subMonth,
    '+h': __addHour,
    '-h': __subHour,
    '+y': __addYear,
    '-y': __subYear
}

__pattern = re.compile(r'(\$\{.+?\})')


def parse(input_sql):
    match = __pattern.split(input_sql)
    if match:
        result = '"' + ''.join([expr(v) for v in match])+ '"'
        return result
    return input_sql


# "select * from   table    where    start_date    >=     ${%Y%m01-1m} and end_date < ${%Y%m01+} "
