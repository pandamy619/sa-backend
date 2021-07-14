def abc_analysis(new_file):
    sorted_new_file = {}
    sorted_keys = sorted(new_file, key=new_file.get, reverse=True)
    for i in sorted_keys:
        sorted_new_file[i] = new_file[i]

    sales_amount = sum([float(sale[0]) for sale in sorted_new_file.values()])

    accrued_share = 0
    for key in sorted_new_file:
        sorted_new_file[key].append(round(sorted_new_file[key][0] / sales_amount * 100, 2))
        sorted_new_file[key].append(round(accrued_share + sorted_new_file[key][1], 2))
        accrued_share = sorted_new_file[key][2]
        if accrued_share <= 80.0:
            sorted_new_file[key].append('A')
        elif accrued_share > 80.0 and accrued_share <= 95.0:
            sorted_new_file[key].append('B')
        elif accrued_share > 95.0:
            sorted_new_file[key].append('C')

    return sorted_new_file