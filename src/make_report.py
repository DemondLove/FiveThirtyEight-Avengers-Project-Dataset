if __name__ == '__main__':
    import sys
    sys.path.append('/Users/Love/Documents/GitHub/msds510/src/msds510')
    import utils
    import datetime
    F = open(
        '/Users/Love/Documents/GitHub/msds510/data/processed/avengers_processed.csv',
        'r')
    lines = F.readlines()

    rows = []
    for line in lines:
        row = line.split(',')
        if len(row) == 22:
            rows.append(row)
    for k in rows:
        k[21].rstrip()
    today = datetime.date.today()

    c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for x in rows:
        if x[2] == '4333':
            c[0] = x
        elif x[2] == '3458':
            c[1] = x
        elif x[2] == '3130':
            c[2] = x
        elif x[2] == '3068':
            c[3] = x
        elif x[2] == '2402':
            c[4] = x
        elif x[2] == '2305':
            c[5] = x
        elif x[2] == '2125':
            c[6] = x
        elif x[2] == '2089':
            c[7] = x
        elif x[2] == '1886':
            c[8] = x
        elif x[2] == '1761':
            c[9] = x
        else:
            pass

    f = open(
        '/Users/Love/Documents/GitHub/msds510/reporting/top_ten_appearances.md',
        'w')
    t = 0
    while t < 10:
        f.write('# ' + str(t + 1)+'. ' + str(c[t][1]) + '\n')
        f.write('* Number of Appearance: ' + str(c[t][2]) + '\n')
        f.write('* Year Joined: ' + str(c[t][7]) + '\n')
        f.write('* Years Since Joining: ' + str(
            utils.years_since_joined((c[t][7]))) + '\n')
        f.write('* URL: ' + str(c[t][0]) + '\n')
        f.write('\n')
        f.write('## Notes' + '\n')
        f.write(''+str(c[t][20]) + '\n')
        t += 1
    f.close()
