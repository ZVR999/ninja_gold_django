# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from random import randint
from datetime import datetime

def index(request):
    if not 'gold_counter' in request.session:
        request.session['gold_counter'] = 0
    return render(request, 'ninja/index.html')

def process_money(request,number):
    current_time = datetime.now()
    now = current_time.strftime('%Y/%m/%d %I:%M %p')
    if not 'activity' in request.session:
        request.session['activity'] = ''

    random_number = 0
    gold_amount = 0
    building = ''
    pos_start = '<div class= "green">Earned'
    neg_start = '<div class= "red">Entered a casino and lost'
    neg_end = 'gold...ouch..'
    where = 'gold from the'
    time = '! ('+now+')</div>'
    # Create an array to hold the divs from request.session['activity'] to then display in the in the activities section
    if not 'history' in request.session:
        request.session['history'] = []
    # Farm
    if number == '1':
        random_number = randint(10,20)
        request.session['gold_counter'] += random_number 
        gold_amount = random_number
        building = 'farm'
        request.session['activity'] = '{} {} {} {}{}'.format(pos_start,str(gold_amount),where,building,str(time)) 
    # Cave
    elif number == '2':
        random_number = randint(5,10)
        request.session['gold_counter'] += random_number
        gold_amount = random_number
        building = 'cave'
        request.session['activity'] = '{} {} {} {}{}'.format(pos_start,str(gold_amount),where,building,str(time))
    # House
    elif number == '3':
        random_number = randint(2,5)
        request.session['gold_counter'] += random_number
        gold_amount = random_number
        building = 'house'
        request.session['activity'] = '{} {} {} {}{}'.format(pos_start,str(gold_amount),where,building,str(time))
    # Casino
    elif number == '4':
        random_number = randint(-50,50)
        request.session['gold_counter'] += random_number
        gold_amount = random_number
        building = 'casino'
        if gold_amount < 0:
            request.session['activity'] = '{} {} {}{}'.format(neg_start,str(gold_amount),neg_end,str(time))
        else:
            request.session['activity'] = '{} {} {} {}{}'.format(pos_start,str(gold_amount),where,building,str(time))
    
    history = request.session['history'] 
    activity = request.session['activity']
    history.append(activity)
    
    # Make sure the last entry stay in the top part of the activities section
    if len(history) > 1:
        def revese(arr):
            for x in range(0,1):
                arr.insert(0,arr[-1])
                arr.pop()
            return arr            

        revese(history)


    return redirect('/')

# Reset game
def reset(request):
    request.session['activity'] = ''
    request.session['history'] = []
    request.session['gold_counter'] = 0
    return redirect('/')