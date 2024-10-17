from django.shortcuts import render, redirect, get_object_or_404
import requests
from .forms import MakeForm  
from django.http import HttpResponse


def makes(request):
    api_url = "https://mobii.api.bluespacefinancial.cloud/makes/" 
    response_data = None
    error_message = None
    search_query = request.GET.get('q', '') 

    if request.method == 'POST':  # At the point of clicking the button, a post request is sent 
        try:
            response = requests.get(api_url) # At the point of sending the http request, a get method is sent
            
            # Check for HTTP status code errors
            if response.status_code == 400:
                error_message = "400 Bad Request"
            elif response.status_code == 401:
                error_message = "401 Unauthorized Request"
            elif response.status_code == 403:
                error_message = "403 Forbidden Request"
            elif response.status_code == 500:
                error_message = "500 Internal Server Error"
            elif response.status_code == 200:
                response_data = response.json()
                
                # Filter the makes data based on search query
                if search_query:
                    response_data = [make for make in response_data if search_query.lower() in make['name'].lower()]
            else:
                # Process JSON response if no error
                error_message = f"Error: {response.status_code}"
        except requests.exceptions.RequestException as e:
            error_message = f"Error: {str(e)}"

    return render(request, 'home.html', {'makes_data': response_data, 'error_message': error_message})

def search_results(request):
    api_url = "https://mobii.api.bluespacefinancial.cloud/makes/"
    response_data = None
    error_message = None
    search_query = request.GET.get('q', '')

    try:
        response = requests.get(api_url)  # Fetch all makes

        if response.status_code == 200:
            response_data = response.json()
            # Filter the makes data based on search query
            if search_query:
                response_data = [make for make in response_data if search_query.lower() in make['name'].lower()]
        else:
            error_message = f"Error: {response.status_code}"

    except requests.exceptions.RequestException as e:
        error_message = f"Error: {str(e)}"

    return render(request, 'search_results.html', {
        'makes_data': response_data,
        'error_message': error_message,
        'search_query': search_query
    })

def delete_make_view(request, id):
    api_url = f"https://mobii.api.bluespacefinancial.cloud/makes/del/{id}"  # API for deletion
    error_message = None
    success_message = None

    if request.method == 'POST':  # Button click triggers the DELETE request
        try:
            response = requests.delete(api_url)
            
            if response.status_code == 200:
                success_message = "Delete successful!"
                return render(request, 'home.html', {'success_message': success_message})
            elif response.status_code == 204:
                success_message = "Delete successful!"
                return render(request, 'home.html', {'success_message': success_message})
            elif response.status_code == 404:
                error_message = "404 Not Found: Make not found."
            else:
                error_message = f"Error: {response.status_code}"
        except requests.exceptions.RequestException as e:
            error_message = f"Request failed: {str(e)}"

    return render(request, 'home.html', {
        'error_message': error_message,
        'success_message': success_message,
    })



def new_make(request):
    error_message = None
    if request.method == 'POST':
        form = MakeForm(request.POST)
        if form.is_valid():
            # Extract form data
            name = form.cleaned_data['name']
            logo = form.cleaned_data['logo']
            is_phone = form.cleaned_data['is_phone']
            is_television = form.cleaned_data['is_television']
            is_laptop = form.cleaned_data['is_laptop']
            is_wearable = form.cleaned_data['is_wearable']
            
            # Send data to the API
            api_url = "https://mobii.api.bluespacefinancial.cloud/makes/new/"
            data = {
                'name': name,
                'logo': logo,
                'is_phone': is_phone,
                'is_television': is_television,
                'is_laptop': is_laptop,
                'is_wearable': is_wearable
            }

            try:
                response = requests.post(api_url, json=data)
                if response.status_code == 201:
                    response_data = "201: Make created successfully."
                    return redirect('home')  # Redirect after success
                elif response.status_code == 400:
                    error_message = "400 Bad Request: Invalid data."
                elif response.status_code == 401:
                    error_message = "401 Unauthorized: Authentication failed."
                elif response.status_code == 403:
                    error_message = "403 Forbidden: Access denied."
                elif response.status_code == 500:
                    error_message = "500 Internal Server Error: Server failed to process request."
                else:
                    return HttpResponse(f"Failed to create make. Status code: {response.status_code}")
            except requests.exceptions.RequestException as e:
                return HttpResponse(f"An error occurred: {str(e)}")
    else:
        form = MakeForm()

    return render(request, 'new_make.html', {
        'form': form, 
        'error_message': error_message,
    })



def make_detail(request, make_id):
    api_url = f"https://mobii.api.bluespacefinancial.cloud/makes/{make_id}/"  # API URL for a specific make
    error_message = None
    make_data = None

    try:
        response = requests.get(api_url)
        
        # Check for HTTP status code errors
        if response.status_code == 200:
            make_data = response.json()  # Parse JSON response to get the make details
        elif response.status_code == 404:
            error_message = "Unable to fetch details for make-id", make_id
        else:
            make_data = response.json()
    
    except requests.exceptions.RequestException as e:
        error_message = f"Error: {str(e)}"

    # Ensure the function returns an HttpResponse (even if it's just the error message)
    return render(request, 'make_detail.html', {'make_data': make_data, 'error_message': error_message})

    

#  define function with request
#  Copy the url 
# Have both response and error message
# Request coming from the frontend (Button == "POST")
#  Try
        # Send out request to the api using "get"
        # Handle all responses/errors and assign them to the response and error fields 
        #  Return the response and error message
        #  Except (HTTP except requests.exceptions.RequestException as e:
       #                             error_message = f"Error: {str(e)}")
       # Render --> render(request, 'make_detail.html', {'make_data': make_data, 'error_message': error_message})
       
# Modify to be a search 

