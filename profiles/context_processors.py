from .models import Profile



def profile_pic(request):
    if request.user.is_authenticated:
        user=request.user
        try:
            profile_obj=Profile.objects.get(user=user)
            pic=profile_obj.profile_picture
        except Profile.DoesNoTExist:
            pic=None

        return {'picture':pic}
    return {}

def get_profile(request):
    if request.user.is_authenticated:
        user=request.user
        try:
            profile_obj=Profile.objects.get(user=user)
        except Profile.DoesNotExist:
            pic=None
        return {"profile":profile_obj}
    return {}

