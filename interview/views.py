from django.shortcuts import render, redirect, get_object_or_404
from .forms import CharacterProfileForm, InterviewForm
from .models import CharacterProfile
from .llama import generate_response

def homepage(request):
    characters = CharacterProfile.objects.all()
    return render(request, 'homepage.html', {'characters': characters})


def create_character(request):
    if request.method == 'POST':
        form = CharacterProfileForm(request.POST)
        if form.is_valid():
            character = form.save() 
            return redirect('interview', character_id=character.id) 
    else:
        form = CharacterProfileForm()

    return render(request, 'create_character.html', {'form': form})

from django.shortcuts import render, get_object_or_404
from .models import CharacterProfile
from .forms import InterviewForm
from .llama import generate_response

def interview(request, character_id):
    character = get_object_or_404(CharacterProfile, id=character_id)
    
    if request.method == 'POST':
        form = InterviewForm(request.POST)
        
        if form.is_valid():
            user_question = form.cleaned_data['question']
            
            
            character_name = character.name
            character_description = f"Personality: {character.personality}\nBackstory: {character.backstory}\nFear: {character.fear}\nDream: {character.dream}\nSecret: {character.secret}"
            
          
            character_response = generate_response(character_name, character_description, user_question)
            
            return render(request, 'interview.html', {
                'form': form,
                'character': character,
                'response': character_response,
                'user_question': user_question
            })
    else:
        form = InterviewForm()
    
    return render(request, 'interview.html', {
        'form': form,
        'character': character
    })


