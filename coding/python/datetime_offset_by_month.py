# -*- coding: utf-8 -*-
import datetime


def datetime_offset_by_month(dt1, n=1):
    """
    对datetime对象按月份偏移（datetime.timedelta只能对时、分、秒、日、周进行偏移，就是不能进行月份偏移）
    （此转换的实现思路是找到要偏移到的那个月份的最后一天，然后再把真实的天数更新回去）
    :param dt1: 需要进行偏移的日期
    :param n: 要偏移的月数
    :return: 偏移后的日期
    """

    # create a shortcut object for one day
    one_day = datetime.timedelta(days=1)

    # first use div and mod to determine year cycle
    q, r = divmod(dt1.month + n, 12)

    # create a datetime2
    # to be the last day of the target month
    dt2 = datetime.datetime(
        dt1.year + q, r + 1, 1, dt1.hour, dt1.minute, dt1.second
    ) - one_day

    '''
       if input date is the last day of this month
       then the output date should also be the last
       day of the target month, although the day
       may be different.
       for example:
       datetime1 = 8.31
       datetime2 = 9.30
    '''

    if dt1.month != (dt1 + one_day).month:
        return dt2

    '''
        if datetime1 day is bigger than last day of
        target month, then, use datetime2
        for example:
        datetime1 = 01.30
        datetime2 = 02.29
    '''

    if dt1.day >= dt2.day:
        return dt2

    '''
     then, here, we just replace datetime2's day
     with the same of datetime1, that's ok.
    '''

    return dt2.replace(day=dt1.day)


if __name__ == '__main__':
    print(datetime_offset_by_month(datetime.datetime.strptime('2020.04.27 17:23', '%Y.%m.%d %H:%M'), n=1))
