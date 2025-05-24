from django.shortcuts import render, redirect
from .forms import PatchForm
from .utils import merge_and_zip
from .models import Patch
from .notion_logger import log_to_notion


def upload_patch(request):
    if request.method == 'POST':
        form = PatchForm(request.POST, request.FILES)
        if form.is_valid():
            patch = form.save()

            merge_and_zip(patch.patch_file.path, f'files/{patch.zip_name}.zip')

            # Notion 연동 제거
            # log_to_notion(patch.author, patch.description, patch.zip_name)

            return redirect('upload_success')
    else:
        form = PatchForm()  
    return render(request, 'patchlog/upload.html', {'form': form})


def upload_success(request):
    return render(request, 'patchlog/success.html')

def upload_history(request):
    patches = Patch.objects.all().order_by('-created_at')
    return render(request, 'patchlog/history.html', {'patches': patches})


