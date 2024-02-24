from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from spellchecker import SpellChecker

spell = SpellChecker()

@csrf_exempt

def check_spelling(request):
    if request.method == 'POST':
        print(request.body)
        data = json.loads(request.body.decode('utf-8'))
        input_text = data['text']

        # Split the input text into words
        words = input_text.split()

        # Find misspelled words
        misspelled = spell.unknown(words)

        # Correct misspelled words
        corrected_text = ' '.join(spell.correction(word) if word in misspelled else word for word in words)

        return JsonResponse({'corrected_text': corrected_text})
    

    return JsonResponse({'error': 'Invalid request method'})
