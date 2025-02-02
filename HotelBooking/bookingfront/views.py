from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import RoomType, Plan, Reservation
from django.contrib.auth.decorators import login_required
from .forms import ReservationForm 
from django.views import View



class Yoyaku(View):
    template_name = 'yoyaku.html'
    model=Reservation
    fields = ['user','email','roomtype','Reservation_date']

    def get_queryset(self):
        current_user = self.request.user
        user_data=Reservation.objects.get(user=current_user)
        if user_data:
            queryset = Reservation.objects.filter(user=current_user)
            queryset = queryset.order_by('Reservation_date')
        return queryset
    
    
          
   
    
    
def yoyaku(request):
    reservations = Reservation.objects.all() 
    return render(request, 'yoyaku.html', {'reservations': reservations})
    
def update_yoyaku(request, pk):
        reservation = get_object_or_404(Reservation, pk=pk)
        if request.method == 'POST':
            form = ReservationForm(request.POST, instance=reservation)
            if form.is_valid():
                reservation = form.save(commit=False)
                reservation.save()
                return redirect('yoyaku', pk=reservation.pk)
        else:
            form = ReservationForm(instance=reservation)
        return render(request, 'yoyaku.html', {'form': form})

def delete_yoyaku(request, pk):
        reservation=get_object_or_404(Reservation, pk=pk)
        if request.method == 'POST':
           reservation.delete()
           return redirect('yoyaku')
        return render(request, 'yoyaku.html', {'reservation': reservation})

def home(request):
    return render(request, 'home.html')

def room_selection(request):
    room_types = RoomType.objects.all()
    return render(request, 'room_selection.html', {'room_types': room_types})



def plan_selection(request):
    if request.method == 'POST':
        selected_room = request.POST.get('room_id')
        request.session['selected_room'] = selected_room
        plans = Plan.objects.all()
        return render(request, 'plan_selection.html', {'plans': plans, 'selected_room': selected_room})
    return HttpResponse("Required data is missing!", status=400)

"""
def booking_form(request):
    if request.method == 'POST':
       return render(request, "booking_form.html")
    return HttpResponse("Required data is missing!", status=400)
"""

    
@login_required#(login_url='/accounts/')   
def booking_confirmation(request):
    if request.method == 'POST':
        selected_plan_id = request.POST.get('plan_id')
        selected_room_id = request.session.get('selected_room')

        if not selected_plan_id or not selected_room_id:
            return HttpResponse("Required data is missing!", status=400)

        # 選択された部屋とプランを取得
        selected_room = RoomType.objects.get(id=selected_room_id)
        selected_plan = Plan.objects.get(id=selected_plan_id)

        # セッションに保存
        request.session['selected_plan'] = selected_plan_id

        return render(request, 'booking_confirmation.html', {
            'room_type': selected_room,
            'plan': selected_plan
        })
    return HttpResponse("Invalid request!", status=400)


@login_required(login_url='/accounts/login/')
def booking_complete(request):
    if request.method == 'POST':
        selected_room_id = request.session.get('selected_room')
        selected_plan_id = request.session.get('selected_plan')

        if not selected_room_id or not selected_plan_id:
            return HttpResponse("Required data is missing!", status=400)

        # データを保存
        selected_room = RoomType.objects.get(id=selected_room_id)
        selected_plan = Plan.objects.get(id=selected_plan_id)

        Reservation.objects.create(
            user=request.user, # 追加：ログインユーザーを予約に紐づけ
            room_type=selected_room,
            plan=selected_plan,
            reservation_date="2024-11-26"  # 適宜日付を動的に変更可能
        )

        # セッションをクリア
        request.session.pop('selected_room', None)
        request.session.pop('selected_plan', None)

        return render(request, 'booking_complete.html', {
            'room_type': selected_room,
            'plan': selected_plan,
            'reservation': Reservation,  # 予約情報も渡す
        })
    return HttpResponse("Invalid request!", status=400)



@login_required
def dashboard(request):
    if  request.user.is_superuser:
        return render(request, 'dashboard.html')
    else:
        return render(request, 'notpage.html')
        
def checkinlist(request):
    return render(request, 'checkinlist.html')

def checkoutlist(request):
    return render(request, 'checkoutlist.html')

def guests_list(request):
    reservations = Reservation.objects.all() 
    return render(request, 'guests_list.html', {'reservations': reservations})
   
def clean_manage(request):
    return render(request, 'clean_manage.html')

def kyakusitu(request):
    return render(request, 'kyakusitu.html')

def edit_plans(request):
    return render(request, 'edit_plans.html')

def shukei(request):
    return render(request, 'shukei.html')

def room_status(request):
    return render(request, 'room_status.html')
