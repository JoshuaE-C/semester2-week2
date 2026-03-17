"""
This is where you should write your code and this is what you need to upload to Gradescope for autograding.

You must NOT change the function definitions (names, arguments).

You can run the functions you define in this file by using test.py (python test.py)
Please do not add any additional code underneath these functions.
"""

import sqlite3

def customer_tickets(conn, customer_id):
    """
    Return a list of tuples:
    (film_title, screen, price)

    Include only tickets purchased by the given customer_id.
    Order results by film title alphabetically.
    """
    query = f"SELECT title, screen, price FROM films INNER JOIN screenings ON films.film_id=screenings.film_id INNER JOIN tickets ON screenings.screening_id=tickets.screening_id INNER JOIN customers ON customers.customer_id=tickets.customer_id WHERE customers.customer_id={customer_id} ORDER BY title ASC;"
    cur = conn.cursor()
    return cur.execute(query).fetchall()


def screening_sales(conn):
    """
    Return a list of tuples:
    (screening_id, film_title, tickets_sold)

    Include all screenings, even if tickets_sold is 0.
    Order results by tickets_sold descending.
    """

    query = """
    SELECT screenings.screening_id, title, COUNT(ticket_id) AS tickets_sold 
    FROM screenings 
    INNER JOIN films 
    ON screenings.film_id=films.film_id 
    LEFT JOIN tickets 
    ON screenings.screening_id=tickets.screening_id 
    GROUP BY screenings.screening_id 
    ORDER BY tickets_sold DESC;"""

    cur = conn.cursor()
    return cur.execute(query).fetchall()


def top_customers_by_spend(conn, limit):
    """
    Return a list of tuples:
    (customer_name, total_spent)

    total_spent is the sum of ticket prices per customer.
    Only include customers who have bought at least one ticket.
    Order by total_spent descending.
    Limit the number of rows returned to `limit`.
    """

    query = f"""
    SELECT customer_name, SUM(price) total_spent
    FROM tickets
    INNER JOIN customers 
    ON customers.customer_id=tickets.customer_id 
    GROUP BY customers.customer_id
    ORDER BY total_spent DESC 
    LIMIT {limit}
    ;"""

    cur = conn.cursor()
    return cur.execute(query).fetchall()
    