
from datetime import datetime, timedelta, timezone

class DateLocal:
    '''
    params:
        - UTC_INT: if localhost, UTC_INT = LOCAL_INT;
        - LOCAL_INT: uses when application would is web.
    '''

    UTC_INT = int(datetime.now().timestamp())
    UTC_STR = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    BR_INT = int(datetime.now(timezone(timedelta(hours = -3))).timestamp())
    BR_STR = datetime.now(timezone(timedelta(hours = -3))).strftime('%Y-%m-%d %H:%M:%S')
