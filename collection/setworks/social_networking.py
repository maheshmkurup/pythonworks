users=["rahul","rohit","kohli","rishab","sanju","pandya","siraj"]

rahul_followers=["rohith","kohli","rishab","rahul"]

rahul_follow_suggestion=set(users).difference(set(rahul_followers))

print(rahul_follow_suggestion)


sanju_followers={"sanju","rohith","kohli"}

mutual_friends=set(rahul_followers).intersection(set(sanju_followers))

print(mutual_friends)

