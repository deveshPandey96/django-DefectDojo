{% load i18n %}
{% load display_tags %}
{
    "@context": "https://schema.org/extensions",
    "@type": "MessageCard",
    "title": "{% trans "Event" %}",
    "summary": "{% trans "Event" %}",
    "sections": [
        {
            "activityTitle": "ExposureX",
            "activityImage": "https://raw.githubusercontent.com/deveshPandey96/django-ExposureX/master/dojo/static/dojo/img/logo.svg",
            "text": "{% autoescape on %} {{ description }} {% endautoescape %}"
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
            "name": "{% trans "View" %}",
            "targets": [
                {
                    "os": "default",
                    "uri": "{{ url|full_url }}"
                }
            ]
        }
    ]
}
