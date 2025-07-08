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
                max_prod_a = form.cleaned_data['max_prod_a']
                max_prod_b = form.cleaned_data['max_prod_b']
                file = request.FILES['file']

                data = DataLoader(
                    file = file, 
                    max_prod_a=max_prod_a, 
                    max_prod_b=max_prod_b
                )
                model = OptimizationModel(data.df, max_prod_a=data.max_prod_a, max_prod_b=data.max_prod_b)
                result, total = model.solve()
                context.update({"result": result, "total": total})
                return render(request, "optimizador/results.html", context)
            except Exception as e:
                form.add_error(None, str(e))
            context["form"] = form
        return render(request, "optimizador/upload.html", context)
