# imports psycopg2 (a PostgeSQL database adaptor for python)
import psycopg2
import psycopg2.extras as extras

# define run_sql function, note 'values' is optional parameter and defaults to None
def run_sql(sql, values = None):
    conn = None
    #run_sql always returns the 'results' varaible which is a list
    results = []

    try:
        #creates a new connection to 'travel_tracker' database
        conn = psycopg2.connect("dbname = 'travel_tracker")
        #creates a cursor
        cur = conn.cursor(cursor_factory=extras.DictCursor)
        #execute SQL command/query with the cursor
        cur.execute(sql, values)
        #commit to database
        conn.commit()
        #fetch rows of query (in list format) and save to results variable
        results = cur.fetchall()
        #close cursor
        cur.close()

    #print any errors
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    #close db connection
    finally:
        if conn is not None:
            conn.close()

    return results