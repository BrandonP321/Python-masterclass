import shelve

# with shelve.open('typing-leaderboard') as score:
#     score['brandonp321'] = 30
#     score['b-phillips3278'] = 90
#     score['bphil076'] = 60
#     place = 0
#     scores_list = []
#     for board in sorted(score):
#         scores_list.append(score[board])
#         place += 1
#         print(f"{place:2}. {score[board]} WPM: {board}")
#     sorted_scores = list(reversed(sorted(scores_list)))
#     print(sorted_scores)

with shelve.open('typing-leaderboard') as score:
    score['Brandon'] = 70
    place = 0
    for board in sorted(score.items(), key=lambda x: x[1], reverse=True):
        place += 1
        print(f"{place}. {board[0]} Overall: {board[1]}")