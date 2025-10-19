# Homework 1:

# Using chinook.db write pandas code.

# 1. Customer Purchases Analysis:
# Find the total amount spent by each customer on purchases (considering invoices).
# Identify the top 5 customers with the highest total purchase amounts.
# Display the customer ID, name, and the total amount spent for the top 5 customers.



import pandas as pd
import sqlite3

# Connect to chinook.db
conn = sqlite3.connect("chinook.db")

# Load data
customers = pd.read_sql_query("SELECT CustomerId, FirstName, LastName FROM customers", conn)
invoices = pd.read_sql_query("SELECT CustomerId, Total FROM invoices", conn)

# Merge and group
customer_spending = (
    invoices.groupby("CustomerId")["Total"]
    .sum()
    .reset_index()
    .merge(customers, on="CustomerId")
)

# Sort and select top 5
top5_customers = customer_spending.sort_values(by="Total", ascending=False).head(5)

# Display
print(top5_customers[["CustomerId", "FirstName", "LastName", "Total"]])



# 2. Album vs. Individual Track Purchases:
# Determine the percentage of customers who prefer to buy individual tracks instead of full albums.
# A customer is considered to prefer individual tracks if they have purchased only a subset of tracks from an album.
# Provide a summary of the percentage of customers who fall into each category (individual tracks vs. full albums).

# Load relevant tables
invoice_items = pd.read_sql_query("SELECT * FROM invoice_items", conn)
tracks = pd.read_sql_query("SELECT TrackId, AlbumId FROM tracks", conn)
albums = pd.read_sql_query("SELECT AlbumId, Title FROM albums", conn)
invoices = pd.read_sql_query("SELECT InvoiceId, CustomerId FROM invoices", conn)

# Merge invoice_items with invoices and tracks to know who bought what
purchases = (
    invoice_items.merge(invoices, on="InvoiceId")
    .merge(tracks, on="TrackId")
)

# Count how many tracks exist per album
album_track_counts = tracks.groupby("AlbumId")["TrackId"].nunique().reset_index()
album_track_counts.rename(columns={"TrackId": "TotalTracksInAlbum"}, inplace=True)

# Count how many tracks each customer bought from each album
customer_album_purchases = (
    purchases.groupby(["CustomerId", "AlbumId"])["TrackId"]
    .nunique()
    .reset_index()
    .merge(album_track_counts, on="AlbumId")
)

# Determine if customer bought full album
customer_album_purchases["FullAlbum"] = (
    customer_album_purchases["TrackId"] == customer_album_purchases["TotalTracksInAlbum"]
)

# Classify customers
customer_pref = (
    customer_album_purchases.groupby("CustomerId")["FullAlbum"]
    .any()
    .reset_index()
)

customer_pref["Preference"] = customer_pref["FullAlbum"].apply(
    lambda x: "Full Albums" if x else "Individual Tracks"
)

# Calculate percentages
summary = (
    customer_pref["Preference"]
    .value_counts(normalize=True) * 100
).reset_index()
summary.columns = ["Preference", "Percentage"]

print(summary)

