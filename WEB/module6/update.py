from sqlite3 import Error

from connect import create_connection, database


def update_task(conn, parameters):
    """
    update project_id
    :param conn:
    :param parameters:
    :return:
    """
    sql = '''
    UPDATE tasks
    SET project_id = ?
    WHERE id = ?
    '''
    cur = conn.cursor()
    try:
        cur.execute(sql, parameters)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cur.close()


def update_task_status(conn, parameters):
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param parameters:
    :return:
    """
    sql = '''
    UPDATE tasks
    SET status = ? 
    WHERE id = ?
    '''

    cur = conn.cursor()
    try:
        cur.execute(sql, parameters)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cur.close()


if __name__ == '__main__':
    with create_connection(database) as conn:
        update_task(conn, (1, 1))
        update_task_status(conn, (True, 1))
        
