from connection import connection

cursor = connection.cursor()

create_customer = """
create table `Customer`(
    `Account No` varchar(12) PRIMARY KEY,
    `First Name` varchar(25) NOT NULL,
    `Last Name` varchar (10) NOT NULL,
    `Address` varchar(50) NOT NULL,
    `Balance` int DEFAULT NULL 
)
"""

# cursor.execute(create_customer)

create_transaction = """
create table `Transaction`(
    `Account No` varchar(12), 
    `Transaction_id` varchar(6) PRIMARY KEY,
    `Amount_Added` int DEFAULT NULL,
    `Amount_Retrieved` int DEFAULT NULL,
    FOREIGN KEY (`Account No`) REFERENCES Customer(`Account No`)
)
"""

# cursor.execute(create_transaction)

insert_customer = """
insert into customer(`Account No`, `First Name`, `Last Name`, `Address`, `Balance`)
values
("fr0gu765jik5", "Uzumaki", "Naruto", "Siliguri, WestBengal.", 100000)
"""

cursor.execute(insert_customer)