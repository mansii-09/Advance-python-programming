from insta_utils.likes import like_count
from insta_utils.comments import comment_count

likes = like_count(100,20)
comments = comment_count(30, 5)

print("Total Likes:", likes)
print("Total Comments:", comments)