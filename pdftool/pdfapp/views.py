from django.http import JsonResponse
from pdfgen import Topdftool



def scrape_api(request):
    input_folder_path = request.GET.get('input_folder_path')
    output_folder_path = request.GET.get('output_folder_path')

    # Call the scrape_files function with the input and output folder paths
    
    Topdftool.scrape_files(input_folder_path, output_folder_path)

    # Return a JSON response indicating the success of the API request
    return JsonResponse({'status': 'success'})
