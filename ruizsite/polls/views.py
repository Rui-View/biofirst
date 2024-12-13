from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Polls Index</title>
        <!-- Link to Google Fonts for Lobster font -->
        <link href="https://fonts.googleapis.com/css2?family=Lobster&display=swap" rel="stylesheet">
        <style>
            body {
                font-family: 'Lobster', cursive; /* Use Lobster font */
                display: flex; /* Flexbox for centering */
                justify-content: center; /* Center horizontally */
                align-items: center; /* Center vertically */
                height: 100vh; /* Full height viewport */
                margin: 0; /* Remove default margin */
                background-color: #f8f9fa; /* Optional background color */
            }

            h1 {
                font-size: 4rem; /* Make the text larger */
                text-align: center;
                color: #333; /* Optional text color */
            }
        </style>
    </head>
    <body>
        <h1>Hello world! You're at the polls index.</h1>
    </body>
    </html>
    """)