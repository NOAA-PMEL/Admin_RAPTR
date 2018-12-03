from django.test import TestCase
from django.urls import reverse


class IndexPageTests(TestCase):

    def test_index_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 301)

    def test_index_view_url_by_name(self):
        response = self.client.get(reverse('raptr:index'))
        self.assertEquals(response.status_code, 200)

    def test_index_view_uses_correct_template(self):
        response = self.client.get(reverse('raptr:index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'raptr/index.html')

    def test_index_page_contains_correct_html(self):
        response = self.client.get(reverse('raptr:index'))
        self.assertContains(response, '<title>RAPTR Dashboard</title>')


class ContactListPageTests(TestCase):

    def test_contact_list_page_status_code(self):
        response = self.client.get('/raptr/contact')
        self.assertEquals(response.status_code, 301)

    def test_contact_list_view_url_by_name(self):
        response = self.client.get(reverse('raptr:contact_list'))
        self.assertEquals(response.status_code, 200)

    def test_contact_list_view_uses_correct_template(self):
        response = self.client.get(reverse('raptr:contact_list'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'raptr/contact_list.html')

    def test_contact_list_page_contains_correct_html(self):
        response = self.client.get(reverse('raptr:contact_list'))
        self.assertContains(response, '<title>RAPTR Contact List</title>')


class ProjectListPageTests(TestCase):

    def test_project_list_page_status_code(self):
        response = self.client.get('/raptr/project')
        self.assertEquals(response.status_code, 301)

    def test_project_list_view_url_by_name(self):
        response = self.client.get(reverse('raptr:project_list'))
        self.assertEquals(response.status_code, 200)

    def test_project_list_view_uses_correct_template(self):
        response = self.client.get(reverse('raptr:project_list'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'raptr/project_list.html')

    def test_project_list_page_contains_correct_html(self):
        response = self.client.get(reverse('raptr:project_list'))
        self.assertContains(response, '<title>RAPTR Project List</title>')


class AboutPageTests(TestCase):

    def test_about_page_status_code(self):
        response = self.client.get('/raptr/about')
        self.assertEquals(response.status_code, 301)

    def test_about_view_url_by_name(self):
        response = self.client.get(reverse('raptr:about'))
        self.assertEquals(response.status_code, 200)

    def test_about_view_uses_correct_template(self):
        response = self.client.get(reverse('raptr:about'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'raptr/about.html')

    def test_about_page_contains_correct_html(self):
        response = self.client.get(reverse('raptr:about'))
        self.assertContains(response, '<title>About RAPTR</title>')