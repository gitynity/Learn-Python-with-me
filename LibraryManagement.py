import random
import re
import sys
import datetime
import pymysql

def connect_to_database():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        database="library"
    )

def main():
    print("Welcome to the library management system")
    print("1. Add a book")
    print("2. Add a member")
    print("3. Issue a book")
    print("4. Return a book")
    print("5. Search a book")
    print("6. Search a member")
    print("7. Delete a book")
    print("8. Delete a member")
    print("9. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_book()
    elif choice == 2:
        add_member()
    elif choice == 3:
        issue_book()
    elif choice == 4:
        return_book()
    elif choice == 5:
        search_book()
    elif choice == 6:
        search_member()
    elif choice == 7:
        delete_book()
    elif choice == 8:
        delete_member()
    elif choice == 9:
        sys.exit()
    else:
        print("Invalid choice")
        main()
    
def add_book():
    print("Add a book")
    book_name = input("Enter book name: ")
    author_name = input("Enter author name: ")
    book_id = random.randint(100000, 999999)
    book_id = str(book_id)
    book_id = book_id + book_name[0:3]
    book_id = book_id.upper()
    book_id = re.sub(r'\s+', '', book_id)
    book_id = book_id[0:6]
    book_id = book_id + "B"
    print("Book ID: ", book_id)
    try:
        connection = connect_to_database()
        cursor = connection.cursor()
        sql = "INSERT INTO books (book_id, book_name, author_name) VALUES (%s, %s, %s)"
        val = (book_id, book_name, author_name)
        cursor.execute(sql, val)
        connection.commit()
        print("Book added successfully")
    except Exception as e:
        print(e)
        print("Book not added")
    finally:
        if connection:
            connection.close()
        main()
    
def add_member():
    print("Add a member")
    member_name = input("Enter member name: ")
    member_id = random.randint(100000, 999999)
    member_id = str(member_id)
    member_id = member_id + member_name[0:3]
    member_id = member_id.upper()
    member_id = re.sub(r'\s+', '', member_id)
    member_id = member_id[0:6]
    member_id = member_id + "M"
    print("Member ID: ", member_id)
    try:
        connection = connect_to_database()
        cursor = connection.cursor()
        sql = "INSERT INTO members (member_id, member_name) VALUES (%s, %s)"
        val = (member_id, member_name)
        cursor.execute(sql, val)
        connection.commit()
        print("Member added successfully")
    except Exception as e:
        print(e)
        print("Member not added")
    finally:
        if connection:
            connection.close()
        main()
        
def issue_book():
    print("Issue a book")
    book_id = input("Enter book ID: ")
    member_id = input("Enter member ID: ")
    issue_date = datetime.datetime.now()
    return_date = issue_date + datetime.timedelta(days=15)
    try:
        connection = connect_to_database()
        cursor = connection.cursor()
        sql = "INSERT INTO issued_books (book_id, member_id, issue_date, return_date) VALUES (%s, %s, %s, %s)"
        val = (book_id, member_id, issue_date, return_date)
        cursor.execute(sql, val)
        connection.commit()
        print("Book issued successfully")
    except Exception as e:
        print(e)
        print("Book not issued")
    finally:
        if connection:
            connection.close()
        main()
    
def return_book():
    print("Return a book")
    book_id = input("Enter book ID: ")
    member_id = input("Enter member ID: ")
    return_date = datetime.datetime.now()
    try:
        connection = connect_to_database()
        cursor = connection.cursor()
        sql = "DELETE FROM issued_books WHERE book_id = %s AND member_id = %s"
        val = (book_id, member_id)
        cursor.execute(sql, val)
        connection.commit()
        print("Book returned successfully")
    except Exception as e:
        print(e)
        print("Book not returned")
    finally:
        if connection:
            connection.close()
        main()
    
def search_book():
    print("Search a book")
    book_id = input("Enter book ID: ")
    try:
        connection = connect_to_database()
        cursor = connection.cursor()
        sql = "SELECT * FROM books WHERE book_id = %s"
        val = (book_id,)
        cursor.execute(sql, val)
        myresult = cursor.fetchall()
        for x in myresult:
            print(x)
        main()
    except Exception as e:
        print(e)
        print("Book not found")
        main()


def search_member():
    print("Search a member")
    member_id = input("Enter member ID: ")
    try:
        connection = connect_to_database()
        cursor = connection.cursor()
        sql = "SELECT * FROM members WHERE member_id = %s"
        val = (member_id,)
        cursor.execute(sql, val)
        myresult = cursor.fetchall()
        for x in myresult:
            print(x)
        main()
    except Exception as e:
        print(e)
        print("Member not found")
        main()
    
def delete_book():
    print("Delete a book")
    book_id = input("Enter book ID: ")
    try:
        connection = connect_to_database()
        cursor = connection.cursor()
        sql = "DELETE FROM books WHERE book_id = %s"
        val = (book_id,)
        cursor.execute(sql, val)
        connection.commit()
        print("Book deleted successfully")
        main()
    except Exception as e:
        print(e)
        print("Book not found")
        main()
    
def delete_member():
    print("Delete a member")
    member_id = input("Enter member ID: ")
    try:
        connection = connect_to_database()
        cursor = connection.cursor()
        sql = "DELETE FROM members WHERE member_id = %s"
        val = (member_id,)
        cursor.execute(sql, val)
        connection.commit()
        print("Member deleted successfully")
        main()
    except Exception as e:
        print(e)
        print("Member not found")
        main()
    
if __name__ == "__main__":
    main()
