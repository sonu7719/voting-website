from django.http import HttpResponse
from django.shortcuts import render
from result.models import vote, cal_votes

# Create your views here.
def result (request):
    return HttpResponse("this result  page")

def voting(request):
    if request.method == 'POST':
        First_name = request.POST.get('First_name')
        Age = request.POST.get('Age')
        party = request.POST.get('PARTY_CHOICES')
        print(First_name, Age, party)
        V = vote()
        V.First_name = First_name
        V.Age = Age
        V.party = party
        
        V.save()
        votes = cal_votes.objects.get(party = party)
        votes.n_vote+=1
        votes.save()
        all_v = cal_votes.objects.all()
        return render(request, 'vote.html',{'all_v':all_v})
        
    return render (request,'vote.html') 
    
