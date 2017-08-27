def answer(src,dst):
    col_src = src % 8
    lin_src = src / 8
    col_dest = dst % 8
    lin_dest = dst / 8
    dif_col = abs(col_src - col_dest)
    dif_lin = abs(lin_src - lin_dest)
    if src == dst:
        return 0
    if dif_col != dif_lin and ((dif_col + dif_lin) % 2 == 0):
        if (dif_col and dif_lin != 0):
            if abs(dif_lin - dif_col) >= 4:
                return 4
            if dif_lin + dif_col <= 8:
                return 2
            else:
                return 4
        else:
            if dif_lin + dif_col <= 4:
                return 2
            elif dif_lin + dif_col <= 6:
                return 4
    elif dif_col == dif_lin:
        #avoid corners
        if src and dst not in [0, 7, 56, 63]:
            if (dif_lin + dif_col) == 2 or (dif_lin + dif_col)  == 6:
                return 2
            elif (dif_lin + dif_col) <= 10:
                return 4
        else:
            if (dif_lin + dif_col)  == 6:
                return 2
            elif (dif_lin + dif_col) == 14:
                return 6
            else:
                return 4
    else:
        if dif_col == 7 or dif_lin == 7:
            return 5
        if (dif_col + dif_lin) == 3:
            return 1
        else:
            return 3
## test
print answer(19,36)