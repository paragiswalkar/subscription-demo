import sqlite3
from datetime import datetime, timedelta
import argparse

# Function to create a new subscription
def create_subscription(user_id):
    conn = sqlite3.connect('subscriptions.db')
    c = conn.cursor()
    
    start_date = datetime.now().date()
    end_date = start_date + timedelta(days=180)  # 6 months from start_date
    
    c.execute('INSERT INTO subscriptions (user_id, start_date, end_date, active) VALUES (?, ?, ?, ?)',
              (user_id, start_date, end_date, True))
    
    conn.commit()
    conn.close()
    print(f"Subscription created for user {user_id} from {start_date} to {end_date}")

# Function to renew a subscription
def renew_subscription(subscription_id):
    conn = sqlite3.connect('subscriptions.db')
    c = conn.cursor()
    
    c.execute('SELECT * FROM subscriptions WHERE id = ?', (subscription_id,))
    subscription = c.fetchone()
    
    if subscription:
        current_end_date = datetime.strptime(subscription[3], '%Y-%m-%d').date()
        new_end_date = current_end_date + timedelta(days=180)  # Renew for another 6 months
        
        c.execute('UPDATE subscriptions SET end_date = ? WHERE id = ?', (new_end_date, subscription_id))
        conn.commit()
        conn.close()
        print(f"Subscription {subscription_id} renewed until {new_end_date}")
    else:
        print(f"Subscription with ID {subscription_id} not found")

# Function to display all subscriptions
def display_subscriptions():
    conn = sqlite3.connect('subscriptions.db')
    c = conn.cursor()
    
    c.execute('SELECT * FROM subscriptions')
    subscriptions = c.fetchall()
    
    print("Current Subscriptions:")
    for sub in subscriptions:
        print(f"ID: {sub[0]}, User ID: {sub[1]}, Start Date: {sub[2]}, End Date: {sub[3]}, Active: {sub[4]}")
    
    conn.close()
    
# Function to handle CLI commands
def main():
    parser = argparse.ArgumentParser(description="Subscription Management System")
    parser.add_argument('--add', metavar='user_id', type=int, help='Add a new subscription for the given user ID')
    parser.add_argument('--renew', metavar='subscription_id', type=int, help='Renew the subscription with the given ID')
    parser.add_argument('--list', action='store_true', help='List all current subscriptions')
    
    args = parser.parse_args()
    
    if args.add:
        create_subscription(args.add)
    elif args.renew:
        renew_subscription(args.renew)
    elif args.list:
        display_subscriptions()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()