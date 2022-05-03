import unittest
from app.models import NewsArticle

class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the NewsArticle class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = NewArticle('CNN','JANE DOE','Thrilling Stories','/home','/image','14-9-2020','Lorem','Ipsum')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,NewsArticle))