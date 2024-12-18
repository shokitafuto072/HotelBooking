from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import RoomType, Plan, Reservation

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
            room_type=selected_room,
            plan=selected_plan,
            reservation_date="2024-11-26"  # 適宜日付を動的に変更可能
        )

        # セッションをクリア
        request.session.pop('selected_room', None)
        request.session.pop('selected_plan', None)

        return render(request, 'booking_complete.html', {
            'room_type': selected_room,
            'plan': selected_plan
        })
    return HttpResponse("Invalid request!", status=400)
