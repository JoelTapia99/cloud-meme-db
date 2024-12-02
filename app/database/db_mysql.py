from decouple import config

import pymysql
import traceback

# Logger
from app.utils.Logger import Logger


def get_connection():
    try:
        return pymysql.connect(
            host=config('AWS_MYSQL_URL'),
            port=config('AWS_MYSQL_PORT'),
            user=config('AWS_MYSQL_USER'),
            password=config('AWS_MYSQL_PASSWORD'),
            db=config('AWS_MYSQL_DB_NAME')
        )
    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())
