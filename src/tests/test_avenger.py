if __name__ == '__main__':
    import unittest

    from src.msds510.avenger import Avenger

    pym_record = {
        'appearances': '1269',
        'current': 'YES',
        'death1': 'YES',
        'death2': '',
        'death3': '',
        'death4': '',
        'death5': '',
        'full_reserve_avengers_intro': 'Sep-63',
        'gender': 'MALE',
        'honorary': 'Full',
        'name_alias': 'Henry Jonathan "Hank" Pym',
        'notes': 'Merged with Ultron in Rage of Ultron Vol. 1. A funeral was held. \n',
        'probationary_introl': '',
        'return1': 'NO',
        'return2': '',
        'return3': '',
        'return4': '',
        'return5': '',
        'url': 'http://marvel.wikia.com/Henry_Pym_(Earth-616)',
        'year': '1963',
        'years_since_joining': '52'
    }

    class TestAvengerClass(unittest.TestCase):
        hank_pym = Avenger(pym_record)
        def test_url(self):
            self.assertEqual(hank_pym.url(), 'http://marvel.wikia.com/Henry_Pym_(Earth-616)')

        def test_name_alias(self):
            self.assertEqual(hank_pym.name_alias(), 'Henry Jonathan "Hank" Pym')

        def test_appearances(self):
            self.assertEqual(hank_pym.appearances(), '1269')

        def test_is_current(self):
            self.assertEqual(hank_pym.is_current(), None)

        def test_gender(self):
            self.assertEqual(hank_pym.gender(), 'MALE')

        def test_year(self):
            self.assertEqual(hank_pym.year(), '1963')

        def test_date_joined(self):
            self.assertEqual(hank_pym.date_joined(), None)

        def test_days_since_joining(self):
            self.assertEqual(hank_pym.days_since_joining(), None)

        def test_years_since_joining(self):
            self.assertEqual(hank_pym.years_since_joining(), '52')

        def test_notes(self):
            self.assertEqual(hank_pym.notes(), 'Merged with Ultron in Rage of Ultron Vol. 1. A funeral was held. \n')

        def test___str__(self):
            self.assertEqual(hank_pym.__str__(), '''[Avenger: {'appearances': '1269', 'current': 'YES', 'death1': 'YES', 'death2': '', 'death3': '', 'death4': '', 'death5': '', 'full_reserve_avengers_intro': 'Sep-63', 'gender': 'MALE', 'honorary': 'Full', 'name_alias': 'Henry Jonathan "Hank" Pym', 'notes': 'Merged with Ultron in Rage of Ultron Vol. 1. A funeral was held. \n', 'probationary_introl': '', 'return1': 'NO', 'return2': '', 'return3': '', 'return4': '', 'return5': '', 'url': 'http://marvel.wikia.com/Henry_Pym_(Earth-616)', 'year': '1963', 'years_since_joining': '52'}]''')

        def test___repr__(self):
            self.assertEqual(hank_pym.__repr__(), '''[Avenger: {'appearances': '1269', 'current': 'YES', 'death1': 'YES', 'death2': '', 'death3': '', 'death4': '', 'death5': '', 'full_reserve_avengers_intro': 'Sep-63', 'gender': 'MALE', 'honorary': 'Full', 'name_alias': 'Henry Jonathan "Hank" Pym', 'notes': 'Merged with Ultron in Rage of Ultron Vol. 1. A funeral was held. \n', 'probationary_introl': '', 'return1': 'NO', 'return2': '', 'return3': '', 'return4': '', 'return5': '', 'url': 'http://marvel.wikia.com/Henry_Pym_(Earth-616)', 'year': '1963', 'years_since_joining': '52'}]''')


    class Testtomarkdown(unittest.TestCase):

        def test_to_markdown(self):
            self.assertEquals((Avenger.to_markdown(), )
