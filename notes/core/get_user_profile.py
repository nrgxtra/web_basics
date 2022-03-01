from notes.user_profile.models import Profile


def get_profile():
    profile = Profile.objects.all().first()
    return profile
