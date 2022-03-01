from django.shortcuts import render, redirect

from petstagram2.pets.models import Pet, Like


def pet_all(request):
    all_pets = Pet.objects.all()
    context = {
        'pets': all_pets
    }

    return render(request, 'pets/pet_list.html', context)


def pet_detail(request, pk):
    pet = Pet.objects.get(pk=pk)
    pet.likes = pet.like_set.count()
    context = {
        'pet': pet
    }
    return render(request, 'pets/pet_detail.html', context)


def like_pet(request, pk):
    like = Like(pet_id=pk)
    like.save()

    return redirect('pet details', pk)
