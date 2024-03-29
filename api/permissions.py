from rest_framework import permissions

class HasAccount(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        ## Read-only permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return  True
        ## Transaction permission are only allowed to the owner  of a account
        return obj.amount == request.user