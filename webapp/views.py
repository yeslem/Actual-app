from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from .models import Material, Head

from .import forms

@login_required(login_url="/login/")
def AddMaterial(request):
    form=forms.AddMaterial()
    return render(request, 'webapp/Add_Material.html',{'form':form})


@login_required(login_url="/login/")
def selection(request, ):
    form = ''
    if request.method == 'POST':
        form=forms.Pressure_choice(request.POST)
    return render(request, 'webapp/selection.html',{'form':form})


@login_required(login_url="/login/")
def Internal_Pressure(request):
    form=forms.Internal_Pressure()
    return render(request, 'webapp/Internal_Pressure.html',{'form':form})

# some needed values
def thickness_l(p,ro,s,e,c):
   return (p*ro)/((2*s*e)+(1.4*p))+c

def thickness_c(p,ro,s,e,c):
   return (p*ro)/((2*s*e)+(0.4*p))+c

def thickness(p,ro,s,e,c):
     if thickness_l(p,ro,s,e,c) < thickness_c():
          return thickness_c
     else:
          return thickness_l

@login_required(login_url="/login/")
def Internal_Pressure_Results(request):
    # assign variables default values
    thickness=0
    s=0
    error = ''
    # these ones come from the form
    material = request.POST['Material']
    custom_stress = request.POST['Custom_stress']
    pressure = request.POST['Pressure']
    Outer_radius = request.POST['Outer_radius']
    joint_efficiency = request.POST['Joint_efficiency']
    corrosion = request.POST['Corrosion']
    allow_stress = Material.objects.get(pk=material).allow_stress
    # allow_stress = request.POST['allow_stress']

    # do the calculation so I can send result
    p = float(pressure)

    if p < 20684:
        # do calc
        ro = int(Outer_radius)
        e = float(joint_efficiency)
        c = float(corrosion)

        if custom_stress:
            s=int(custom_stress)
        else:
            s=int(allow_stress)

        if thickness_l(p,ro,s,e,c) < thickness_c(p,ro,s,e,c):
            thickness = thickness_c(p, ro, s, e, c)
        else:
            thickness = thickness_l(p, ro, s, e, c)
    else:
        error = 'Pressure too high!'
    # now I pass the calculated values to the result so I can show
    material_name = Material.objects.get(pk=int(material))
    result = {'material': material,
              'material_name': material_name,
              'custom_stress': custom_stress,
              'pressure': pressure,
              'Outer_radius': Outer_radius,
              'corrosion': corrosion,
              'joint_efficiency': joint_efficiency,
              'error': error,
              'thickness': thickness,
              'allow_stress': allow_stress,
             }
    return render(request, 'webapp/Internal_Pressure_Results.html',{'result':result})

@login_required(login_url="/login/")
def External_Pressure_Results(request):
    error = ''
    material = request.POST['Material']
    head = request.POST['Head']
    custom_stress = request.POST['Custom_stress']
    pressure = request.POST['Pressure']
    tan_to_tan = request.POST['Tan_to_Tan_Length']
    outside_diameter = request.POST['Outside_Diameter']
    thickness = request.POST['Thickness']
    step_size = request.POST['Step_size']
    temperature = request.POST['Temperature']
    head_name = Head.objects.get(pk=int(head))
    head_constant = head_name.Constant

    # do the calculation so I can send result
    p = float(pressure)

    if p < 20684:
        ltt = float(tan_to_tan)
        do = float(outside_diameter)
        t= float(thickness)
        step_size= float(step_size)
        temp= float(temperature)

        # todo: check 'el' value
        if custom_stress:
            s=int(custom_stress)
        else:
            s=int(allow_stress)

        allowable_pressure=0

        # TODO: check how to change this, while never ends?
        # while allowable_pressure < p:
        t=t+step_size
        d=do-2*t

        # here we use head constant
        l=ltt + float(head_constant) * d

        # TODO: check this
        # if choice_2 == '1':
        #    allowable_pressure=(3*do/t)

        # elif choice_2 == '2':
        #    allowable_pressure=(4*a*el)/(3*do/t)
        allowable_pressure = 0
    else:
        error = 'Pressure too high!'

    material_name = Material.objects.get(pk=int(material))
    result = {
        'material': material,
        'material_name': material_name,
        'head': head,
        'custom_stress': custom_stress,
        'head_name': head_name,
        'pressure': pressure,
        'tan_to_tan': tan_to_tan,
        'outside_diameter': outside_diameter,
        'thickness': thickness,
        'step_size': step_size,
        'temperature': temperature,
        'thickness_result': t,
        'allow_pressure': 0,
        'error': error,
    }
    return render(request, 'webapp/External_Pressure_Results.html',{'result':result})


@login_required(login_url="/login/")
def External_Pressure(request):
    form=forms.External_Pressure()
    return render(request, 'webapp/External_Pressure.html',{'form':form})

@login_required(login_url="/login/")
def Materials(request):
    if request.POST:
        Name = request.POST['Name']
        elasticity = request.POST['elasticity']
        NewMaterial = Material.objects.create()
        NewMaterial.Name = Name
        NewMaterial.allow_stress = float(allow_stress)
        NewMaterial.elasticity = float(elasticity)
        NewMaterial.save()

        materials = Material.objects.all()
        context = {'materials':materials}
        return render(request, 'webapp/Material_List.html', context)
    else:
        materials = Material.objects.all()
        context = {'materials':materials}
        return render(request, 'webapp/Material_List.html', context)

def Material_delete(request, **kwargs):
    id = kwargs['pk']
    Material.objects.filter(pk=id).delete()
    materials = Material.objects.all()
    context = {'materials': materials}
    return render(request, 'webapp/Material_List.html', context)

@login_required(login_url="/login/")
def AddHead(request):
    form=forms.AddHead()
    return render(request, 'webapp/Add_Head.html',{'form':form})

@login_required(login_url="/login/")
def Heads(request):
    if request.POST:
        Name = request.POST['Name']
        Constant = request.POST['Constant']
        NewHead = Head.objects.create()
        NewHead.Name = Name
        NewHead.Constant = Constant
        NewHead.save()
    else:
        pass
    heads = Head.objects.all()
    context = {'heads': heads}
    return render(request, 'webapp/Head_List.html', context)

@login_required(login_url="/login/")
def Head_delete(request, **kwargs):
    id = kwargs['pk']
    Head.objects.filter(pk=id).delete()
    heads = Head.objects.all()
    context = {'heads': heads}
    return render(request, 'webapp/Head_List.html', context)
