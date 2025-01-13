def solution(score):
    x = []
    rank = []

    for i in score:
        y = (i[0] + i[1]) / 2
        x.append(y)

    sorted_averages = sorted(x, reverse=True)

    for avg in x:
        rank.append(sorted_averages.index(avg) + 1)

    final_rank = []
    prev_rank = 0
    prev_score = None

    for i, r in enumerate(rank):
        if prev_score is not None and prev_score == x[i]:
            final_rank.append(prev_rank)
        else:
            final_rank.append(r)
            prev_rank = r
        prev_score = x[i]

    return final_rank
