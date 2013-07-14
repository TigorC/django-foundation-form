from django import forms
from django.test import TestCase
from django.template import Template, Context


class TestForm(forms.Form):
    text = forms.CharField(label='text')


class FilterTest(TestCase):
    def setUp(self):
        self.context = Context({'form': TestForm()})

    def test_base_render(self):
        template = Template('{% load foundation %}{{ form|foundation }}')
        rendered = template.render(self.context)
        self.assertIn('class="large-12 columns"', rendered)
        self.assertIn('class="row"', rendered)

    def test_inline_filter(self):
        template = Template('{% load foundation %}{{ form|foundationinline }}')
        rendered = template.render(self.context)
        self.assertIn('class="large-3 columns"', rendered)

    def test_field_render(self):
        template = Template('{% load foundation %}{{ form.text|foundation }}')
        rendered = template.render(self.context)
        self.assertIn('class="large-12 columns"', rendered)
