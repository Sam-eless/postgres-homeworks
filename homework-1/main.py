"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import psycopg2


def main():
    conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='123131')
    customers_data = 'north_data/customers_data.csv'
    employees_data = 'north_data/employees_data.csv'
    orders_data = 'north_data/orders_data.csv'

    try:
        with conn.cursor() as cur:
            with open(employees_data, newline="") as file:
                reader = csv.reader(file)
                emp_id = 1
                for row in reader:
                    if '_' not in row[0]:
                        cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)",
                                    (emp_id, row[0], row[1], row[2], row[3], row[4]))
                        emp_id += 1

            with open(customers_data, newline="") as file:
                reader = csv.reader(file)
                for row in reader:
                    if '_' not in row[0]:
                        cur.execute("INSERT INTO customers VALUES (%s, %s, %s)",
                                    (row[0], row[1], row[2]))

            with open(orders_data, newline="") as file:
                reader = csv.reader(file)
                for row in reader:
                    if '_' not in row[0]:
                        cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)",
                                    (row[0], row[1], row[2], row[3], row[4]))

    finally:
        conn.commit()
        conn.close()

    # try:
    #     sql = "COPY %s FROM STDIN WITH CSV HEADER DELIMITER AS ','"
    #     e = open(employees_data, 'r', encoding='utf8')
    #     cur.execute("truncate " + 'employees' + ";")
    #     cur.copy_expert(sql=sql % 'employees', file=e)
    #
    #     # with open(employees_data, newline='') as file:
    #     #     cur.copy_from(file, 'employees', sep=',')
    #
    #     with open(customers_data, newline='') as file:
    #         cur.copy_from(file, 'customers', sep=',')
    #
    #     with open(orders_data, newline='') as file:
    #         cur.copy_from(file, 'orders', sep=',')
    #
    # finally:
    #     conn.commit()
    #     cur.close()
    #     conn.close()


if __name__ == '__main__':
    main()
