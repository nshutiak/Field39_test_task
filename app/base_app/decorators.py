import functools
from django.core.exceptions import PermissionDenied


def check_form_accessibility(view_func):
    """
        this decorator ensures that a user has rights to fill the form
    """

    @functools.wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.form_access == True:
            return view_func(request, *args, **kwargs)
        raise PermissionDenied()

    return wrapper