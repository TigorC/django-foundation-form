# django-foundation-form

Reusable Django app for display [zurb foundation forms](http://foundation.zurb.com/)

## Installation
Install with pip: `pip install foundationform`

Add `'foundationform',` to INSTALLED_APPS

## Usage

Simple form:

```html
{% load foundation %}

<h2>Form</h2>
<form method="POST">
    {{ form|foundation }}
    <button type="submit" class="small button">Submit</button>
</form>
```

Inline labels:

```html
{% load foundation %}

<h2>Form</h2>
<form method="POST">
    {{ form|foundationinline }}
    <button type="submit" class="small button">Submit</button>
</form>
```

Render form fields:
```html
{% load foundation %}

<h2>Form</h2>
<form method="POST">
    {{ form.title|foundation }}
    {{ form.text|foundationinline }}
    <button type="submit" class="small button">Submit</button>
</form>
```

### Running the tests
Install [tox](http://tox.testrun.org/) and run `tox` from the source checkout