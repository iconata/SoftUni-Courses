def center_point(x1, y1, x2, y2):
    first_pair_pos = [int(x1), int(y1)]
    second_pair_pos = [int(x2), int(y2)]
    first_pair_pos_cp = [abs(float(x1)), abs(float(y1))]
    second_pair_pos_cp = [abs(float(x2)), abs(float(y2))]

    if sum(first_pair_pos_cp) <= sum(second_pair_pos_cp):
        print(tuple(first_pair_pos))
    elif sum(first_pair_pos_cp) > sum(second_pair_pos_cp):
        print(tuple(second_pair_pos))


center_point(x1=float(input()), y1=float(input()), x2=float(input()), y2=float(input()))
