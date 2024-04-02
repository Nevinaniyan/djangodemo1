# {#
# In Django, when you render a web page using a template, you often need to pass some data from your views to the template. This data could be anything from user information to the contents of a blog post.
#
# Context processors help you by automatically adding certain data to every template without you having to explicitly pass it from every view. Think of context processors as a way to provide common information or settings across multiple templates without repeating yourself.
#
# For example, you might want to include the name and URL of your website in the footer of every page. Instead of passing this data from every view, you can use a context processor to automatically add it to the context of every template.
#
# Here's how it works:
#
# You define a context processor function that returns a dictionary of data you want to add to the template context.
# You tell Django to use this context processor by adding its path to the context_processors list in your project settings.
# Django automatically calls this context processor function for every request and adds its returned data to the template context.
# Now, the data provided by your context processor is available in every template, so you can use it without having to pass it from every view.
# This makes it easier to maintain consistency across your templates and reduces the amount of code you need to write. Context processors are especially useful for providing common information, like site-wide settings or user authentication data, to all your templates.
# #}

from shop.models import Categories

def links(request):
    c = Categories.objects.all()
    return {'links':c}