# Homework 2:

# df = pd.read_csv('task\\stackoverflow_qa.csv')
# df.head()
# id	creationdate	score	viewcount	title	answercount	commentcount	favoritecount	quest_name	quest_rep	ans_name	ans_rep
# 332289	2008-12-01 21:24:44	3184	5962784	How do I change the size of figures drawn with...	14	1	0.0	tatwright	37837.0	NaN	NaN
# 2051744	2010-01-12 19:31:47	420	587728	How to invert the x or y axis	10	3	0.0	DarkAnt	4211.0	Demitri	13369.0
# 2225995	2010-02-09 00:51:38	51	59922	How can I create stacked line graph?	4	0	0.0	David Underhill	15936.0	doug	69290.0
# 5486226	2011-03-30 12:26:50	7	6393	Rolling median in python	5	4	0.0	yueerhu	175.0	Mike Pennington	42288.0
# 5515021	2011-04-01 14:50:44	10	13744	Compute a compounded return series in Python	3	6	0.0	Jason Strimpel	14916.0	Mike Pennington	42288.0
# Find all questions that were created before 2014
# Find all questions with a score more than 50
# Find all questions with a score between 50 and 100
# Find all questions answered by Scott Boston
# Find all questions answered by the following 5 users
# Find all questions that were created between March, 2014 and October 2014 that were answered by Unutbu and have score less than 5.
# Find all questions that have score between 5 and 10 or have a view count of greater than 10,000
# Find all questions that are not answered by Scott Boston
# Homework 3:

# Titanic data set, stored as CSV. The data consists of the following data columns:

# PassengerId: Id of every passenger.
# Survived: Indication whether passenger survived. 0 for yes and 1 for no.
# Pclass: One out of the 3 ticket classes: Class 1, Class 2 and Class 3.
# Name: Name of passenger.
# Sex: Gender of passenger.
# Age: Age of passenger in years.
# SibSp: Number of siblings or spouses aboard.
# Parch: Number of parents or children aboard.
# Ticket: Ticket number of passenger.
# Fare: Indicating the fare.
# Cabin: Cabin number of passenger.
# Embarked: Port of embarkation.
# titanic_df = pd.read_csv("task\\titanic.csv")
# titanic_df.head()
# PassengerId	Survived	Pclass	Name	Sex	Age	SibSp	Parch	Ticket	Fare	Cabin	Embarked
# 1	0	3	Braund, Mr. Owen Harris	male	22.0	1	0	A/5 21171	7.2500	NaN	S
# 2	1	1	Cumings, Mrs. John Bradley (Florence Briggs Th.)	female	38.0	1	0	PC 17599	71.2833	C85	C
# 3	1	3	Heikkinen, Miss. Laina	female	26.0	0	0	STON/O2. 3101282	7.9250	NaN	S
# 4	1	1	Futrelle, Mrs. Jacques Heath (Lily May Peel)	female	35.0	1	0	113803	53.1000	C123	S
# 5	0	3	Allen, Mr. William Henry	male	35.0	0	0	373450	8.0500	NaN	S
# Select Female Passengers in Class 1 with Ages between 20 and 30: Extract a DataFrame containing female passengers in Class 1 with ages between 20 and 30.

# Filter Passengers Who Paid More than $100: Create a DataFrame with passengers who paid a fare greater than $100.

# Select Passengers Who Survived and Were Alone: Filter passengers who survived and were traveling alone (no siblings, spouses, parents, or children).

# Filter Passengers Embarked from 'C' and Paid More Than $50: Create a DataFrame with passengers who embarked from 'C' and paid more than $50.

# Select Passengers with Siblings or Spouses and Parents or Children: Extract passengers who had both siblings or spouses aboard and parents or children aboard.

# Filter Passengers Aged 15 or Younger Who Didn't Survive: Create a DataFrame with passengers aged 15 or younger who did not survive.

# Select Passengers with Cabins and Fare Greater Than $200: Extract passengers with known cabin numbers and a fare greater than $200.

# Filter Passengers with Odd-Numbered Passenger IDs: Create a DataFrame with passengers whose PassengerId is an odd number.

# Select Passengers with Unique Ticket Numbers: Extract a DataFrame with passengers having unique ticket numbers.

# Filter Passengers with 'Miss' in Their Name and Were in Class 1: Create a DataFrame with female passengers having 'Miss' in their name and were in Class 1.




import pandas as pd

# Load dataset
df = pd.read_csv("task\\stackoverflow_qa.csv")

# Convert creationdate to datetime for date filters
df["creationdate"] = pd.to_datetime(df["creationdate"])

# 1️⃣ Questions created before 2014
before_2014 = df[df["creationdate"] < "2014-01-01"]

# 2️⃣ Questions with score more than 50
score_over_50 = df[df["score"] > 50]

# 3️⃣ Questions with score between 50 and 100
score_between_50_100 = df[(df["score"] >= 50) & (df["score"] <= 100)]

# 4️⃣ Questions answered by Scott Boston
answered_by_scott = df[df["ans_name"] == "Scott Boston"]

# 5️⃣ Questions answered by any of the following 5 users
users = ["Scott Boston", "unutbu", "unutbu", "Demitri", "Mike Pennington"]
answered_by_users = df[df["ans_name"].isin(users)]

# 6️⃣ Questions created between March 2014 and October 2014,
#     answered by Unutbu and have score < 5
filtered_unutbu = df[
    (df["creationdate"].between("2014-03-01", "2014-10-31"))
    & (df["ans_name"] == "unutbu")
    & (df["score"] < 5)
]

# 7️⃣ Questions with score between 5 and 10 OR viewcount > 10 000
score_or_views = df[((df["score"] >= 5) & (df["score"] <= 10)) | (df["viewcount"] > 10000)]

# 8️⃣ Questions NOT answered by Scott Boston
not_by_scott = df[df["ans_name"] != "Scott Boston"]

# ✅ Print summary
print("Questions before 2014:", before_2014.shape[0])
print("Score > 50:", score_over_50.shape[0])
print("Score 50–100:", score_between_50_100.shape[0])
print("Answered by Scott Boston:", answered_by_scott.shape[0])
print("Answered by selected users:", answered_by_users.shape[0])
print("Unutbu, 2014-03 to 2014-10, score<5:", filtered_unutbu.shape[0])
print("Score 5–10 or viewcount > 10000:", score_or_views.shape[0])
print("Not answered by Scott Boston:", not_by_scott.shape[0])


import pandas as pd

# Load Titanic dataset
titanic_df = pd.read_csv("task\\titanic.csv")

# 1️⃣ Female passengers in Class 1, age 20–30
female_class1_20_30 = titanic_df[
    (titanic_df["Sex"] == "female")
    & (titanic_df["Pclass"] == 1)
    & (titanic_df["Age"].between(20, 30))
]

# 2️⃣ Passengers who paid > $100
paid_over_100 = titanic_df[titanic_df["Fare"] > 100]

# 3️⃣ Passengers who survived and were alone
survived_alone = titanic_df[
    (titanic_df["Survived"] == 1)
    & (titanic_df["SibSp"] == 0)
    & (titanic_df["Parch"] == 0)
]

# 4️⃣ Embarked from 'C' and paid > $50
embarked_c_over_50 = titanic_df[
    (titanic_df["Embarked"] == "C") & (titanic_df["Fare"] > 50)
]

# 5️⃣ Had both siblings/spouses and parents/children aboard
siblings_and_parents = titanic_df[
    (titanic_df["SibSp"] > 0) & (titanic_df["Parch"] > 0)
]

# 6️⃣ Age ≤ 15 who did NOT survive
age15_not_survived = titanic_df[
    (titanic_df["Age"] <= 15) & (titanic_df["Survived"] == 0)
]

# 7️⃣ Known cabin and fare > $200
cabin_fare_over200 = titanic_df[
    titanic_df["Cabin"].notna() & (titanic_df["Fare"] > 200)
]

# 8️⃣ Odd-numbered Passenger IDs
odd_passenger_ids = titanic_df[titanic_df["PassengerId"] % 2 != 0]

# 9️⃣ Passengers with unique ticket numbers
unique_tickets = titanic_df[
    ~titanic_df["Ticket"].duplicated(keep=False)
]

# 🔟 Female passengers with 'Miss' in name and in Class 1
miss_class1 = titanic_df[
    (titanic_df["Name"].str.contains("Miss", case=False, na=False))
    & (titanic_df["Sex"] == "female")
    & (titanic_df["Pclass"] == 1)
]

# ✅ Print summary
print("Female Class 1 20–30:", female_class1_20_30.shape[0])
print("Fare > 100:", paid_over_100.shape[0])
print("Survived and alone:", survived_alone.shape[0])
print("Embarked C and > 50:", embarked_c_over_50.shape[0])
print("Siblings and Parents:", siblings_and_parents.shape[0])
print("Age≤15 not survived:", age15_not_survived.shape[0])
print("Cabin & Fare > 200:", cabin_fare_over200.shape[0])
print("Odd Passenger IDs:", odd_passenger_ids.shape[0])
print("Unique tickets:", unique_tickets.shape[0])
print("Miss in Class 1:", miss_class1.shape[0])
