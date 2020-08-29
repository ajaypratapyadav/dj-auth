from django.test import TestCase
from django.urls import reverse


class HomePageTests(TestCase):

    def setUp(self):
        self.home_url = reverse('home')

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_contains_correct_html(self):
        response = self.client.get('/')
        self.assertContains(response, '<h2>Hello, Welcome on Investor or Borrower Django App!</h2>')

    def test_home_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/')
        self.assertNotContains(
            response, 'Hi there! I should not be on the page.')


class TestView(TestCase):

    def setUp(self, data={}):
        self.borrower_list = reverse('borrowerList')
        self.change_investor_status = reverse('changeInvestorStatus')
        self.investor_group_list = reverse('getGroup')

    def test_change_investor_status_GET(self):
        self.client.login(email="ajaypratapyadav002@bgmail.com", password="ajay@002")
        response = self.client.get(self.borrower_list)
        self.assertEquals(response.status_code, 302)

    def test_investor_group_list_GET(self):
        response = self.client.get(self.investor_group_list)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'group.html')
