from django.shortcuts import render, redirect
from covtrack.utils import get_plot, get_bar, get_pie
from covid import Covid

def home(request):
    return render(request, 'home.html')

def load_data(request):
    covid = Covid()
    world_covid_data = covid.get_data()
    return render(request, 'covid_update.html', {'whole_data':world_covid_data})

def show_graphical(request):
    covid = Covid()
    world_covid_data = covid.get_data()
    country = []
    confirmed_cases = []
    i = 0
    for covid_data in world_covid_data:
        country.append(covid_data['country'])
        confirmed_cases.append(covid_data['confirmed'])
        i+=1
        if i > 25:
            break
    chart = get_bar(country, confirmed_cases)
    return render(request, 'show_graphical.html', {'chart':chart})

def india_update(request):
    covid = Covid()
    india_covid_data = covid.get_status_by_country_name("india")
    confirmed = india_covid_data['confirmed']
    active = india_covid_data['active']
    recovered = india_covid_data['recovered']
    death = india_covid_data['deaths']
    cases = [confirmed, active, recovered, death]
    type = ['confirmed_cases', 'active_cases', 'recovered_cases', 'deaths']
    clrs = ['r', 'y', 'g', 'b']
    chart = get_pie(cases, type, clrs)
    return render(request, 'show_graphical.html', {'chart':chart})

def covid_sypmtoms(request):
    symptoms = ['fever','dry cough','tiredness','aches and pains','sore throat','diarrhoea','conjunctivitis',
    'headache','loss of taste or smell','a rash on skin, or discolouration of fingers or toes','difficulty breathing or shortness of breath','chest pain or pressure','loss of speech or movement']
    return render(request, 'cov_symptoms.html', {'symptoms':symptoms})

def covid_preventions(request):
    preventions = [
        'Clean your hands often. Use soap and water, or an alcohol-based hand rub.',
        'Maintain a safe distance from anyone who is coughing or sneezing.',
        'Wear a mask when physical distancing is not possible.',
        'Don’t touch your eyes, nose or mouth.',
        'Cover your nose and mouth with your bent elbow or a tissue when you cough or sneeze.',
        'Stay home if you feel unwell.',
        'If you have a fever, cough and difficulty breathing, seek medical attention.'
        ]
    return render(request, 'cov_symptoms.html', {'preventions':preventions})

# Create your views here.
