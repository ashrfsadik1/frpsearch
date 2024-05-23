from django.shortcuts import render, redirect
from SearchEngine.search import google
from django.contrib.auth.models import User
from display.models import Display,Display_Data
#from SearchEngine.search import google,yahoo,duck,ecosia, bing, givewater

def homepage(request):
    user_count=User.objects.count()
    sites_count=Display.objects.count()
    sucuss_count=Display_Data.objects.filter(choosenum=1).count()
    print(sucuss_count)
    failed_count=Display_Data.objects.filter(choosenum=2).count()
    print(failed_count)
    context={
        "user_count":user_count,
        "sites_count":sites_count,
        "sucuss_count":sucuss_count,
        "failed_count":failed_count,
    }
    return render(request,'index.html',{'context':context})

def searchpage(request):
    return render(request,'home.html')
def results(request):
    if request.method == "POST":
        result = request.POST.get('search')
        google_link,google_text = google(result)
        google_data = zip(google_link,google_text )
        # yahoo_link,yahoo_text = yahoo(result)
        # yahoo_data = zip(yahoo_link,yahoo_text)
        # duck_link,duck_text = duck(result)
        # duck_data = zip(duck_link,duck_text)
        # ecosia_link,ecosia_text = ecosia(result)
        # ecosia_data = zip(ecosia_link,ecosia_text)
        # bing_link,bing_text = bing(result)
        # bing_data = zip(bing_link,bing_text)
        # givewater_link,givewater_text = givewater(result)
        # givewater_data = zip(givewater_link,givewater_text)




        if result == '':
            return redirect('Home')
        else:
            
            
            return render(request,'results.html',{'google': google_data})
            #return render(request,'results.html',{'google': google_data, 'yahoo': yahoo_data, 'duck': duck_data, 'ecosia': ecosia_data,'bing': bing_data, 'givewater': givewater_data})
