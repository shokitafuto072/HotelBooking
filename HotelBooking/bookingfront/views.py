from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import RoomType, Plan, Reservation,RoomAllocation,User
from django.contrib.auth.decorators import login_required
from django.views import View
from .forms import ReservationForm
from django.urls import reverse


"""
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
"""  

def already(request):
    return render(request, 'already.html')

@login_required
def delete_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    
    if reservation.user == request.user or request.user.is_superuser:
        reservation.delete()
        return redirect(reverse('bookingfront:yoyaku'))  # 削除後にリストにリダイレクト
    else:
        return HttpResponse("You do not have permission to delete this reservation.", status=403)
    
    
@login_required
def update_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)

    # もしユーザーが予約の所有者でない場合や管理者でない場合はエラーメッセージを表示
    if reservation.user != request.user and not request.user.is_superuser:
        return HttpResponse("You do not have permission to update this reservation.", status=403)

    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect(reverse('bookingfront:yoyaku'))  # 更新後にリストページにリダイレクト
    else:
        form = ReservationForm(instance=reservation)

    return render(request, 'update_reservation.html', {'form': form, 'reservation': reservation})       
   
    
@login_required  
def yoyaku(request):
    reservations = Reservation.objects.filter(user=request.user) 
    return render(request, 'yoyaku.html', {'reservations': reservations})
    


def home(request):
    return render(request, 'home.html')

def room_selection(request):
    room_types = RoomType.objects.all()
    return render(request, 'room_selection.html', {'room_types': room_types,})



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

    
@login_required
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




@login_required
def room_assignment(request):
    room_allocations = RoomAllocation.objects.all()
    user_reservations = [
        {'id': reservation.id, 'first_name': reservation.user.first_name, 'last_name': reservation.user.last_name}
        for reservation in Reservation.objects.all()
    ]

    if request.method == 'POST':
        # フォームから送られてきた予約情報を取得
        reservation_id = request.POST.get('reservation')
        roomallocation_id = request.POST.get('roomallocation_id')  # 対応する部屋のIDも送信されていると仮定
        
        # 選択された予約を取得
        reservation = get_object_or_404(Reservation, id=reservation_id)
        roomallocation = get_object_or_404(RoomAllocation, id=roomallocation_id)
        
        # 部屋割り当てに予約を関連付け
        roomallocation.reservation = reservation  # `RoomAllocation`に予約を設定
        roomallocation.save()  # 保存
        
        return redirect('bookingfront:room_assignment')  # リダイレクトして更新された情報を表示
    
    return render(request, 'room_assignment.html', {
        'room_allocations': room_allocations,
        'user_reservations': user_reservations,
    })

   