from django.shortcuts import render
from django.http import JsonResponse
import csv
from django.core.paginator import Paginator
from .models import BlogPost
from .utils import get_user_country

def post_list(request):
    detected_country = get_user_country(request=request) #Detect country name using IP address of the user

    posts = BlogPost.objects.all()

    #Pagination for show limited post per page
    page_number = request.GET.get('page', 1)  # Default to page 1
    paginator = Paginator(posts, 12)  # 12 posts per page
    page_obj = paginator.get_page(page_number)


    return render(request, 'blog/post_list.html', {
        'posts': posts,
        'detected_country': detected_country,
        'page_obj': page_obj,
    })


 # View to upload a CSV file and store its data in the database.1
def upload_csv(request):
   
    if request.method == "POST" and request.FILES.get("csv_file"):
        csv_file = request.FILES["csv_file"]

        # Check if the file is a valid CSV
        if not csv_file.name.endswith(".csv"):
            return JsonResponse({"error": "File is not a CSV."}, status=400)

        try:
            # Decode the file and read its content
            data = csv_file.read().decode("utf-8").splitlines()
            reader = csv.reader(data)

            # Iterate through the rows and save to the database
            for row in reader:
                BlogPost.objects.create(
                    title=row[0],
                    content=row[1],
                    country=row[2]  
                )

            return JsonResponse({"success": "Data uploaded successfully."})

        except Exception as e:
            return JsonResponse({"error": f"Error processing file: {str(e)}"}, status=500)

    return render(request, "blog/upload_file.html")
