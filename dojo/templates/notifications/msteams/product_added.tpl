{% load i18n %}
{% load display_tags %}
{
    "@context": "https://schema.org/extensions",
    "@type": "MessageCard",
    "title": "{% trans "Product Added" %}",
    "summary": "{% trans "Product Added" %}",
    "sections": [
        {
            "activityTitle": "ExposureX",
            "activityImage": "https://raw.githubusercontent.com/ExposureX/django-ExposureX/master/dojo/static/dojo/img/logo.svg",
            "text": "{% trans "A new product has been added" %}.",
            "facts": [
                {
                    "name": "{% trans "Product" %}:",
                    "value": "{{ title }}"
                }
            ]
        }
        {% if system_settings.disclaimer_notifications and system_settings.disclaimer_notifications.strip %}
            ,{
                "activityTitle": "{% trans "Disclaimer" %}",
                "text": "{{ system_settings.disclaimer_notifications }}"
            }
        {% endif %}
    ],
    "potentialAction": [
        {
            "@type": "OpenUri",
            "name": "{% trans "View Product" %}",
            "targets": [
                {
                    "os": "default",
                    "uri": "{{ url|full_url }}"
                }
            ]
        }
    ]
}
