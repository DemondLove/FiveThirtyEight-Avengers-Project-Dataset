class Avenger:
    def __init__(self, record):
        """
        Initializes the object with a dictionary-based record.

        Args:
            record (dict): Dictionary-based record of Avenger data
        """
        self.record = record

    def url(self):
        """

        Returns:
            str: The URL of the comic character on the Marvel Wikia

        """
        return self.record.get('url')

    def name_alias(self):
        """

        Returns:
            str: The full name or alias of the character

        """
        return self.record.get('name_alias')

    def appearances(self):
        """

        Returns:
            int: The number of comic books that character appeared in as of April 30

        """
        return self.record.get('appearances')

    def is_current(self):
        """

        Returns:
            bool: Is the member currently active on an avengers affiliated team? (True/False)

        """
        return self.record.get('is_current')

    def gender(self):
        """

        Returns:
            str: The recorded gender of the character

        """
        return self.record.get('gender')

    def year(self):
        """

        Returns:
            int: The year the character was introduced as a full or reserve member of the Avengers

        """
        return self.record.get('year')

    def date_joined(self):
        """

        Returns:
            datetime.date: The date the character joined

        """
        return self.record.get('date_joined')

    def days_since_joining(self):
        """

        Returns:
            int: The number of integer days since the character joined

        """
        return self.record.get('days_since_joining')

    def years_since_joining(self):
        """

        Returns:
            int: The number of integer years since the character joined

        """
        return self.record.get('years_since_joining')

    def notes(self):
        """STRIP OFF TRAILING NEWLINES AND SPACES

        Returns:
            str: Descriptions of deaths and resurrections.

        """
        return self.record.get('notes')

    def __str__(self):
        """

        Returns:
            str: A human-readable value for this character

        """
        return '[Avenger: %s]' % self.record

    def __repr__(self):
        """

        Returns:
            str: String representation of object.  Useful for debugging.
        """
        return '[Avenger: %s]' % self.record

    def to_markdown():
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
            '/Users/Love/Documents/GitHub/msds510/reports/top_ten_appearances.md', 'w')
        t = 0
        while t < 10:
            f.write('# ' + str(t + 1)+'. ' + str(c[t][1]) + '\n')
            f.write('* Number of Appearance: ' + str(c[t][2]) + '\n')
            f.write('* Year Joined: ' + str(c[t][7]) + '\n')
            f.write('* Years Since Joining: ' + str(
                utils.years_since_joined((c[t][7]), c[t][6])) + '\n')
            f.write('* URL: ' + str(c[t][0]) + '\n')
            f.write('\n')
            f.write('## Notes' + '\n')
            f.write(''+str(c[t][20]) + '\n')
            t += 1
        f.close()

print(Avenger.to_markdown())
