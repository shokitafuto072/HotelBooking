from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import RoomType, Plan, Reservation,RoomAllocation,User
from django.contrib.auth.decorators import login_required
from django.views import View
from .forms import ReservationForm, PlanForm, RoomTypeForm, RoomAllocationForm
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

"""

@login_required
def booking_confirmation(request):
    if request.method == 'POST':
        selected_plan_id = request.POST.get('plan_id')
        selected_room_id = request.session.get('selected_room')

        if not selected_plan_id or not selected_room_id:
            return HttpResponse("必須データが欠けています!", status=400)

        # 部屋とプランを取得
        selected_room = RoomType.objects.get(id=selected_room_id)
        selected_plan = Plan.objects.get(id=selected_plan_id)

        # セッションにプラン情報を保存
        request.session['selected_plan'] = selected_plan_id

        return render(request, 'booking_confirmation.html', {
            'room_type': selected_room,
            'plan': selected_plan
        })
    return HttpResponse("無効なリクエストです！", status=400)

@login_required
def booking_complete(request):
    if request.method == 'POST':
        selected_room_id = request.session.get('selected_room')
        selected_plan_id = request.session.get('selected_plan')
        payment_method = request.POST.get('payment_method')

        if not selected_room_id or not selected_plan_id or not payment_method:
            return HttpResponse("必須データが欠けています!", status=400)

        selected_room = RoomType.objects.get(id=selected_room_id)
        selected_plan = Plan.objects.get(id=selected_plan_id)

        reservation = Reservation.objects.create(
            user=request.user,
            room_type=selected_room,
            plan=selected_plan,
            reservation_date="2024-11-26",
            payment_method=payment_method
        )

        request.session.pop('selected_room', None)
        request.session.pop('selected_plan', None)

        return render(request, 'booking_complete.html', {
            'room_type': selected_room,
            'plan': selected_plan,
            'payment_method': payment_method,
        })
    return HttpResponse("無効なリクエストです！", status=400)




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

def update_plan(request):
    if request.method == 'POST':
        form = PlanForm(request.POST)
        if form.is_valid():
            form.save()  # フォームのデータをデータベースに保存
            return redirect('bookingfront:home')  # 保存後にリダイレクト

    else:
        form = PlanForm()
    
    return render(request, 'update_plan.html', {'form': form})



def delete_plan(request, plan_id):
    plan = get_object_or_404(Plan, pk=plan_id)  # post_idに対応するPostオブジェクトを取得
    plan.delete()  # データベースから削除
    return redirect('bookingfront:sousa')  # 削除後にリダイレクト


def update_room_type(request):
    if request.method == 'POST':
        form = RoomTypeForm(request.POST)
        if form.is_valid():
            form.save()  # フォームのデータをデータベースに保存
            return redirect('bookingfront:home')  # 保存後にリダイレクト

    else:
        form = RoomTypeForm()
    
    return render(request, 'update_room_type.html', {'form': form})

def delete_room_type(request, room_type_id):
    room_type = get_object_or_404(RoomType, pk=room_type_id)  # post_idに対応するPostオブジェクトを取得
    room_type.delete()  # データベースから削除
    return redirect('bookingfront:sousa')  # 削除後にリダイレクト


def sousa(request):
    plans=Plan.objects.all()
    room_types=RoomType.objects.all()
    return render(request, 'sousa.html', {'plans': plans, 'room_types': room_types})
 
    




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
        room_allocation_id = request.POST.get('roomallocation_id')  # 対応する部屋のIDも送信されていると仮定
        
        # 選択された予約を取得
        reservation = get_object_or_404(Reservation, id=reservation_id)
        room_allocation = get_object_or_404(RoomAllocation, id=room_allocation_id)
        
        # 部屋割り当てに予約を関連付け
        room_allocation.reservation = reservation  # `RoomAllocation`に予約を設定
        room_allocation.save()  # 保存
        
        return redirect('bookingfront:room_assignment')  # リダイレクトして更新された情報を表示
    
    return render(request, 'room_assignment.html', {
        'room_allocations': room_allocations,
        'user_reservations': user_reservations,
    })

@login_required
def update_room_allocation(request):
    if request.method == 'POST':
        form = RoomAllocationForm(request.POST)
        if form.is_valid():
            form.save()  # フォームのデータをデータベースに保存
            return redirect('bookingfront:room_assignment')  # 保存後にリダイレクト

    else:
        form = RoomAllocationForm()
    
    return render(request, 'update_room_allocation.html', {'form': form})

@login_required
def delete_room_allocation(request, room_allocation_id):
    room_allocation = get_object_or_404(RoomAllocation, pk=room_allocation_id)  # post_idに対応するPostオブジェクトを取得
    room_allocation.delete()  # データベースから削除
    return redirect('bookingfront:room_assignment')  # 削除後にリダイレクト

   
