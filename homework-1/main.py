"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2


def main():
    conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='123131')
    cur = conn.cursor()
    customers_data = 'north_data/customers_data.csv'
    employees_data = 'north_data/employees_data.csv'
    orders_data = 'north_data/orders_data.csv'

    try:
        sql = "COPY %s FROM STDIN WITH CSV HEADER DELIMITER AS ','"
        e = open(employees_data, 'r', encoding='utf8')
        cur.execute("truncate " + 'employees' + ";")
        cur.copy_expert(sql=sql % 'employees', file=e)

        # with open(employees_data, newline='') as file:
        #     cur.copy_from(file, 'employees', sep=',')

        with open(customers_data, newline='') as file:
            cur.copy_from(file, 'customers', sep=',')

        with open(orders_data, newline='') as file:
            cur.copy_from(file, 'orders', sep=',')

    finally:
        conn.commit()
        cur.close()
        conn.close()


if __name__ == '__main__':
    main()
