from connection import connection
from utils import *

cursor = connection.cursor()


def add_customer(data):
    acc_no = generate_account_no()
    data.append(acc_no)
    query = """
    insert into Customer(`First Name`, `Last Name`, `Address`, `Balance`, `Account No`)
    values(%s, %s, %s, %s, %s)
    """
    cursor.execute(query, data)


def retrieve_data(acc_no):
    query = """
    select * from `Customer` where `Account No`=%s
    """
    cursor.execute(query, acc_no)
    data = cursor.fetchone()
    if data :
        column_names = [column[0] for column in cursor.description] 
        data = dict(zip(column_names, data))
    return data


def update_data(data):
    query = """
    update `Customer` set `First Name`=%s, `Last Name`=%s, `Address`=%s where `Account No`=%s
    """
    cursor.execute(query, data)


def remove(acc_no):
    query = """
    delete from `Customer` where `Account No`=%s
    """
    cursor.execute(query, acc_no)


def add_money(acc_no, amount):
    trans_id = generate_transaction_id() 
    # data.append(trans_id)

    get_amount_query = """
    select Balance from Customer where `Account No` =%s
    """
    cursor.execute(get_amount_query, acc_no)
    available_amount = cursor.fetchone()

    updated_balance = available_amount[0] + amount

    update_balance_query = """
    update Customer set `Balance` = %s where `Account No` =%s
    """
    cursor.execute(update_balance_query, (updated_balance, acc_no))

    insert_query = """
    insert into `Transaction`(`Account No`, `Amount_Added`, `Transaction_id` )
    values(%s, %s, %s)
    """
    cursor.execute(insert_query, (acc_no, amount, trans_id))


def retrieve_money(acc_no, amount):
    trans_id = generate_transaction_id() 
    # data.append(trans_id)
    
    get_amount_query = """
    select Balance from Customer where `Account No` =%s
    """
    cursor.execute(get_amount_query, acc_no)
    available_amount = cursor.fetchone()

    updated_balance = available_amount[0] - amount

    update_balance_query = """
    update Customer set `Balance` = %s where `Account No` =%s
    """
    cursor.execute(update_balance_query, (updated_balance, acc_no))

    insert_query = """
    insert into `Transaction`(`Account No`, `Amount_Retrieved`, `Transaction_id` )
    values(%s, %s, %s)
    """
    cursor.execute(insert_query, (acc_no, amount, trans_id))