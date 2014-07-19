from django.views.generic import TemplateView

class AboutView(TemplateView):
    #load home page with link to blockbuilder/phrase
    #rankin had his cheat sheet... now we have this.
    template_name = "about.html"
