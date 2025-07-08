from django.shortcuts import render, redirect
from .forms import UploadForm
from .optimization.dataloader import DataLoader
from .optimization.model import OptimizationModel

def upload(request):
    context = {}
    form = UploadForm()
    context["form"] = form
    return render(request, "optimizador/upload.html", context)

def results(request):
    context = {}
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                data = DataLoader(request.FILES['file'])
                model = OptimizationModel(data.df)
                result, total = model.solve()
                context.update({"result": result, "total": total})
                return render(request, "optimizador/results.html", context)
            except Exception as e:
                form.add_error(None, str(e))
            context["form"] = form
        return render(request, "optimizador/upload.html", context)
