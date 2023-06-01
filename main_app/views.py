from django.shortcuts import render

finches = [
    {
        'species': 'Zebra Finch',
        'color': 'Grey',
        'beak_size': 'Small',
        'location': 'Australia'
    },
    {
        'species': 'Gouldian Finch',
        'color': 'Multi-colored',
        'beak_size': 'Small',
        'location': 'Australia'
    },
    {
        'species': 'Society Finch',
        'color': 'White',
        'beak_size': 'Small',
        'location': 'United States'
    },
    {
        'species': 'Java Sparrow',
        'color': 'Grey',
        'beak_size': 'Medium',
        'location': 'Indonesia'
    },
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

