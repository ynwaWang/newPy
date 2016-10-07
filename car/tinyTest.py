import datetime
from data_base.utils.typeutils import time_conv

if __name__ == '__main__':
    stte1 = ['a\nb\nc\n','a1\n1b\nc2\n']
    saf = ''.join(stte1)


    now = datetime.datetime.now()
    now = time_conv.timestr_to_datetime('2016-02-01 01:00:00')
    checkpoint = time_conv.datetime_to_timestamp(now)
    week = 6 * 24 * 3600 * 1000
    last_checkpoint = checkpoint + week

    print time_conv.timestamp_to_date_str(last_checkpoint)
    print time_conv.timestamp_to_datetime_str(last_checkpoint, '%A').lower()
    print int(time_conv.timestamp_to_datetime_str(checkpoint, '%d'))
    print time_conv.timestamp_to_date_str(checkpoint - 24*3600*1000*1, pattern='%Y%m')